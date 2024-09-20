# budget.py

def get_budget():
    budget = float(input("Enter your monthly budget: "))
    return budget

def get_savings_goal():
    savings_goal = float(input("Enter your monthly savings goal: "))
    return savings_goal

def display_budget_summary(budget, remaining_budget, savings_goal):

    print("\n--- Budget summary ---")
    print(f"\nTotal expenses: £{budget:.2f}")
    print(f"Remaining budget: £{remaining_budget:.2f}")

    if remaining_budget >= savings_goal:
        print(f"Congratulations! You have met your savings goal of £{savings_goal:.2f}.")
    else:
        print(f"You are £{savings_goal - remaining_budget:.2f} "
              f"away from reaching your savings goal of £{savings_goal:.2f}.")