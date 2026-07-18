import json
import os
DATA_FILE = "inventory.json"
LOW_STOCK_THRESHOLD = 5
class Item:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity
    def sell(self, amount):
        if amount > self.quantity:
            raise ValueError(f"Not enough stock. Only {self.quantity} available.")
        self.quantity -= amount
        return amount * self.price
    def restock(self, amount):
        self.quantity += amount
    def is_low_stock(self):
        return self.quantity <= LOW_STOCK_THRESHOLD
    def to_dict(self):
        return {"item_id": self.item_id, "name": self.name, "price": self.price, "quantity": self.quantity}
    @staticmethod
    def from_dict(data):
        return Item(data["item_id"], data["name"], data["price"], data["quantity"])
class Shop:
    def __init__(self):
        self.items = {}
        self.total_revenue = 0.0
        self.load()
    def load(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
            self.items = {i: Item.from_dict(item_data) for i, item_data in data.get("items", {}).items()}
            self.total_revenue = data.get("total_revenue", 0.0)
    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump({
                "items": {i: item.to_dict() for i, item in self.items.items()},
                "total_revenue": self.total_revenue,
            }, f, indent=2)
    def add_item(self, name, price, quantity):
        item_id = str(len(self.items) + 1)
        item = Item(item_id, name, price, quantity)
        self.items[item_id] = item
        self.save()
        return item
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")
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
def add_item_flow(shop):
    name = input("Enter item name: ").strip()
    price = get_float("Enter item price: ")
    quantity = get_int("Enter initial quantity: ")
    item = shop.add_item(name, price, quantity)
    print(f"Added '{item.name}' (ID: {item.item_id}) with {quantity} units at {price} each.")
def view_inventory(shop):
    if not shop.items:
        print("Inventory is empty.")
        return
    print("\n" + "=" * 55)
    print(f"{'ID':<5}{'Name':<20}{'Price':<10}{'Qty':<8}{'Alert':<10}")
    print("=" * 55)
    for item in shop.items.values():
        alert = "LOW STOCK" if item.is_low_stock() else ""
        print(f"{item.item_id:<5}{item.name:<20}{item.price:<10}{item.quantity:<8}{alert:<10}")
    print("=" * 55)
def sell_item(shop):
    item_id = input("Enter item ID to sell: ").strip()
    item = shop.items.get(item_id)
    if not item:
        print("Item not found.")
        return
    amount = get_int("Enter quantity to sell: ")
    try:
        revenue = item.sell(amount)
        shop.total_revenue += revenue
        shop.save()
        print(f"Sold {amount} x {item.name} for {revenue:.2f}.")
        if item.is_low_stock():
            print(f"⚠ Low stock warning: only {item.quantity} left.")
    except ValueError as e:
        print(f"Error: {e}")
def restock_item(shop):
    item_id = input("Enter item ID to restock: ").strip()
    item = shop.items.get(item_id)
    if not item:
        print("Item not found.")
        return
    amount = get_int("Enter quantity to add: ")
    item.restock(amount)
    shop.save()
    print(f"Restocked '{item.name}'. New quantity: {item.quantity}")
def view_revenue(shop):
    print(f"\nTotal Revenue: {shop.total_revenue:.2f}")
def print_menu():
    print("\n" + "=" * 35)
    print("     SIMPLE INVENTORY / SHOP MGMT")
    print("=" * 35)
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Sell Item")
    print("4. Restock Item")
    print("5. View Total Revenue")
    print("6. Exit")
    print("=" * 35)
def main():
    shop = Shop()
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_item_flow(shop)
        elif choice == "2":
            view_inventory(shop)
        elif choice == "3":
            sell_item(shop)
        elif choice == "4":
            restock_item(shop)
        elif choice == "5":
            view_revenue(shop)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()