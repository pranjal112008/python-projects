import csv
import os
DATA_FILE = "students.csv"
def load_students():
    """Load students from CSV file if it exists."""
    students = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["marks"] = float(row["marks"])
                students.append(row)
    return students
def save_students(students):
    """Save all students to CSV file."""
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "marks", "grade"])
        writer.writeheader()
        writer.writerows(students)
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"
def add_student(students):
    name = input("Enter student name: ").strip()
    while True:
        try:
            marks = float(input(f"Enter marks for {name}: "))
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    grade = get_grade(marks)
    students.append({"name": name, "marks": marks, "grade": grade})
    save_students(students)
    print(f"Added {name} with marks {marks} (Grade: {grade})")
def view_all(students):
    if not students:
        print("No students recorded yet.")
        return
    print("\n" + "=" * 45)
    print(f"{'Name':<20}{'Marks':<10}{'Grade':<10}")
    print("=" * 45)
    for s in students:
        print(f"{s['name']:<20}{s['marks']:<10}{s['grade']:<10}")
    print("=" * 45)
def search_student(students):
    name = input("Enter name to search: ").strip().lower()
    matches = [s for s in students if s["name"].lower() == name]
    if not matches:
        print("No student found with that name.")
        return
    for s in matches:
        print(f"Name: {s['name']} | Marks: {s['marks']} | Grade: {s['grade']}")
def class_summary(students):
    if not students:
        print("No students recorded yet.")
        return
    marks_list = [s["marks"] for s in students]
    total = sum(marks_list)
    average = total / len(marks_list)
    highest = max(students, key=lambda s: s["marks"])
    lowest = min(students, key=lambda s: s["marks"])
    passed = sum(1 for s in students if s["marks"] >= 40)
    failed = len(students) - passed
    print("\n" + "=" * 40)
    print("          CLASS SUMMARY REPORT")
    print("=" * 40)
    print(f"Total Students   : {len(students)}")
    print(f"Average Marks    : {average:.2f}")
    print(f"Highest          : {highest['name']} ({highest['marks']})")
    print(f"Lowest           : {lowest['name']} ({lowest['marks']})")
    print(f"Passed           : {passed}")
    print(f"Failed           : {failed}")
    print("=" * 40)
def print_menu():
    print("\n" + "=" * 40)
    print("     STUDENT REPORT CARD SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. Class Summary Report")
    print("5. Exit")
    print("=" * 40)
def main():
    students = load_students()
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            class_summary(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()