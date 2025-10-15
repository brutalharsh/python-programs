"""
Program 2: Time Tracker
Practice: from module_name import specific_items and import module as alias
This program demonstrates selective imports and aliasing.
"""

from datetime import datetime, timedelta, date
import time as t

def track_execution_time(func):
    """Decorator to track function execution time"""
    def wrapper(*args, **kwargs):
        start = t.time()
        result = func(*args, **kwargs)
        end = t.time()
        print(f"  Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@track_execution_time
def simulate_work():
    """Simulate some work with a small delay"""
    print("  Simulating work...")
    t.sleep(0.5)  # Sleep for 0.5 seconds
    return "Work completed!"

def calculate_age(birth_year, birth_month, birth_day):
    """Calculate age from birthdate"""
    birthdate = date(birth_year, birth_month, birth_day)
    today = date.today()
    age = today.year - birthdate.year

    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age, birthdate

def schedule_reminders():
    """Create a schedule of reminders for the week"""
    now = datetime.now()
    reminders = []

    for i in range(1, 8):
        reminder_time = now + timedelta(days=i)
        reminders.append(reminder_time.strftime("%A, %B %d at %H:%M"))

    return reminders

def main():
    print("=== Time Tracker Application ===\n")

    # Current time information
    current_time = datetime.now()
    print(f"Current Date and Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Current Day: {current_time.strftime('%A')}")
    print(f"Current Month: {current_time.strftime('%B')}")

    # Age calculation
    print("\nAge Calculator:")
    age, birthdate = calculate_age(1995, 5, 15)
    print(f"  Birth Date: {birthdate.strftime('%B %d, %Y')}")
    print(f"  Current Age: {age} years")

    # Time until next year
    new_year = datetime(datetime.now().year + 1, 1, 1)
    time_until_new_year = new_year - datetime.now()
    print(f"\nDays until next year: {time_until_new_year.days}")

    # Execution time tracking
    print("\nFunction Execution Tracking:")
    result = simulate_work()
    print(f"  Result: {result}")

    # Schedule reminders
    print("\nWeekly Reminder Schedule:")
    reminders = schedule_reminders()
    for i, reminder in enumerate(reminders, 1):
        print(f"  Day {i}: {reminder}")

    # Unix timestamp
    print(f"\nCurrent Unix Timestamp: {t.time():.0f}")

if __name__ == "__main__":
    main()