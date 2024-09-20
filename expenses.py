# expenses.py

from datetime import datetime
from categories import assign_category

def add_expenses():
    expenses = []
    while True:
        expense_name = input("Enter the expense name (or type 'done' to finish): ")
        if expense_name.lower() == 'done':
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

                available_categories = ["Housing", "Utilities", "Food", "Transportation", "Other"]

                expense_category = assign_category(expense_name)
                if expense_category == "Other":
                    print("Could not assign a category. Please enter a category for this expense.")
                    print(", ".join(available_categories))  # Display available categories
                    expense_category = input("Enter the category for this expense (or press Enter to choose 'Other'): ")
                    if not expense_category.strip():
                        expense_category = "Other"

                expenses.append((expense_name, expense_amount, expense_date, expense_category))
            except ValueError:
                print(f"Incorrect input. Please enter a valid number.")
                continue
    return expenses

def calculate_total_expenses(expenses):
    total = sum(expense[1] for expense in expenses)
    return total

def display_expenses(expenses):
    print("\n--- Expense summary ---")
    expenses_sorted = sorted(expenses, key=lambda x: x[2])  # Sort by third element (date)
    for expense in expenses_sorted:
        print(f"{expense[2]} - {expense[0]}: £{expense[1]:.2f} (Category: {expense[3]})")