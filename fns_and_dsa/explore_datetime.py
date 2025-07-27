from datetime import datetime

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the result
    print("Current Date and Time:", formatted_date)

# Example usage
display_current_datetime()

from datetime import datetime, timedelta

def calculate_future_date(days_to_add):
    # Get the current date
    current_date = datetime.now()

    # Calculate future date
    future_date = current_date + timedelta(days=days_to_add)

    # Format future date as 'YYYY-MM-DD'
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Return the formatted date
    return formatted_future_date

# Ask user for input
try:
    days = int(input("Enter the number of days to add to the current date:"))
    result = calculate_future_date(days)
    print(f"Future date after {days} days: {result}")
except ValueError:
    print("Invalid input! Please enter an integer.")
