tasks = []

# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass

while True:
    print("\n------- TO DO LIST -------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)

        # Save tasks to file
        with open("tasks.txt", "w") as file:
            for item in tasks:
                file.write(item + "\n")

        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            remove = int(input("Enter the task number to remove: "))

            if 1 <= remove <= len(tasks):
                removed_task = tasks.pop(remove - 1)

                # Save updated tasks to file
                with open("tasks.txt", "w") as file:
                    for item in tasks:
                        file.write(item + "\n")

                print(f"'{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")