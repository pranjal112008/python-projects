# python-projects
A collection of Python projects, scripts, and practice exercises for learning and building real-world applications.
# python-projects
A collection of Python projects, scripts, and practice exercises for learning and building real-world applications.

# Python Projects
A collection of practical Python projects for learning, skill-building, and fun.

## About

This repository contains various Python projects ranging from beginner-friendly games to useful tools. It was created to organize and showcase my Python development journey. 


## Projects

| # | Project Name              | Description                                                                  | Type          |
|---|---------------------------|------------------------------------------------------------------------------|---------------|
| 1 | **CLI Calculator**        | A command-line calculator supporting basic and advanced operations           | Utility       |
| 2 | **Report System**         | A system to generate, manage, and export reports                             | Productivity  |
| 3 | **Guessing Game**         | Interactive number guessing game with scoring and multiple difficulty levels | Game          |
| 4 | **Rock Paper Scissor**    | A CLI Rock Paper Scissors game with score tracking                           | Game          |


**CLI Calculator
A simple, robust command-line calculator built in Python.
Features : Basic operations: Add, Subtract, Multiply, Divide
          Extended operations: Modulo, Power, Square Root
          Input validation (no crashes on bad input)
          Handles division/modulo by zero gracefully
          Loops until the user chooses to exit
          Clean, function-based design
Possible Future Improvements :Add a GUI using Tkinter
                              Add calculation history/log to a file
                              Support chained calculations (e.g. 5 + 3 * 2)

**Student Report Card System
A CLI-based student record manager that stores data persistently in a CSV file.
Features: Add students with name and marks
          Auto-assigns letter grade (A/B/C/D/F)
          View all students in a formatted table
          Search for a student by name
          Generate a class summary report (average, highest, lowest, pass/fail count)
          Data persists across runs using students.csv
Possible Future Improvements: Add subject-wise marks instead of a single score
                              Add edit/delete student functionality
                              Export report as PDF

**Number Guessing Game
A CLI number guessing game with difficulty levels, limited attempts, and score tracking.
Features: Three difficulty levels (Easy / Medium / Hard) with different ranges and attempt limits
          Higher/lower hints after each guess
          Score tracking across multiple rounds
          Input validation
          Play again loop
Possible Future Improvements: Add a timer-based challenge mode
                              Track best scores in a leaderboard file
                              Add a GUI version using Tkinter or Pygame
                           
**Rock Paper Scissors game
A CLI Rock Paper Scissors game with score tracking, a replay loop, and an optional
"adaptive" computer opponent that tries to counter your most frequent move.
Features : Accepts full words or short forms (r/p/s)
          Score tracking across rounds (wins, losses, ties)
          Replay loop until you choose to stop
          Two computer difficulty modes:
          Random — fair, unpredictable
          Adaptive — tracks your move history and counters your most common choice

                              Add a simple GUI (Tkinter) or web version (Flask)

