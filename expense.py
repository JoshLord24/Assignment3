# This is an Expense Tracker

def main():


    expenses = {
        "Travel": [],
        "Food": [],
        "Entertainment": [],
        "Other": []
    }

    print("Please Input Travel Expenses: ")
    category = "Travel"
    while True:
        expense = input("Expense (or 'done' to finish): ")
        if expense.lower() == 'done':
            break
        expenses[category].append(float(expense))
    
    print("Please Input Food Expenses: ")
    category = "Food"
    while True:
        expense = input("Expense (or 'done' to finish): ")
        if expense.lower() == 'done':
            break
        expenses[category].append(float(expense))
    
    print("Please Input Entertainment Expenses: ")
    category = "Entertainment"
    while True:
        expense = input("Expense (or 'done' to finish): ")
        if expense.lower() == 'done':
            break
        expenses[category].append(float(expense))

    print("Please Input Other Expenses: ")
    category = "Other"
    while True:
        expense = input("Expense (or 'done' to finish): ")
        if expense.lower() == 'done':
            break
        expenses[category].append(float(expense))



    def expense_report(expenses, category):
            for category in expenses:
                print(f"Total {category} expenses: ${sum(expenses[category])}")
            print(f"Total expenses: $ {sum([sum(expenses[category]) for category in expenses])}")

    expense_report(expenses, category)        

main()