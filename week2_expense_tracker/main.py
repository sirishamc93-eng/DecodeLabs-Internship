expenses = []

try:
    with open("expenses.txt", "r") as file:
        for line in file:
            expenses.append(float(line.strip()))
except FileNotFoundError:
    pass

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Show Average")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        try:
            amount = float(input("Enter expense amount: "))
            expenses.append(amount)
            print("Expense added successfully!")

            # Save to file
            with open("expenses.txt", "a") as file:
                file.write(str(amount) + "\n")

        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\nYour Expenses:")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp}")

    elif choice == "3":
        print("Total Expenses:", sum(expenses))

    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses to calculate average.")
        else:
            print("Average Expense:", sum(expenses) / len(expenses))

    elif choice == "5":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
