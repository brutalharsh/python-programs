def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == number

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")