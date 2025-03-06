import csv

EXPENSE_FILE = "expenses.csv"

def add_expense(amount, category, date):
    """Saves an expense to a file."""
    with open(EXPENSE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date])
    return True

def view_expenses():
    """Reads all expenses from the file."""
    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return [] 

def total_expenses():
    """Calculates the total money spent."""
    expenses = view_expenses()
    total = 0
    for row in expenses:
        if row: 
            total += float(row[0])
    return total

def main():
    print("Welcome to Expense Manager!")

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(amount, category, date)
            print("Expense added!")

        elif choice == "2":
            expenses = view_expenses()
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\nDate\t\tCategory\tAmount")
                print("-" * 30)
                for expense in expenses:
                    print(f"{expense[2]}\t{expense[1]}\t${expense[0]}")

        elif choice == "3":
            print(f"Total Expenses: ${total_expenses()}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
