from datetime import datetime

def get_budget():
    budget = float(input("Enter your monthly budget: "))
    return budget

def add_expenses():
    expenses = []
    while True:
        expense_name = input("Enter the expense name (or type 'done' to finish): ")
        if expense_name.lower() == 'done':
            print(f"Exiting the program...")
            break
        elif not expense_name.strip():
            print(f"Please enter a valid expense name.")
            continue
        else:
            try:
                expense_amount = float(input(f"Enter the cost for {expense_name}: "))
                expense_date = input(f"Enter the date of the expense (YYYY-MM-DD): ")
                try:
                    datetime.strptime(expense_date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    continue

                expenses.append((expense_name, expense_amount, expense_date))
            except ValueError:
                print(f"Incorrect input. Please enter a valid number.")
                continue
    return expenses

def calculate_total_expenses(expenses):
    total = sum(expense[1] for expense in expenses)
    return total

def display_summary(budget, expenses):
    expenses_sorted = sorted(expenses, key=lambda x: x[2])  # Sort by third element (date)
    total_expenses = calculate_total_expenses(expenses_sorted)
    remaining_budget = budget - total_expenses

    print("\n--- Budget summary ---")
    for expense in expenses_sorted:
        print(f"{expense[2]} - {expense[0]}: £{expense[1]:.2f}")    # Date - Expense name: £Amount
    print(f"\nTotal expenses: £{total_expenses:.2f}")
    print(f"Remaining budget: £{remaining_budget:.2f}")

if __name__ == "__main__":
    income = get_budget()
    expenditure = add_expenses()
    display_summary(income, expenditure)
