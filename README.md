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
| 2 | **Report System**         | A system to generate, manage, and export reports                             |Productivity   |
| 3 | **Guessing Game**         | Interactive number guessing game with scoring and multiple difficulty levels | Game          |
| 4 | **Rock Paper Scissor**    | A CLI Rock Paper Scissors game with score tracking                           | Game          |
| 5 | **Temperature Converter** |A CLI utility that converts temperatures between Celsius, Fahrenheit,                                                                                            and Kelvin with weather condition descriptions                               | Utility       |                                                                                                                              

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
          Adaptive — tracks your move history and counters your most common ch
Possible Future Improvements: Add a "best of N" mode instead of open-ended play
                              Add Rock Paper Scissors Lizard Spock variant
                              Track stats across sessions using a save file

**Quiz Game
A CLI multiple-choice quiz game with score tracking, shuffled questions, and a
results summary that reviews incorrect answers.
quiz_random.py — True random selection (fixed local questions)
Picks each question randomly at the moment it's asked from a slightly
bigger local pool (7 questions), with no repeats within a round.
Features: List of multiple-choice questions (easy to extend, in the local versions)
          Live questions from a huge external question bank (quiz_online.py)
          Category and difficulty selection (quiz_online.py)
          Input validation
          Score tracking and percentage calculation
          End-of-quiz performance message
          Review section showing which questions were missed and the correct answers
          Replay loop
Possible Future Improvements :Load questions from a JSON or CSV file instead of hardcoding
                              Add categories/difficulty levels
                              Add a timer per question
                              Save high scores to a file

**Temperature Converter
A CLI tool to convert between Celsius, Fahrenheit, and Kelvin, with a simple
"weather condition" description based on the temperature.
Features: Convert between all 3 temperature scales (6 conversion directions)
          Input validation (rejects non-numeric input)
          Prevents invalid Kelvin values (below absolute zero)
          Describes the temperature in plain language (Freezing / Cold / Mild / Warm / Hot)
          Menu-driven loop
Possible Future Improvements:Add a real weather API lookup (e.g. OpenWeatherMap) for actual current temperatures
                             Add Rankine scale support
                              Build a small GUI version with Tkinter         








