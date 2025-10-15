"""
Program 1: Math Calculator
Practice: import module_name
This program demonstrates importing the entire math module and using its functions.
"""

import math

def calculate_circle_properties(radius):
    """Calculate area and circumference of a circle"""
    area = math.pi * math.pow(radius, 2)
    circumference = 2 * math.pi * radius
    return area, circumference

def calculate_triangle_properties(a, b, c):
    """Calculate area using Heron's formula and check if valid triangle"""
    # Check if it's a valid triangle
    if a + b > c and b + c > a and a + c > b:
        # Calculate semi-perimeter
        s = (a + b + c) / 2
        # Calculate area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return None

def main():
    print("=== Math Calculator ===\n")

    # Circle calculations
    radius = 5
    area, circumference = calculate_circle_properties(radius)
    print(f"Circle with radius {radius}:")
    print(f"  Area: {area:.2f}")
    print(f"  Circumference: {circumference:.2f}")

    # Triangle calculations
    print("\nTriangle with sides 3, 4, 5:")
    triangle_area = calculate_triangle_properties(3, 4, 5)
    if triangle_area:
        print(f"  Area: {triangle_area:.2f}")

    # Other math operations
    print("\nOther Math Operations:")
    print(f"  Ceiling of 4.3: {math.ceil(4.3)}")
    print(f"  Floor of 4.7: {math.floor(4.7)}")
    print(f"  Square root of 16: {math.sqrt(16)}")
    print(f"  10 factorial: {math.factorial(10)}")
    print(f"  GCD of 48 and 18: {math.gcd(48, 18)}")
    print(f"  Sine of 30 degrees: {math.sin(math.radians(30)):.2f}")

if __name__ == "__main__":
    main()