def get_budget():
    budget = float(input("Enter your monthly budget: "))
    return budget

def get_expenses():
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
                expense_cost = float(input(f"Enter the cost for {expense_name}: "))
                expenses.append((expense_name, expense_cost))
            except ValueError:
                print(f"Incorrect input. Please enter a valid number.")
                continue
    return expenses

def calculate_remaining_budget(budget, expenses):
    total_expenses = sum([expense[1] for expense in expenses])
    return budget - total_expenses

def display_summary(budget, expenses):
    print("\nExpense summary:")
    for expense in expenses:
        print(f"{expense[0]}: £{expense[1]}")
    remaining_budget = calculate_remaining_budget(budget, expenses)
    print(f"\nTotal expenses: £{sum([expense[1] for expense in expenses])}")
    print(f"Remaining budget: £{remaining_budget}")

if __name__ == "__main__":
    budget = get_budget()
    expenses = get_expenses()
    display_summary(budget, expenses)
