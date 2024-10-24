# PRODIGY_SD_04


# Sudoku Solver

This is a Python program that solves Sudoku puzzles using the backtracking algorithm. The program takes an input grid representing an unsolved Sudoku puzzle and fills in the missing numbers to solve the puzzle.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automatically solves any valid 9x9 Sudoku puzzle.
- Uses backtracking to explore all possible solutions efficiently.
- Provides a clear output of the solved puzzle.
- Simple command-line interface.

## Technologies Used

- Python 3.x

## Usage

Clone the repository and run the Python script with an input Sudoku grid to solve the puzzle.


### Input Options

- The program expects a 9x9 grid with empty spaces represented by `0`.

### Sample Input Format

You can define the unsolved Sudoku puzzle directly in the Python script as a 2D list (9x9 grid):

unsolved_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

## How It Works

1. The program uses **backtracking** to solve the puzzle.
2. It checks if a number can be placed in an empty cell by validating the row, column, and 3x3 sub-grid.
3. If a valid number is found, it is placed in the cell and the program recursively tries to solve the rest of the board.
4. If a mistake is made, the program backtracks by resetting the cell and trying another number.

## Example


Initial Sudoku puzzle:
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9

Solved Sudoku puzzle:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
