"""
Fibonacci Numbers using Recursion

This module demonstrates:
1. Simple recursion (learning only - inefficient)
2. Optimized recursion using memoization
3. Iterative approach for performance comparison

It highlights:
- Importance of base cases
- Performance issues in naive recursion
- Benefits of optimization
"""

import time


def fibonacci_recursive(n):
    """Calculate Fibonacci number using simple recursion. WARNING: Inefficient for large n."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memo(n, memo=None):
    """Calculate Fibonacci number using recursion + memoization. Efficient and avoids repeated calculations."""
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


def fibonacci_iterative(n):
    """Calculate Fibonacci number using a loop. Most efficient approach."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


def compare_all_methods(n):
    """Compare all three methods with timing."""
    print("\n" + "=" * 70)
    print(f"  COMPARING FIBONACCI METHODS FOR n = {n}")
    print("=" * 70)
    
    if n > 35:
        print("\n Warning: Simple recursion will be very slow for n > 35")
        print("   This demonstrates why optimization matters!\n")
    
    print("\n--- Simple Recursive Fibonacci ---")
    if n <= 40:
        start = time.time()
        result = fibonacci_recursive(n)
        elapsed = time.time() - start
        print(f"Result: {result}")
        print(f"Time taken: {round(elapsed, 5)} seconds")
    else:
        print("Skipped (too slow for n > 40)")
    
    print("\n--- Optimized Recursive Fibonacci (Memoization) ---")
    start = time.time()
    result = fibonacci_memo(n)
    elapsed = time.time() - start
    print(f"Result: {result}")
    print(f"Time taken: {round(elapsed, 5)} seconds")
    
    print("\n--- Iterative Fibonacci ---")
    start = time.time()
    result = fibonacci_iterative(n)
    elapsed = time.time() - start
    print(f"Result: {result}")
    print(f"Time taken: {round(elapsed, 5)} seconds")
    
    print("\n" + "=" * 70)
    print("Key Takeaways:")
    print("• Simple recursion recalculates the same values many times")
    print("• Memoization stores results to avoid recalculation")
    print("• Iteration is often the fastest approach")
    print("=" * 70 + "\n")


def display_sequence(n):
    """Display Fibonacci sequence up to position n."""
    print("\n" + "=" * 70)
    print(f"  FIBONACCI SEQUENCE (First {n + 1} numbers)")
    print("=" * 70)
    print("\nPosition | Fibonacci Number")
    print("-" * 70)
    
    for i in range(n + 1):
        result = fibonacci_memo(i)
        print(f"   {i:3d}   |       {result:15d}")
    
    print("=" * 70)
    print(f"\nThe {n}th Fibonacci number is: {fibonacci_memo(n)}")
    print("\nPattern: Each number is the sum of the two preceding ones")
    print("Formula: fib(n) = fib(n-1) + fib(n-2)")
    print("Base cases: fib(0) = 0, fib(1) = 1")
    print("=" * 70 + "\n")
