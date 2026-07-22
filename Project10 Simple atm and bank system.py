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
    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient balance!")
        self.balance -= amount
    def account_type(self) -> str:
        return "standard"
    def __str__(self):
        return f"[{self.account_type().title()}] {self.name} ({self.account_number}) - ₹{self.balance:.2f}"
class SavingsAccount(Account):
    def __init__(self, account_number, name, pin, balance=0.0, interest_rate=0.04):
        super().__init__(account_number, name, pin, balance)
        self.interest_rate = interest_rate
    def apply_interest(self) -> float:
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest
    def account_type(self) -> str:
        return "savings"
class CurrentAccount(Account):
    def __init__(self, account_number, name, pin, balance=0.0, overdraft_limit=5000.0):
        super().__init__(account_number, name, pin, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount: float):
        available = self.balance + self.overdraft_limit
        if amount > available:
    raise ValueError(f"Exceeds overdraft limit! Available: ₹{available:.2f}")
        self.balance -= amount
    def account_type(self) -> str:
        return "current"
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
                    balance REAL DEFAULT 0.0,
                    account_type TEXT DEFAULT 'standard'
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
    def create_account(self, name: str, pin: str, account_type: str) -> str:
        if not (pin.isdigit() and len(pin) == 4):
            raise ValueError("PIN must be 4 digits.")
        if account_type not in ("savings", "current", "standard"):
            raise ValueError(f"Unknown account type: {account_type}")
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO accounts (account_number, name, pin, balance, account_type) VALUES (NULL, ?, ?, 0.0, ?)",
                (name, pin, account_type)
            )
            new_id = cursor.lastrowid
            account_number = f"ACC{1000 + new_id}"
            self.conn.execute(
                "UPDATE accounts SET account_number = ? WHERE rowid = ?",
                (account_number, new_id)
            )
        print(f"✅ {account_type.title()} account created! Your Account Number: {account_number}")
        return account_number
    def _row_to_account(self, row) -> Account:
        account_number, name, pin, balance, account_type = row
        if account_type == "savings":
            return SavingsAccount(account_number, name, pin, balance)
        elif account_type == "current":
            return CurrentAccount(account_number, name, pin, balance)
        return Account(account_number, name, pin, balance)
   def authenticate(self, account_number: str, pin: str) -> Optional[Account]:
        cursor = self.conn.execute(
            "SELECT account_number, name, pin, balance, account_type FROM accounts WHERE account_number = ? AND pin = ?",
            (account_number, pin)
        )
        row = cursor.fetchone()
        return self._row_to_account(row) if row else None
    def deposit(self, account: Account, amount: float):
        account.balance += amount  # same call for every account type
        with self.conn:
            self.conn.execute("UPDATE accounts SET balance = balance + ? WHERE account_number = ?",
                            (amount, account.account_number))
        self.log_transaction(account.account_number, "DEPOSIT", amount)
        print(f"✅ Deposited ₹{amount:.2f}. New Balance: ₹{account.balance:.2f}")
    def withdraw(self, account: Account, amount: float):
       account.withdraw(amount)
        with self.conn:
            self.conn.execute("UPDATE accounts SET balance = ? WHERE account_number = ?",
                            (account.balance, account.account_number))
        self.log_transaction(account.account_number, "WITHDRAW", amount)
        print(f"✅ Withdrew ₹{amount:.2f}. New Balance: ₹{account.balance:.2f}")
    def apply_interest(self, account: SavingsAccount) -> float:
        if not isinstance(account, SavingsAccount):
            raise ValueError("Interest can only be applied to Savings accounts.")
        interest = account.apply_interest()
        with self.conn:
            self.conn.execute("UPDATE accounts SET balance = ? WHERE account_number = ?",
                            (account.balance, account.account_number))
        self.log_transaction(account.account_number, "INTEREST", interest)
        print(f"✅ Interest applied: ₹{interest:.2f}. New Balance: ₹{account.balance:.2f}")
        return interest
    def transfer(self, sender: Account, receiver_number: str, amount: float):
        cursor = self.conn.execute(
            "SELECT account_number, name, pin, balance, account_type FROM accounts WHERE account_number = ?",
            (receiver_number,)
        )
        row = cursor.fetchone()
        if not row:
            raise ValueError("Receiver account not found!")
        receiver = self._row_to_account(row)
        sender.withdraw(amount)  
        receiver.balance += amount
        with self.conn:
            self.conn.execute("UPDATE accounts SET balance = ? WHERE account_number = ?",
                            (sender.balance, sender.account_number))
            self.conn.execute("UPDATE accounts SET balance = ? WHERE account_number = ?",
                            (receiver.balance, receiver.account_number))
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
def choose_account_type() -> str:
    print("\n1. Savings (earns interest)\n2. Current (has overdraft)")
    choice = input("Choose account type: ").strip()
    return "savings" if choice == "1" else "current"
def main():
    bank = Bank()
    print("=" * 50)
    print("     ATM / BANK SYSTEM (with Inheritance)")
    print("=" * 50)
    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            name = input("Enter your name: ").strip()
            pin = input("Set 4-digit PIN: ").strip()
            acc_type = choose_account_type()
            try:
                bank.create_account(name, pin, acc_type)
            except ValueError as e:
                print(f"❌ {e}")
        elif choice == "2":
            acc_num = input("Enter account number: ").strip()
            pin = input("Enter PIN: ").strip()
            account = bank.authenticate(acc_num, pin)
            if not account:
                print("❌ Invalid credentials!")
                continue
            print(f"\nWelcome, {account.name}! ({account})")
            is_savings = isinstance(account, SavingsAccount)
            menu = "\n1. Balance  2. Deposit  3. Withdraw  4. Transfer  5. History  6. Logout"
            if is_savings:
                menu = "\n1. Balance  2. Deposit  3. Withdraw  4. Transfer  5. History  6. Apply Interest  7. Logout"
            print(menu)
            while True:
                op = input("Choose: ").strip()
                if op == "1":
                    print(f"Balance: ₹{account.balance:.2f}")
                elif op == "2":
                    bank.deposit(account, get_amount("Deposit amount: "))
                elif op == "3":
                    try:
                        bank.withdraw(account, get_amount("Withdraw amount: "))
                    except ValueError as e:
                        print(f"❌ {e}")
                elif op == "4":
                    rec = input("Receiver Account Number: ").strip()
                    amt = get_amount("Transfer amount: ")
                    try:
                        bank.transfer(account, rec, amt)
                    except ValueError as e:
                        print(f"❌ {e}")
                elif op == "5":
                    for act, amt, ts in bank.get_history(account.account_number)[:5]:
                        print(f"{ts} | {act} | ₹{amt}")
                elif op == "6" and is_savings:
                    bank.apply_interest(account)
                elif (op == "6" and not is_savings) or (op == "7" and is_savings):
                    print("Logged out.")
                    break
                else:
                    print("Invalid option.")
                    print(menu)
                    continue
                print(menu)
        elif choice == "3":
            print("Thank you for using the ATM!")
            break
if __name__ == "__main__":
    main()
