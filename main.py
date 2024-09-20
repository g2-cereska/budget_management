from datetime import datetime

def get_budget():
    budget = float(input("Enter your monthly budget: "))
    return budget

def assign_category(expense_name):
    if expense_name.lower() in ["rent", "mortgage"]:
        return "Housing"
    elif expense_name.lower() in ["electricity", "water", "gas", "internet", "phone", "lyca","council tax"]:
        return "Utilities"
    elif expense_name.lower() in ["groceries", "eating out", "takeout", "huel", "butcher", "bakery"]:
        return "Food"
    elif expense_name.lower() in ["bus", "train", "taxi", "car", "flight", "fuel"]:
        return "Transportation"
    elif expense_name.lower() in ["movie", "netflix", "spotify", "youtube", "books", "amazon prime", "games"]:
        return "Entertainment"
    elif expense_name.lower() in ["trip", "vacation", "holiday", "hotel", "tourism", "museum", "excursion"]:
        return "Tourism/Travel"
    elif expense_name.lower() in ["clothes", "shoes", "accessories"]:
        return "Shopping"
    elif expense_name.lower() in ["haircut", "salon", "beauty", "makeup", "nails", "spa", "jewelry", "perfume"]:
        return "Beauty/Personal Care"
    elif expense_name.lower() in ["school lunch", "tuition", "uniform", "school supplies"]:
        return "Education/Childcare"
    elif expense_name.lower() in ["capital one", "lloyds", "next", "currys", "argos", "zopa", "sainsburys", "tesco"
                                  , "rate setter", "klarna"]:
        return "Debts/Loans"
    elif expense_name.lower() in ["tools", "paint", "wood", "screws", "nails", "plumbing", "electrics", "repairs",
                                  "furniture", "lighting"]:
        return "Home Improvement/Repairs"
    else:
        return "Other"

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

def get_savings_goal():
    savings_goal = float(input("Enter your monthly savings goal: "))
    return savings_goal

def display_summary(budget, expenses, savings_goal):
    expenses_sorted = sorted(expenses, key=lambda x: x[2])  # Sort by third element (date)
    total_expenses = calculate_total_expenses(expenses_sorted)
    remaining_budget = budget - total_expenses

    print("\n--- Budget summary ---")
    for expense in expenses_sorted:
        print(f"{expense[2]} - {expense[0]}: £{expense[1]:.2f} (Category: {expense[3]})")
    print(f"\nTotal expenses: £{total_expenses:.2f}")
    print(f"Remaining budget: £{remaining_budget:.2f}")

    if remaining_budget >= savings_goal:
        print(f"Congratulations! You have met your savings goal of £{savings_goal:.2f}.")
    else:
        print(f"You are £{savings_goal - remaining_budget:.2f} "
              f"away from reaching your savings goal of £{savings_goal:.2f}.")

if __name__ == "__main__":
    income = get_budget()
    savings = get_savings_goal()
    expenditure = add_expenses()
    display_summary(income, expenditure, savings)
