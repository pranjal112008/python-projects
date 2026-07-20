import sqlite3
from datetime import datetime
from typing import Optional, List
DB_FILE = "bank.db"
class Account:
    def __init__(self, account_number: str, name: str, pin: str, balance: float = 0.0):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = balance
class Bank:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self.create_tables()
    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS accounts (
                    account_number TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    pin TEXT NOT NULL,
                    balance REAL DEFAULT 0.0
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    account_number TEXT,
                    action TEXT,
                    amount REAL,
                    timestamp TEXT
                )
            ''')
    def log_transaction(self, account_number: str, action: str, amount: float):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with self.conn:
            self.conn.execute(
                "INSERT INTO transactions (account_number, action, amount, timestamp) VALUES (?, ?, ?, ?)",
                (account_number, action, amount, timestamp)
            )
    def create_account(self, name: str, pin: str) -> str:
        if not (pin.isdigit() and len(pin) == 4):
            raise ValueError("PIN must be 4 digits.")
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO accounts (account_number, name, pin, balance) VALUES (NULL, ?, ?, 0.0)",
                (name, pin)
            )
            new_id = cursor.lastrowid
            account_number = f"ACC{1000 + new_id}"
            self.conn.execute(
                "UPDATE accounts SET account_number = ? WHERE rowid = ?",
                (account_number, new_id)
            )
        print(f"✅ Account created successfully! Your Account Number: {account_number}")
        return account_number
    def get_account_count(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM accounts").fetchone()[0]
    def authenticate(self, account_number: str, pin: str) -> Optional[Account]:
        cursor = self.conn.execute(
            "SELECT account_number, name, pin, balance FROM accounts WHERE account_number = ? AND pin = ?", 
            (account_number, pin)
        )
        row = cursor.fetchone()
        if row:
            return Account(row[0], row[1], row[2], row[3])
        return None
    def deposit(self, account: Account, amount: float):
        with self.conn:
            self.conn.execute("UPDATE accounts SET balance = balance + ? WHERE account_number = ?", 
                            (amount, account.account_number))
        account.balance += amount
        self.log_transaction(account.account_number, "DEPOSIT", amount)
        print(f"✅ Deposited ₹{amount:.2f}. New Balance: ₹{account.balance:.2f}")
    def withdraw(self, account: Account, amount: float):
        if amount > account.balance:
            raise ValueError("Insufficient balance!")
        with self.conn:
            self.conn.execute("UPDATE accounts SET balance = balance - ? WHERE account_number = ?", 
                            (amount, account.account_number))
        account.balance -= amount
        self.log_transaction(account.account_number, "WITHDRAW", amount)
        print(f"✅ Withdrew ₹{amount:.2f}. New Balance: ₹{account.balance:.2f}")
    def transfer(self, sender: Account, receiver_number: str, amount: float):
        if amount > sender.balance:
            raise ValueError("Insufficient balance!")
        cursor = self.conn.execute("SELECT * FROM accounts WHERE account_number = ?", (receiver_number,))
        if not cursor.fetchone():
            raise ValueError("Receiver account not found!")
        with self.conn:
            self.conn.execute("UPDATE accounts SET balance = balance - ? WHERE account_number = ?", 
                            (amount, sender.account_number))
            self.conn.execute("UPDATE accounts SET balance = balance + ? WHERE account_number = ?", 
                            (amount, receiver_number))
            sender.balance -= amount
        self.log_transaction(sender.account_number, f"TRANSFER TO {receiver_number}", amount)
        self.log_transaction(receiver_number, f"RECEIVED FROM {sender.account_number}", amount)
        print(f"✅ Transferred ₹{amount:.2f} to {receiver_number}")
    def get_history(self, account_number: str) -> List[tuple]:
        cursor = self.conn.execute(
            "SELECT action, amount, timestamp FROM transactions WHERE account_number = ? ORDER BY id DESC", 
            (account_number,)
        )
        return cursor.fetchall()
def get_amount(prompt: str) -> float:
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a number.")
def main():
    bank = Bank()
    print("=" * 50)
    print("       IMPROVED ATM / BANK SYSTEM")
    print("=" * 50)
    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            name = input("Enter your name: ").strip()
            pin = input("Set 4-digit PIN: ").strip()
            try:
                bank.create_account(name, pin)
            except ValueError as e:
                print(e)
        elif choice == "2":
            acc_num = input("Enter account number: ").strip()
            pin = input("Enter PIN: ").strip()
            account = bank.authenticate(acc_num, pin)
            if not account:
                print("❌ Invalid credentials!")
                continue
            print(f"\nWelcome, {account.name}!")
            while True:
                print("\n1. Balance  2. Deposit  3. Withdraw  4. Transfer  5. History  6. Logout")
                op = input("Choose: ").strip()
                if op == "1":
                    print(f"Balance: ₹{account.balance:.2f}")
                elif op == "2":
                    amt = get_amount("Deposit amount: ")
                    bank.deposit(account, amt)
                elif op == "3":
                    amt = get_amount("Withdraw amount: ")
                    try:
                        bank.withdraw(account, amt)
                    except ValueError as e:
                        print(e)
                elif op == "4":
                    rec = input("Receiver Account Number: ").strip()
                    amt = get_amount("Transfer amount: ")
                    try:
                        bank.transfer(account, rec, amt)
                    except ValueError as e:
                        print(e)
                elif op == "5":
                    history = bank.get_history(account.account_number)
                    for act, amt, ts in history[:5]:
                        print(f"{ts} | {act} | ₹{amt}")
                elif op == "6":
                    print("Logged out.")
                    break
        elif choice == "3":
            print("Thank you for using Improved ATM!")
            break
if __name__ == "__main__":
    main()
