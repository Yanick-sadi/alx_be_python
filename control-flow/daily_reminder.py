task = input("Enter your task:")
task_priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match task_priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a {task_priority} task that requires {task_priority} attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a {task_priority} task that requires {task_priority} attention today!")
    case "low":
        if time_bound == "no":
            print(f"{task} is a {task_priority} task. Consider completing it when you have free time.")
