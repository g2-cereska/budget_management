# main.py
import sys

from budget import get_budget, get_savings_goal, display_budget_summary
from expenses import add_expenses, calculate_total_expenses, display_expenses
from debts import add_debts, calculate_total_debt_payments, display_debt_summary
from data_manager import save_data, load_data

def select_year_month():
    year = input("Enter the year (YYYY): ")
    month = input("Enter the month (MM): ")
    selected_period = f"{year}-{month.zfill(2)}"    # Ensure month is 2 digits
    return selected_period

def main_menu():
    print("\n--- Budget Management Menu ---")
    print("1. Set Budget and Savings Goal")
    print("2. Manage Expenses")
    print("3. Manage Debts")
    print("4. View Summary")
    print("5. View Expenses for a Specific Month/Year")
    print("6. Save the data")
    print("7. Exit")
    return input("\nSelect an option: ")

def manage_expenses(expenses):
    expenses += add_expenses()  # Append new expenses to existing list
    display_expenses(expenses)

def manage_debts(debts):
    debts += add_debts()    # Append new debts to existing list
    display_debt_summary(debts)

def filter_expenses_by_month(expenses, selected_period):
    return [expense for expense in expenses if expense[2].startswith(selected_period)]

def view_summary(budget, expenses, debts, savings_goal):
    total_expenses = calculate_total_expenses(expenses)
    total_debt_payments = calculate_total_debt_payments(debts)
    remaining_budget = budget - total_expenses - total_debt_payments

    display_expenses(expenses)
    display_debt_summary(debts)
    display_budget_summary(budget, remaining_budget, savings_goal)

if __name__ == "__main__":
    data = load_data()
    monthly_budget = data.get("budget", None)
    savings = data.get("savings_goal", None)
    expenditure = data.get("expenses", [])
    money_owed = data.get("debts", [])

    while True:
        choice = main_menu()

        if choice == '1':
            monthly_budget = get_budget()
            savings = get_savings_goal()

        elif choice == '2':
            if monthly_budget is None or savings is None:
                print("\nPlease set your budget and savings goal first (Option 1).")
            else:
                manage_expenses(expenditure)

        elif choice == '3':
            if monthly_budget is None or savings is None:
                print("\nPlease set your budget and savings goal first (Option 1).")
            else:
                manage_debts(money_owed)

        elif choice == '4':
            if monthly_budget is None or savings is None:
                print("\nPlease set your budget and savings goal first (Option 1).")
            else:
                view_summary(monthly_budget, expenditure, money_owed, savings)

        elif choice == '5':
            selected_period = select_year_month()
            filtered_expenses = filter_expenses_by_month(expenditure, selected_period)
            if filtered_expenses:
                print(f"\n--- Expenses for {selected_period} ---")
                display_expenses(filtered_expenses)
            else:
                print(f"\nNo expenses found for {selected_period}.")

        elif choice == '6':
            if monthly_budget is None or savings is None:
                print("\nPlease set your budget and savings goal first (Option 1).")
            else:
                save_data(monthly_budget, savings, expenditure, money_owed)
        elif choice == '7':
            while True:
                exit_confirm = input("\nAre you sure you want to exit? (yes/no)\n").strip().lower()

                if exit_confirm == 'yes':
                    save_choice = input("Do you want to save your data before exiting? (yes/no)\n").strip().lower()

                    if save_choice.lower() == 'yes':
                        save_data(monthly_budget, savings, expenditure, money_owed)
                        print("\nData saved. Exiting the program. Goodbye!")
                    else:
                        print("\nChanges not saved. Exiting the program. Goodbye!")
                    sys.exit()

                elif exit_confirm == 'no':
                    break

            else:
                print("Invalid option. Please enter 'yes' or 'no'.")
