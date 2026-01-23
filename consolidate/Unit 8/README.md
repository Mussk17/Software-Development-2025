
# Unit 8: Fibonacci Numbers using Recursion - Concept of Recursion in Programming

A Python program demonstrating recursion through the Fibonacci sequence. This project implements three different approaches to calculating Fibonacci numbers and compares their performance.

## Overview

This program teaches recursion by demonstrating three computational approaches:

1. **Simple Recursion** - Basic recursive implementation (inefficient for large values)
2. **Memoized Recursion** - Optimized recursion using caching
3. **Iterative Approach** - Loop-based solution (most efficient)

## How to Run

```bash
python main.py
```

The program provides an interactive menu with the following options:
- Calculate a single Fibonacci number and compare all three methods
- Display the complete Fibonacci sequence up to a specified position
- Exit the program

## What is Recursion?

Recursion is a programming technique where a function calls itself to solve a problem. A recursive function must have:

1. **Base Case**: A stopping condition that prevents infinite recursion
2. **Recursive Case**: The function calls itself with a smaller problem

### Fibonacci Sequence

The Fibonacci sequence is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n ≥ 2

Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

## Implementation Approaches

### 1. Simple Recursive Fibonacci

```python
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

**Characteristics:**
- Time Complexity: O(2^n) - Exponential
- Direct implementation of the mathematical definition
- Recalculates the same values multiple times
- Suitable only for small values (n < 35)

### 2. Memoized Recursive Fibonacci

```python
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
```

**Characteristics:**
- Time Complexity: O(n) - Linear
- Stores previously calculated results to avoid recalculation
- Maintains recursive structure while improving performance
- Requires O(n) additional memory

### 3. Iterative Fibonacci

```python
def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b
```

**Characteristics:**
- Time Complexity: O(n) - Linear
- Space Complexity: O(1) - Constant
- Most efficient approach
- Does not demonstrate recursion

## Key Concepts

### Base Cases

Base cases are essential to stop recursion. Without them, the function would call itself infinitely, leading to stack overflow.

```python
if n == 0:
    return 0  # Base case
elif n == 1:
    return 1  # Base case
```

### Memoization

Memoization is an optimization technique that stores previously computed results. This eliminates redundant calculations in recursive algorithms.

**Why it matters:**
- Computing F(5) requires F(4) and F(3)
- Computing F(4) also requires F(3)
- Without memoization, F(3) is calculated twice
- With memoization, F(3) is calculated once and stored

### Performance Comparison

For F(35):
- Simple recursion: ~2-5 seconds
- Memoized recursion: ~0.0001 seconds
- Iterative: ~0.00001 seconds

## Program Features

### Feature 1: Compare All Methods

Compare all three implementations side-by-side with execution timing:
- See how simple recursion becomes slow for larger values
- Observe the performance improvement with memoization
- Compare with the iterative approach

### Feature 2: Display Sequence

View the complete Fibonacci sequence up to any position:
- Visualize the pattern
- Understand how numbers build on each other
- See the recursive formula in action

## Files

```
unit 8/
├── main.py          # Main program with interactive menu
├── functions.py     # Three Fibonacci implementations
└── README.md        # This documentation
```

## Functions

### functions.py

- `fibonacci_recursive(n)` - Simple recursive implementation
- `fibonacci_memo(n, memo=None)` - Memoized recursive implementation
- `fibonacci_iterative(n)` - Iterative implementation
- `compare_all_methods(n)` - Performance comparison function
- `display_sequence(n)` - Sequence display function

### main.py

- `main()` - Program entry point with menu system
- `get_number(prompt, max_value=None)` - Input validation helper

## Important Notes

### Performance Considerations

- Simple recursion becomes very slow for n > 35
- Memoization dramatically improves performance (20,000-50,000x speedup)
- Iterative approach is optimal for production code

### Input Constraints

- Input must be a non-negative integer
- Values > 35 may cause significant delays with simple recursion
- Memoized and iterative approaches handle larger values efficiently

## Learning Objectives

Upon completing this unit, students will:

1. Understand how recursive functions work
2. Recognize the importance of base cases
3. Learn memoization as an optimization technique
4. Compare different algorithmic approaches
5. Understand time complexity trade-offs

## Example Usage

```
Menu Options:
1. Calculate Single Fibonacci Number (Compare All Methods)
2. Display Fibonacci Sequence
3. Exit

Enter your choice (1-3): 1

Enter a non-negative integer: 10

======================================================================
  COMPARING FIBONACCI METHODS FOR n = 10
======================================================================

--- Simple Recursive Fibonacci ---
Result: 55
Time taken: 0.00002 seconds

--- Optimized Recursive Fibonacci (Memoization) ---
Result: 55
Time taken: 0.00001 seconds

--- Iterative Fibonacci ---
Result: 55
Time taken: 0.00001 seconds
```

## Real-World Applications

Recursion is used in:
- Sorting algorithms (merge sort, quicksort)
- Tree and graph traversal
- Dynamic programming problems
- Mathematical sequence calculations
- File system navigation

---

*This unit demonstrates the fundamentals of recursive programming and optimization techniques through the Fibonacci sequence.*
