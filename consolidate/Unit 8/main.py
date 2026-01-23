"""
Main Program: Fibonacci Numbers using Recursion

Demonstrates three approaches to calculating Fibonacci numbers:
1. Simple recursion (inefficient but educational)
2. Memoized recursion (optimized)
3. Iterative approach (most efficient)
"""

import functions


def get_number(prompt, max_value=None):
    """Get a non-negative integer from user."""
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print("Please enter a non-negative number.")
                continue
            if max_value and num > max_value:
                confirm = input(f"Values > {max_value} may be slow. Continue? (yes/no): ").strip().lower()
                if confirm not in ['yes', 'y']:
                    return None
            return num
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def main():
    """Main program entry point."""
    print("=" * 70)
    print("  FIBONACCI NUMBERS USING RECURSION")
    print("=" * 70)
    print("\nThis program demonstrates:")
    print("1. Simple recursion (learning only - inefficient)")
    print("2. Optimized recursion using memoization")
    print("3. Iterative approach for performance comparison")
    print("\nIt highlights:")
    print("• Importance of base cases")
    print("• Performance issues in naive recursion")
    print("• Benefits of optimization")
    
    while True:
        print("\n" + "=" * 70)
        print("Menu Options:")
        print("1. Calculate Single Fibonacci Number (Compare All Methods)")
        print("2. Display Fibonacci Sequence")
        print("3. Exit")
        print("=" * 70)
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            num = get_number("\nEnter a non-negative integer: ", 45)
            if num is not None:
                try:
                    functions.compare_all_methods(num)
                except RecursionError:
                    print("\n  Recursion depth exceeded!")
                    print("This demonstrates why base cases and optimization are crucial!")
        
        elif choice == "2":
            num = get_number("\nEnter how many numbers to display (0-50 recommended): ", 50)
            if num is not None:
                functions.display_sequence(num)
        
        elif choice == "3":
            print("\n" + "=" * 70)
            print("Thank you for exploring recursion!")
            print("\nRemember:")
            print("• Recursion breaks problems into smaller sub-problems")
            print("• Base cases prevent infinite recursion")
            print("• Optimization (memoization) can dramatically improve performance")
            print("=" * 70)
            break
        
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
