# Tic-Tac-Toe

A command-line Tic-Tac-Toe game built in Python for two players sharing the same computer.

## Overview

This project is a simple implementation of the classic 3 × 3 Tic-Tac-Toe game. The program handles the game loop, validates player input, updates the board, and determines whether a player has won or the game has ended in a draw.

I built this project to strengthen my understanding of Python fundamentals, particularly functions, lists, conditional logic, loops, and input validation.

## Features

* 3 × 3 game board
* Two-player gameplay
* Alternating turns between `X` and `O`
* Input validation for invalid positions
* Prevents players from selecting an occupied position
* Automatic win detection
* Draw detection
* Displays the board after each move
* Runs entirely in the terminal

## How It Works

The game follows a simple cycle:

1. Display the current board.
2. Ask the current player for a position.
3. Check whether the input is valid and the position is available.
4. Place the player's mark on the board.
5. Check for a winning combination.
6. If there is no winner, check whether the board is full.
7. Switch players and continue.

Winning positions are checked across the three rows, three columns, and two diagonals of the board.

## Technologies

* **Language:** Python
* **Interface:** Command Line / Terminal
* **Concepts:** Lists, loops, functions, conditionals, input validation, game logic

## Running the Game

Clone the repository:

```bash
git clone https://github.com/your-username/tictactoe.git
cd tictactoe
```

Run the program:

```bash
python tictactoe.py
```

## Example

```text
  1 | 2 | 3
 ---+---+---
  4 | 5 | 6
 ---+---+---
  7 | 8 | 9

Player X, choose a position:
```

Players select positions from `1` to `9` until one player completes a row, column, or diagonal, or the board is filled.

## What I Learned

Building this project helped me practise breaking a larger problem into smaller pieces of logic. In particular, I worked with:

* Representing a board using a Python list
* Designing functions for separate tasks
* Validating user input
* Controlling a repeated game loop
* Checking multiple possible winning conditions
* Managing changing program state between turns

## Future Improvements

Possible extensions include:

* Single-player mode against a computer
* Different board sizes
* A stronger computer opponent using the minimax algorithm
* Score tracking across multiple games
* A graphical interface

## Author

**Abiral**

Built as part of my ongoing journey in Python and computer science.
