# Python Projects

A collection of practical Python projects for learning, skill-building, and showcasing real-world CLI applications — spanning simple utilities to OOP-based systems with persistent storage.

## About

This repository documents my Python development journey, from foundational scripts to fully structured, portfolio-ready projects. Each project lives in its own subfolder, is self-contained, and includes input validation, error handling, and (where relevant) persistent data storage.

## Project Index

| # | Project                                                            | Description                                                | Type         | Storage |
|---|--------------------------------------------------------------------|------------------------------------------------------------|--------------|---------|
| 1 | [CLI Calculator](#1-cli-calculator)                                | Command-line calculator with basic and advanced operations | Utility      | —       |
| 2 | [Student Report Card System](#2-student-report-card-system)        | Manages student records, grades, and class summaries       | Productivity | CSV     |
| 3 | [Number Guessing Game](#3-number-guessing-game)                    | Guessing game with difficulty levels and scoring           | Game         | —       |
| 4 | [Rock Paper Scissors](#4-rock-paper-scissors)                      | RPS with score tracking and an adaptive AI opponent        | Game         | —       |
| 5 | [Quiz Game](#5-quiz-game)                                          | Multiple-choice general knowledge quiz                     | Game         | —       |
| 6 | [Temperature Converter](#6-temperature-converter)                  | Converts between Celsius, Fahrenheit, and Kelvin           | Utility      | —       |
| 7 | [Password Generator](#7-password-generator)                        | Generates secure, customizable random passwords            | Utility      | —       |
| 8 | [Contact Book](#8-contact-book)                                    | Stores, searches, updates, and deletes contacts            | Productivity | JSON    |
| 9 | [Todo List Manager](#9-todo-list-manager)                          | Task manager with priorities and completion tracking       | Productivity | JSON    |
| 10 | [Simple ATM / Bank System](#10-simple-atm--bank-system)           | OOP banking simulator with inheritance, PIN auth, transfers | Productivity | SQLite  |
| 11 | [Personal Expense Tracker](#11-personal-expense-tracker)          | Logs, categorizes, and summarizes expenses                 | Productivity | JSON    |
| 12 | [Simple Inventory / Shop Management](#12-simple-inventory--shop-management) | Tracks stock, sales, restocking, and revenue     | Productivity | JSON    |
| 13 | [Library Management System](#13-library-management-system)        | Tracks books, issues/returns, due dates, and late fees     | Productivity | SQLite  |
| 14 | [Word Frequency Counter](#14-word-frequency-counter)               | Analyzes text and ranks word frequency, with stopword filtering | Utility  | —       |

---

### 1. CLI Calculator
A simple, robust command-line calculator.

**Features**
- Basic operations: Add, Subtract, Multiply, Divide
- Extended operations: Modulo, Power, Square Root
- Input validation — no crashes on bad input
- Graceful handling of division/modulo by zero
- Loops until the user chooses to exit

**Possible future improvements**
- GUI version using Tkinter
- Calculation history/log saved to a file
- Support for chained calculations (e.g. `5 + 3 * 2`)

### 2. Student Report Card System
A CLI-based student record manager with persistent storage in a CSV file.

**Features**
- Add students with name and marks
- Auto-assigns letter grade (A/B/C/D/F)
- View all students in a formatted table
- Search for a student by name
- Class summary report (average, highest, lowest, pass/fail count)
- Data persists across runs in `students.csv`

**Possible future improvements**
- Subject-wise marks instead of a single score
- Edit/delete student functionality
- Export report as PDF

### 3. Number Guessing Game
A CLI guessing game with difficulty levels, limited attempts, and score tracking.

**Features**
- Three difficulty levels (Easy / Medium / Hard) with different ranges and attempt limits
- Higher/lower hints after each guess
- Score tracking across multiple rounds
- Input validation and a replay loop

**Possible future improvements**
- Timer-based challenge mode
- Leaderboard saved to a file
- GUI version using Tkinter or Pygame

### 4. Rock Paper Scissors
A CLI Rock Paper Scissors game with score tracking, a replay loop, and an optional adaptive computer opponent.

**Features**
- Accepts full words or short forms (`r`/`p`/`s`)
- Score tracking across rounds (wins, losses, ties)
- Two computer difficulty modes:
  - **Random** — fair, unpredictable
  - **Adaptive** — tracks your move history and counters your most common choice
- Replay loop until you choose to stop

**Possible future improvements**
- "Best of N" mode instead of open-ended play
- Rock Paper Scissors Lizard Spock variant
- Session stats saved to a file

### 5. Quiz Game
A CLI multiple-choice quiz with score tracking, shuffled questions, and a results summary reviewing incorrect answers. Includes a variant that pulls live questions from the Open Trivia Database API.

**Features**
- Local question pool with no repeats within a round
- Optional live-question mode via the Open Trivia Database API (category/difficulty selection)
- Input validation
- Score tracking and percentage calculation
- End-of-quiz performance message
- Review section showing missed questions and correct answers
- Replay loop

**Possible future improvements**
- Load questions from a JSON or CSV file instead of hardcoding
- Timer per question
- Save high scores to a file

### 6. Temperature Converter
A CLI tool to convert between Celsius, Fahrenheit, and Kelvin, with a plain-language description of the temperature.

**Features**
- Convert between all 3 scales (6 conversion directions)
- Input validation (rejects non-numeric input)
- Prevents invalid Kelvin values (below absolute zero)
- Describes the temperature in plain language (Freezing / Cold / Mild / Warm / Hot)
- Menu-driven loop

**Possible future improvements**
- Real weather API lookup (e.g. OpenWeatherMap) for current temperatures
- Rankine scale support
- Small GUI version with Tkinter

### 7. Password Generator
A CLI tool that generates secure, customizable random passwords using `random` and `string`.

**Features**
- Customizable password length
- Choose character types to include: uppercase, lowercase, digits, symbols
- Guarantees at least one character from each selected type
- Password strength rating (Weak / Moderate / Strong / Very Strong)
- Input validation throughout
- Generate multiple passwords in one session

**Possible future improvements**
- "Password Manager" mode: save generated passwords (encrypted) to a local file
- Strength checker for user-entered passwords, not just generated ones
- Option to exclude ambiguous characters (e.g. `l`, `1`, `O`, `0`)

### 8. Contact Book
A CLI contact manager with persistent storage in JSON.

**Features**
- Add contacts (name, phone, email)
- View all contacts, sorted alphabetically
- Search contacts by partial name match
- Update phone/email for an existing contact
- Delete a contact (with confirmation)
- Data persists in `contacts.json`

**Possible future improvements**
- Contact groups/categories
- Multiple phone numbers per contact
- Export contacts to CSV
- Simple GUI with Tkinter

### 9. Todo List Manager
A CLI task manager with priorities, completion tracking, and persistent storage in JSON.

**Features**
- Add tasks with a priority level (low/medium/high)
- Auto-incrementing task IDs
- View all tasks or only pending ones
- Mark tasks as complete
- Delete tasks
- Timestamps each task with its creation date/time
- Data persists in `todos.json`

**Possible future improvements**
- Due dates with sorting by urgency
- Task categories/tags
- Editing of existing tasks
- GUI or web version

### 10. Simple ATM / Bank System
An object-oriented CLI banking simulator with PIN-protected accounts, deposits, withdrawals, and transfers between accounts, backed by a **SQLite** database. Built around an `Account` base class with `SavingsAccount` and `CurrentAccount` subclasses, demonstrating inheritance and polymorphism.

**Features**
- Create an account as either **Savings** (earns interest) or **Current** (has an overdraft limit)
- Auto-generated, collision-safe account numbers
- Login with account number + PIN authentication
- Deposit and withdraw funds — withdrawal rules differ by account type (standard balance check for Savings, overdraft allowance for Current) via polymorphic `withdraw()` overriding
- Apply interest to Savings accounts on demand
- Transfer funds between two accounts (respects each account type's own withdrawal rules)
- Full transaction history log per account, with timestamps
- Data persists in `bank.db` (SQLite), including account type per row

**Possible future improvements**
- PIN change functionality
- Minimum balance requirements
- Hash/encrypt PINs instead of storing them in plain text (essential for any real system)
- Abstract base class (`ABC`) for `Account` to enforce subclasses implement required methods

### 11. Personal Expense Tracker
A CLI tool to log, categorize, and analyze personal expenses, with persistent storage in JSON.

**Features**
- Add expenses with amount, category, note, and auto-recorded date
- Predefined categories (Food, Transport, Rent, Entertainment, Utilities, Shopping, Other)
- View all expenses in a table
- Category-wise summary with percentage breakdown
- Delete an expense by ID
- Data persists in `expenses.json`

**Possible future improvements**
- Monthly/weekly filtering and reports
- Budget limit per category with warnings
- Export to CSV for use in Excel/Sheets
- Spending visualizations (bar chart by category) using matplotlib

### 12. Simple Inventory / Shop Management
An object-oriented CLI system for managing a shop's inventory, with persistent storage in JSON.

**Features**
- Add items with name, price, and quantity
- Auto-generated item IDs
- Sell items (reduces stock, adds to revenue, checks for sufficient stock)
- Restock items
- Low-stock alerts (flagged when quantity ≤ 5)
- Track total revenue across all sales
- Data persists in `inventory.json`

**Possible future improvements**
- Item categories
- Supplier/purchase cost tracking (to calculate profit, not just revenue)
- Sales history log with timestamps
- Barcode/SKU lookup

### 13. Library Management System
An object-oriented CLI system to manage a library's books and lending, backed by a **SQLite** database.

**Features**
- Add books with title, author, and number of copies
- Issue books to members (tracks who has what, and the due date)
- Prevents issuing when no copies are available
- Return books with automatic late fee calculation (based on days overdue)
- Search books by title/author
- View all books with live availability count
- Data persists in `library.db` (SQLite)

**Possible future improvements**
- Separate `Member` class with borrowing limits and history
- Reservation queue for fully-borrowed books
- Reminders for books nearing their due date

### 14. Word Frequency Counter
A CLI text analysis tool that counts and ranks how often each word appears in a block of text, with optional stopword filtering.

**Features**
- Case-insensitive word counting with punctuation stripped
- Ranks words by frequency, most common first
- Stopword filtering using a set (removes common words like "the", "is", "and" so results highlight meaningful terms)
- Reports the single most common word
- Menu-driven, matches the structure of the other CLI tools in this repo

**Possible future improvements**
- Load text from a `.txt` file instead of manual input
- Configurable/editable stopword list
- Word cloud visualization
- Support for analyzing multiple files and comparing frequency across them

---

## Repository Structure

```
python-projects/
├── Project1_CLI_Calculator/
├── Project2_Report_System/
├── Project3_Number_Guessing_Game/
├── Project4_Rock_Paper_Scissors/
├── Project5_Quiz_Game/
├── Project6_Temperature_Converter/
├── Project7_Password_Generator/
├── Project8_Contact_Book/
├── Project9_Todo_List/
├── Project10_Simple_ATM/
├── Project11_Expense_Tracker/
├── Project12_Simple_Inventory/
├── Project13_Library_Management/
├── Project14_Word_Frequency_Counter/
└── README.md
```

Each subfolder contains the project's script(s), and larger projects (Math Utils Toolkit, multi-file OOP systems) separate logic, CLI, and tests where applicable.

## Tools & Technologies

- Python 3
- Visual Studio Code
- Git & GitHub
- SQLite3 (for ATM and Library systems)
- `requests` (for the live Quiz Game API mode)

## Progress

This repository is updated continuously as new topics are learned and new projects are completed — progressing from single-file scripts toward multi-file, OOP-based systems.

## Author

**Pranjal Jhariya**
