import json
import os
from datetime import datetime, timedelta
DATA_FILE = "library.json"
LOAN_DAYS = 14
LATE_FEE_PER_DAY = 2.0
class Book:
    def __init__(self, book_id, title, author, copies, borrowed_by=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed_by = borrowed_by if borrowed_by is not None else {}
    def available_copies(self):
        return self.copies - len(self.borrowed_by)
    def to_dict(self):
        return {
            "book_id": self.book_id, "title": self.title, "author": self.author,
            "copies": self.copies, "borrowed_by": self.borrowed_by,
        }
    @staticmethod
    def from_dict(data):
        return Book(data["book_id"], data["title"], data["author"], data["copies"], data["borrowed_by"])
class Library:
    def __init__(self):
        self.books = {}
        self.load()
    def load(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
            self.books = {i: Book.from_dict(b) for i, b in data.items()}
    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump({i: b.to_dict() for i, b in self.books.items()}, f, indent=2)
    def add_book(self, title, author, copies):
        book_id = str(len(self.books) + 1)
        book = Book(book_id, title, author, copies)
        self.books[book_id] = book
        self.save()
        return book
    def issue_book(self, book_id, member_name):
        book = self.books.get(book_id)
        if not book:
            raise ValueError("Book not found.")
        if member_name in book.borrowed_by:
            raise ValueError(f"{member_name} has already borrowed this book.")
        if book.available_copies() <= 0:
            raise ValueError("No copies available.")
        due_date = (datetime.now() + timedelta(days=LOAN_DAYS)).strftime("%Y-%m-%d")
        book.borrowed_by[member_name] = due_date
        self.save()
        return due_date
    def return_book(self, book_id, member_name):
        book = self.books.get(book_id)
        if not book:
            raise ValueError("Book not found.")
        if member_name not in book.borrowed_by:
            raise ValueError(f"No record of {member_name} borrowing this book.")
        due_date_str = book.borrowed_by[member_name]
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        days_late = max(0, (datetime.now() - due_date).days)
        fee = days_late * LATE_FEE_PER_DAY
        del book.borrowed_by[member_name]
        self.save()
        return days_late, fee
def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")
def add_book_flow(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    copies = get_int("Enter number of copies: ")
    book = library.add_book(title, author, copies)
    print(f"Added '{book.title}' (ID: {book.book_id}) with {copies} copies.")
def view_books(library):
    if not library.books:
        print("No books in the library yet.")
        return
    print("\n" + "=" * 65)
    print(f"{'ID':<5}{'Title':<25}{'Author':<20}{'Available':<10}")
    print("=" * 65)
    for book in library.books.values():
        print(f"{book.book_id:<5}{book.title:<25}{book.author:<20}{book.available_copies():<10}")
    print("=" * 65)
def issue_book_flow(library):
    book_id = input("Enter book ID: ").strip()
    member_name = input("Enter member name: ").strip()
    try:
        due_date = library.issue_book(book_id, member_name)
        print(f"Book issued to {member_name}. Due date: {due_date}")
    except ValueError as e:
        print(f"Error: {e}")
def return_book_flow(library):
    book_id = input("Enter book ID: ").strip()
    member_name = input("Enter member name: ").strip()
    try:
        days_late, fee = library.return_book(book_id, member_name)
        if days_late > 0:
            print(f"Book returned {days_late} day(s) late. Late fee: {fee:.2f}")
        else:
            print("Book returned on time. No late fee.")
    except ValueError as e:
        print(f"Error: {e}")
def view_borrowed(library):
    found = False
    print("\nCurrently Borrowed Books:")
    for book in library.books.values():
        for member, due_date in book.borrowed_by.items():
            found = True
            print(f" - '{book.title}' borrowed by {member}, due {due_date}")
    if not found:
        print("No books currently borrowed.")
def print_menu():
    print("\n" + "=" * 35)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("=" * 35)
    print("1. Add Book")
    print("2. View All Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View Borrowed Books")
    print("6. Exit")
    print("=" * 35)
def main():
    library = Library()
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_book_flow(library)
        elif choice == "2":
            view_books(library)
        elif choice == "3":
            issue_book_flow(library)
        elif choice == "4":
            return_book_flow(library)
        elif choice == "5":
            view_borrowed(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()