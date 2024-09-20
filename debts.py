# debts.py

def add_debts():
    debts = []
    while True:
        debt_name = input("Enter the debt name (or type 'done' to finish): ")
        if debt_name.lower() == 'done':
            break
        debt_amount = float(input(f"Enter the total debt owed for {debt_name}: "))
        monthly_payment = float(input(f"Enter the monthly payment for {debt_name}: "))
        debts.append((debt_name, debt_amount, monthly_payment))
    return debts

def calculate_total_debt_payments(debts):
    return sum(debt[2] for debt in debts)   # Sum of monthly debt payments

def display_debt_summary(debts):
    print("\n--- Debt summary ---")
    for debt in debts:
        print(f"{debt[0]}: Total debt - £{debt[1]:.2f}, Monthly payment - £{debt[2]:.2f}")

