# categories.py

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

