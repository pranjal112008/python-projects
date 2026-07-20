import sqlite3
import re
from datetime import datetime, timedelta
from typing import List, Optional, Tuple
from functools import wraps
DB_FILE = "library.db"
LOAN_DAYS = 14
LATE_FEE_PER_DAY = 2.0
def log_action(action: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {action} executed.")
            return func(*args, **kwargs)
        return wrapper
    return decorator
class Book:
    def __init__(self, book_id: int, title: str, author: str, copies: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
    def to_dict(self):
        return {"book_id": self.book_id, "title": self.title, "author": self.author, "copies": self.copies}
class User:
    def __init__(self, user_id: int, name: str, role: str = "member"):
        self.user_id = user_id
        self.name = name
        self.role = role
class LibraryDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self.create_tables()
    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    copies INTEGER DEFAULT 1
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS borrowings (
                    id INTEGER PRIMARY KEY,
                    book_id INTEGER,
                    user_name TEXT,
                    due_date TEXT,
                    FOREIGN KEY(book_id) REFERENCES books(book_id)
                )
            ''')
    @log_action("Add Book")
    def add_book(self, title: str, author: str, copies: int) -> Book:
        with self.conn:
            cursor = self.conn.execute("INSERT INTO books (title, author, copies) VALUES (?, ?, ?)",
                                     (title, author, copies))
            book_id = cursor.lastrowid
        return Book(book_id, title, author, copies)
    def get_all_books(self) -> List[Book]:
        cursor = self.conn.execute("SELECT * FROM books")
        return [Book(row[0], row[1], row[2], row[3]) for row in cursor.fetchall()]
    @log_action("Issue Book")
    def issue_book(self, book_id: int, user_name: str) -> str:
        cursor = self.conn.execute("SELECT copies FROM books WHERE book_id = ?", (book_id,))
        row = cursor.fetchone()
        if not row or row[0] <= 0:
            raise ValueError("Book not available.")
        due_date = (datetime.now() + timedelta(days=LOAN_DAYS)).strftime("%Y-%m-%d")
        with self.conn:
            self.conn.execute("INSERT INTO borrowings (book_id, user_name, due_date) VALUES (?, ?, ?)",
                            (book_id, user_name, due_date))
            self.conn.execute("UPDATE books SET copies = copies - 1 WHERE book_id = ?", (book_id,))
        return due_date
    @log_action("Return Book")
    def return_book(self, book_id: int, user_name: str) -> Tuple[int, float]:
        cursor = self.conn.execute("SELECT due_date FROM borrowings WHERE book_id = ? AND user_name = ?",
                                 (book_id, user_name))
        row = cursor.fetchone()
        if not row:
            raise ValueError("No borrowing record found.")
        due_date = datetime.strptime(row[0], "%Y-%m-%d")
        days_late = max(0, (datetime.now() - due_date).days)
        fee = days_late * LATE_FEE_PER_DAY
        with self.conn:
            self.conn.execute("DELETE FROM borrowings WHERE book_id = ? AND user_name = ?", (book_id, user_name))
            self.conn.execute("UPDATE books SET copies = copies + 1 WHERE book_id = ?", (book_id,))
        return days_late, fee
    def search_books(self, query: str) -> List[Book]:
        pattern = f"%{query}%"
        cursor = self.conn.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (pattern, pattern))
        return [Book(row[0], row[1], row[2], row[3]) for row in cursor.fetchall()]
def main():
    db = LibraryDB()
    print("=" * 50)
    print("     ADVANCED LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)
    while True:
        print("\n1. Add Book\n2. View All Books\n3. Search Books\n4. Issue Book\n5. Return Book\n6. Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            while True:
                try:
                    copies = int(input("Copies: "))
                    if copies <= 0:
                        print("❌ Copies must be a positive whole number.")
                        continue
                    break
                except ValueError:
                    print("❌ Invalid input. Please enter a whole number.")
            book = db.add_book(title, author, copies)
            print(f"✅ Book added with ID: {book.book_id}")
        elif choice == "2":
            books = db.get_all_books()
            for b in books:
                print(f"ID: {b.book_id} | {b.title} by {b.author} | Copies: {b.copies}")
        elif choice == "3":
            query = input("Search title/author: ").strip()
            results = db.search_books(query)
            for b in results:
                print(f"ID: {b.book_id} | {b.title} by {b.author}")
        elif choice == "4":
            try:
                book_id = int(input("Book ID: "))
            except ValueError:
                print("❌ Invalid Book ID.")
                continue
            user = input("Member Name: ").strip()
            try:
                due = db.issue_book(book_id, user)
                print(f"✅ Issued! Due: {due}")
            except ValueError as e:
                print(f"❌ Error: {e}")
        elif choice == "5":
            try:
                book_id = int(input("Book ID: "))
            except ValueError:
                print("❌ Invalid Book ID.")
                continue
            user = input("Member Name: ").strip()
            try:
                days, fee = db.return_book(book_id, user)
                print(f"✅ Returned. Late days: {days} | Fee: ₹{fee:.2f}")
            except ValueError as e:
                print(f"❌ Error: {e}")
        elif choice == "6":
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()
