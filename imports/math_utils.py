"""
Custom Module: Math Utilities
This is a custom module that will be imported by program5_custom_import.py
Save this as: math_utils.py
"""

# Constants
PI = 3.14159265359
E = 2.71828182846
GOLDEN_RATIO = 1.61803398875

def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(limit):
    """Generate all prime numbers up to limit"""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

class Calculator:
    """A simple calculator class"""

    def __init__(self):
        self.result = 0
        self.history = []

    def add(self, x, y=None):
        """Add numbers"""
        if y is None:
            self.result += x
            self.history.append(f"Added {x}, Result: {self.result}")
            return self.result
        else:
            result = x + y
            self.history.append(f"Added {x} + {y} = {result}")
            return result

    def subtract(self, x, y=None):
        """Subtract numbers"""
        if y is None:
            self.result -= x
            self.history.append(f"Subtracted {x}, Result: {self.result}")
            return self.result
        else:
            result = x - y
            self.history.append(f"Subtracted {x} - {y} = {result}")
            return result

    def multiply(self, x, y):
        """Multiply numbers"""
        result = x * y
        self.history.append(f"Multiplied {x} * {y} = {result}")
        return result

    def divide(self, x, y):
        """Divide numbers"""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        result = x / y
        self.history.append(f"Divided {x} / {y} = {result}")
        return result

    def clear(self):
        """Clear calculator"""
        self.result = 0
        self.history = []

    def get_history(self):
        """Get calculation history"""
        return self.history

# Module-level function
def gcd(a, b):
    """Calculate Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate Least Common Multiple"""
    return abs(a * b) // gcd(a, b)

# This will only run if the module is executed directly
if __name__ == "__main__":
    print("Math Utils Module Test")
    print(f"PI = {PI}")
    print(f"Factorial of 5 = {factorial(5)}")
    print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Prime numbers up to 20: {prime_numbers(20)}")