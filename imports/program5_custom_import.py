"""
Program 5: Custom Module Import Demo
Practice: Importing custom modules with various import styles
This program demonstrates how to import and use a custom module.
"""

# Different ways to import from our custom module
import math_utils  # Import entire module
from math_utils import factorial, fibonacci  # Import specific functions
from math_utils import Calculator  # Import a class
from math_utils import PI as MATH_PI  # Import with alias
import math_utils as mu  # Import module with alias

def demonstrate_basic_import():
    """Demonstrate importing entire module"""
    print("=== Basic Import (import math_utils) ===")

    # Access module constants
    print(f"Value of PI: {math_utils.PI}")
    print(f"Value of E: {math_utils.E}")
    print(f"Golden Ratio: {math_utils.GOLDEN_RATIO}")

    # Use module functions
    print(f"\nGCD of 48 and 18: {math_utils.gcd(48, 18)}")
    print(f"LCM of 12 and 18: {math_utils.lcm(12, 18)}")

def demonstrate_specific_import():
    """Demonstrate importing specific items"""
    print("\n=== Specific Import (from math_utils import ...) ===")

    # Using directly imported functions
    print(f"Factorial of 6: {factorial(6)}")
    print(f"First 8 Fibonacci numbers: {fibonacci(8)}")

    # Using imported class
    calc = Calculator()
    calc.add(10, 5)
    calc.multiply(3, 4)
    calc.divide(20, 4)
    print(f"\nCalculator History:")
    for operation in calc.get_history():
        print(f"  - {operation}")

def demonstrate_alias_import():
    """Demonstrate importing with aliases"""
    print("\n=== Alias Import (import as ...) ===")

    # Using aliased constant
    print(f"PI imported as MATH_PI: {MATH_PI}")

    # Using aliased module
    print(f"Prime numbers up to 30: {mu.prime_numbers(30)}")
    print(f"Is 23 prime? {mu.is_prime(23)}")

def demonstrate_calculator_features():
    """Demonstrate the Calculator class in detail"""
    print("\n=== Calculator Class Demo ===")

    calc = Calculator()

    # Chain operations
    print("Performing chain calculations:")
    calc.add(100)
    print(f"  Start with 100: {calc.result}")
    calc.add(50)
    print(f"  Add 50: {calc.result}")
    calc.subtract(30)
    print(f"  Subtract 30: {calc.result}")

    # Show history
    print("\nOperation History:")
    for op in calc.get_history():
        print(f"  {op}")

def compare_import_methods():
    """Compare different import methods and their namespaces"""
    print("\n=== Import Method Comparison ===")

    # Method 1: Full module import
    print("Method 1 - Full Import:")
    print(f"  math_utils.factorial(4) = {math_utils.factorial(4)}")

    # Method 2: Specific import
    print("\nMethod 2 - Specific Import:")
    print(f"  factorial(4) = {factorial(4)}")  # Direct use

    # Method 3: Aliased module
    print("\nMethod 3 - Aliased Module:")
    print(f"  mu.factorial(4) = {mu.factorial(4)}")

    # Check namespace
    print("\nNamespace Check:")
    print(f"  'math_utils' in globals(): {'math_utils' in globals()}")
    print(f"  'factorial' in globals(): {'factorial' in globals()}")
    print(f"  'mu' in globals(): {'mu' in globals()}")

def demonstrate_practical_usage():
    """Show practical usage of the custom module"""
    print("\n=== Practical Usage Example ===")

    # Problem: Find all prime Fibonacci numbers under 100
    print("Finding prime Fibonacci numbers under 100:")

    # Generate Fibonacci numbers
    fib_numbers = fibonacci(20)  # Get first 20 Fibonacci numbers

    # Filter for primes under 100
    prime_fibs = []
    for num in fib_numbers:
        if num < 100 and mu.is_prime(num):
            prime_fibs.append(num)

    print(f"Fibonacci numbers: {fib_numbers[:10]}...")  # Show first 10
    print(f"Prime Fibonacci numbers under 100: {prime_fibs}")

    # Mathematical calculations
    print("\nMathematical Calculations:")
    numbers = [12, 18, 24]
    print(f"Numbers: {numbers}")

    # Find GCD of all numbers
    result = numbers[0]
    for num in numbers[1:]:
        result = math_utils.gcd(result, num)
    print(f"GCD of all numbers: {result}")

def main():
    """Main function to run all demonstrations"""
    print("=" * 60)
    print("CUSTOM MODULE IMPORT DEMONSTRATION")
    print("=" * 60)

    # Run all demonstrations
    demonstrate_basic_import()
    demonstrate_specific_import()
    demonstrate_alias_import()
    demonstrate_calculator_features()
    compare_import_methods()
    demonstrate_practical_usage()

    print("\n" + "=" * 60)
    print("Custom module demonstration completed!")
    print("=" * 60)

    # Show module information
    print("\nModule Information:")
    print(f"Module Name: {math_utils.__name__}")
    print(f"Module File: {math_utils.__file__ if hasattr(math_utils, '__file__') else 'Built-in'}")

if __name__ == "__main__":
    main()