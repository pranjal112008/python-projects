import json
import os
from datetime import datetime
DATA_FILE = "todos.json"
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
def add_task(tasks):
    description = input("Enter task description: ").strip()
    if not description:
        print("Task description cannot be empty.")
        return
    priority = input("Priority (low/medium/high, default medium): ").strip().lower()
    if priority not in ["low", "medium", "high"]:
        priority = "medium"
    task = {
        "id": (max([t["id"] for t in tasks], default=0) + 1),
        "description": description,
        "priority": priority,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added with ID {task['id']}.")
def view_tasks(tasks, show_completed=True):
    if not tasks:
        print("No tasks yet.")
        return
    visible = tasks if show_completed else [t for t in tasks if not t["done"]]
    if not visible:
        print("No pending tasks.")
        return
    print("\n" + "=" * 60)
    print(f"{'ID':<5}{'Status':<10}{'Priority':<10}{'Description':<35}")
    print("=" * 60)
    for t in visible:
        status = "Done" if t["done"] else "Pending"
        print(f"{t['id']:<5}{status:<10}{t['priority']:<10}{t['description']:<35}")
    print("=" * 60)
def complete_task(tasks):
    task_id = get_task_id("Enter task ID to mark as complete: ")
    task = find_task(tasks, task_id)
    if task:
        task["done"] = True
        save_tasks(tasks)
        print(f"Task {task_id} marked as complete.")
    else:
        print("Task not found.")
def delete_task(tasks):
    task_id = get_task_id("Enter task ID to delete: ")
    task = find_task(tasks, task_id)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task {task_id} deleted.")
    else:
        print("Task not found.")
def find_task(tasks, task_id):
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None
def get_task_id(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")
def print_menu():
    print("\n" + "=" * 35)
    print("        TODO LIST MANAGER")
    print("=" * 35)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks Only")
    print("4. Mark Task as Complete")
    print("5. Delete Task")
    print("6. Exit")
    print("=" * 35)
def main():
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks, show_completed=True)
        elif choice == "3":
            view_tasks(tasks, show_completed=False)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()