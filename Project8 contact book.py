import json
import os
import re
DATA_FILE = "contacts.json"

# Matches phone numbers like "9876543210", "987-654-3210", "+91 9876543210"
PHONE_PATTERN = re.compile(r"^\+?[\d\s\-]{7,15}$")
# Standard email shape: local-part@domain.tld (supports multi-level domains like mail.example.co)
EMAIL_PATTERN = re.compile(r"^[\w\.\-]+@[\w\-]+(\.[\w\-]+)*\.[A-Za-z]{2,}$")

def get_valid_phone(prompt):
    while True:
        phone = input(prompt).strip()
        if PHONE_PATTERN.match(phone):
            return phone
        print("Invalid phone number. Use digits, spaces, or hyphens (7-15 digits), optionally starting with '+'.")

def get_valid_email(prompt, allow_blank=False):
    while True:
        email = input(prompt).strip()
        if allow_blank and not email:
            return email
        if EMAIL_PATTERN.match(email):
            return email
        print("Invalid email format. Expected something like name@example.com.")
def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}
def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=2)
def add_contact(contacts):
    name = input("Enter name: ").strip()
    if name in contacts:
        print("A contact with this name already exists. Use update instead.")
        return
    phone = get_valid_phone("Enter phone number: ")
    email = get_valid_email("Enter email (optional, press Enter to skip): ", allow_blank=True)
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' added.")
def view_all(contacts):
    if not contacts:
        print("No contacts saved yet.")
        return
    print("\n" + "=" * 50)
    print(f"{'Name':<20}{'Phone':<15}{'Email':<15}")
    print("=" * 50)
    for name, info in sorted(contacts.items()):
        print(f"{name:<20}{info['phone']:<15}{info['email']:<15}")
    print("=" * 50)
def search_contact(contacts):
    query = input("Enter name to search: ").strip().lower()
    matches = {n: info for n, info in contacts.items() if query in n.lower()}
    if not matches:
        print("No matching contacts found.")
        return
    for name, info in matches.items():
        print(f"Name: {name} | Phone: {info['phone']} | Email: {info['email']}")
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    while True:
        phone = input(f"New phone (leave blank to keep '{contacts[name]['phone']}'): ").strip()
        if not phone or PHONE_PATTERN.match(phone):
            break
        print("Invalid phone number. Use digits, spaces, or hyphens (7-15 digits), optionally starting with '+'.")
    while True:
        email = input(f"New email (leave blank to keep '{contacts[name]['email']}'): ").strip()
        if not email or EMAIL_PATTERN.match(email):
            break
        print("Invalid email format. Expected something like name@example.com.")
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    save_contacts(contacts)
    print(f"Contact '{name}' updated.")
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
    if confirm == "y":
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted.")
def print_menu():
    print("\n" + "=" * 35)
    print("          CONTACT BOOK")
    print("=" * 35)
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("=" * 35)
def main():
    contacts = load_contacts()
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_all(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
