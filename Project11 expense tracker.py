import json
import os
from datetime import datetime
DATA_FILE = "expenses.json"
CATEGORIES = ["Food", "Transport", "Rent", "Entertainment", "Utilities", "Shopping", "Other"]
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []
def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)
def choose_category():
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}. {cat}")
    while True:
        choice = input("Choose a category number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("Invalid choice.")
def add_expense(expenses):
    amount = get_amount("Enter amount: ")
    category = choose_category()
    note = input("Note (optional): ").strip()
    expense = {
        "id": (max([e["id"] for e in expenses], default=0) + 1),
        "amount": amount,
        "category": category,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d"),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense of {amount} added under '{category}'.")
def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a number.")
def view_all(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n" + "=" * 60)
    print(f"{'ID':<5}{'Date':<12}{'Category':<15}{'Amount':<10}{'Note':<20}")
    print("=" * 60)
    for e in expenses:
        print(f"{e['id']:<5}{e['date']:<12}{e['category']:<15}{e['amount']:<10}{e['note']:<20}")
    print("=" * 60)
def view_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    total = sum(e["amount"] for e in expenses)
    print("\n" + "=" * 40)
    print("          EXPENSE SUMMARY")
    print("=" * 40)
    print(f"Total Spent: {total:.2f}\n")
    print(f"{'Category':<15}{'Amount':<10}{'%':<8}")
    print("-" * 40)
    for cat in CATEGORIES:
        cat_total = sum(e["amount"] for e in expenses if e["category"] == cat)
        if cat_total > 0:
            percentage = (cat_total / total) * 100
            print(f"{cat:<15}{cat_total:<10.2f}{percentage:<8.1f}")
    print("=" * 40)
def delete_expense(expenses):
    expense_id = get_id("Enter expense ID to delete: ")
    for e in expenses:
        if e["id"] == expense_id:
            expenses.remove(e)
            save_expenses(expenses)
            print(f"Expense {expense_id} deleted.")
            return
    print("Expense not found.")
def get_id(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid ID.")
def print_menu():
    print("\n" + "=" * 35)
    print("      PERSONAL EXPENSE TRACKER")
    print("=" * 35)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary by Category")
    print("4. Delete Expense")
    print("5. Exit")
    print("=" * 35)
def main():
    expenses = load_expenses()
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()