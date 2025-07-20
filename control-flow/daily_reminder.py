task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: finish {task} is a {priority} task that requires {priority} attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: finish {task} is a {priority} task that requires {priority} attention today!")
    case "low":
        if time_bound == "no":
            print(f"Reminder: finish {task} is a {priority} task. Consider completing it when you have free time.")
