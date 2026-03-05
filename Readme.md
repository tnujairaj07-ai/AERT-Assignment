# AERT – Algorithmic Efficiency & Recursion Toolkit

This project is my Unit 1 assignment for the Data Structures course.  
The goal is to practice recursion, basic algorithm analysis, and the idea of ADTs using Python.

## Files in this project

- `aert_toolkit.py` – main Python file with all the code.
- `report.pdf` – short report explaining time/space complexity and paradigms.
- `output.txt` – console output for all required test cases.

## Features implemented

1. **Stack ADT**
   - Implemented a simple `StackADT` class with:
     - `push(x)`
     - `pop()`
     - `peek()`
     - `is_empty()`
     - `size()`
   - The stack is used to store mid indices visited during recursive binary search.

2. **Factorial (Recursive)**
   - Function `factorial(n)` for `n >= 0`.
   - Uses a base case `n == 0` and a recursive case `n * factorial(n-1)`.
   - Handles negative input by returning `None`.

3. **Fibonacci (Naive and Memoized)**
   - `fib_naive(n)` – simple recursive version.
   - `fib_memo(n)` – recursive version with memoization (dictionary).
   - Global counters show how many recursive calls each version makes.
   - Test cases: `n = 5, 10, 20, 30`.

4. **Tower of Hanoi**
   - Function `hanoi(n, source, auxiliary, destination)`.
   - Prints the exact sequence of moves for `N = 3` disks.
   - Helps visualize how recursion works on a classic problem.

5. **Recursive Binary Search**
   - Function `binary_search(arr, key, low, high)`:
     - Returns index if found, otherwise `-1`.
     - Handles empty list and “key not present” cases.
   - Uses the `StackADT` to record all mid indices visited in each search.

## How to run

1. Make sure you have Python installed.
2. Open a terminal in this project folder.
3. Run:
   python aert_toolkit.py
