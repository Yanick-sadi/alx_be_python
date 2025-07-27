from datetime import datetime

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the result
    print("Current Date and Time:", formatted_date)

# Example usage
display_current_datetime()