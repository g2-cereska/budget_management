# data_manager.py

import json
import os

DATA_FOLDER = "data"

def ensure_data_folder_exists():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
        print(f"Created folder: {DATA_FOLDER}")

def save_data(budget, savings_goal, expenses, debts, filename="budget_data.json"):
    data = {
        "budget": budget,
        "savings_goal": savings_goal,
        "expenses": expenses,
        "debts": debts
    }
    ensure_data_folder_exists()
    filepath = os.path.join(DATA_FOLDER, filename)
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filepath} as {filename}.")

def load_data(filename="budget_data.json"):
    ensure_data_folder_exists()
    filepath = os.path.join(DATA_FOLDER, filename)
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            print(f"Data loaded from {filename} in {filepath}.")
            return data
    except FileNotFoundError:
        print(f"No saved data found ({filename} in {filepath}). Starting with empty data.")
        return {"budget": None, "savings_goal": None, "expenses": [], "debts": []}

def get_current_month():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m")