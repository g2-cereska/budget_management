# main.py

from budget import get_budget, get_savings_goal, display_budget_summary, display_budget_summary
from expenses import add_expenses, calculate_total_expenses, display_expenses
from debts import add_debts, calculate_total_debt_payments, display_debt_summary
from data_manager import save_data, load_data

def main_menu():
    print("\n--- Budget Management Menu ---")
    print("1. Set Budget and Savings Goal")
    print("2. Manage Expenses")
    print("3. Manage Debts")
    print("4. View Summary")
    print("5. Save and Exit")
    return input("\nSelect an option: ")

def manage_expenses(expenses):
    expenses += add_expenses()  # Append new expenses to existing list
    display_expenses(expenses)

def manage_debts(debts):
    debts += add_debts()    # Append new debts to existing list
    display_debt_summary(debts)

def view_summary(budget, expenses, debts, savings_goal):
    total_expenses = calculate_total_expenses(expenses)
    total_debt_payments = calculate_total_debt_payments(debts)
    remaining_budget = budget - total_expenses - total_debt_payments

    display_expenses(expenses)
    display_debt_summary(debts)
    display_budget_summary(budget, remaining_budget, savings_goal)

if __name__ == "__main__":
    data = load_data()
    monthly_budget = data["budget"]
    savings = data["savings_goal"]
    expenditure = data["expenses"]
    money_owed = data["debts"]

    while True:
        choice = main_menu()

        if choice == '1':
            monthly_budget = get_budget()
            savings = get_savings_goal()

        elif choice == '2':
            if monthly_budget is None:
                print("\nPlease set your budget and savings goal first (Option 1).")
            else:
                manage_expenses(expenditure)

        elif choice == '3':
            if monthly_budget is None:
                print("\nPlease set your budget and savings goal first (Option 1).")
            else:
                manage_debts(money_owed)

        elif choice == '4':
            if monthly_budget is None:
                print("\nPlease set your budget and savings goal first (Option 1).")
            else:
                view_summary(monthly_budget, expenditure, money_owed, savings)

        elif choice == '5':
            save_data(monthly_budget, savings, expenditure, money_owed)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")