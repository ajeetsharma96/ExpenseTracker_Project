from expense import Expense
from typing import List
import datetime
import calendar
import os


def main():
     print("Running expense tracker.")

    # Ask for username
     username = input("Enter your username: ").strip()
     expense_file_path = f"expenses_{username}.txt"   # This will create unique file per user

     budget=float(input("Enter your budget: "))

     print(f"\nNice {username} !\nEnter your Expense Details\n")

    # Create file if not exists
     if not os.path.exists(expense_file_path):
        open(expense_file_path, "w").close()

     expense = get_user_expense()
     save_expense_to_file(expense, expense_file_path)
     summarize_expense(expense_file_path, budget)

    # Get user input for expense.
     expense=get_user_expense()
    # write their expense to a file.
     save_expense_to_file(expense,expense_file_path)
    # Read file and summarize expense.
     summarize_expense(expense_file_path,budget)
 

def get_user_expense():

    # expense name
    expense_name=input("\nEnter expense name: ")
    
    # expense amount
    expense_amount=float(input("Enter expense amount: "))

    # expense category
    expense_categories=[ 
        "Food","Home","Work","Fun","Miscellaneous","Shopping"
    ]
    
    while True:
        print("Select a category: ")
        for i,category_name in enumerate(expense_categories):
            print(f"{i+1}.{category_name}")
        value_range=f"[1 - {len(expense_categories)}]"
        selected_index=int(input(f"Enter a category number {value_range}: "))-1
        
        if selected_index in range(len(expense_categories)):
            selected_category=expense_categories[selected_index]
            new_expense= Expense(name=expense_name,category=selected_category,amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again!")

        break

def save_expense_to_file(expense: Expense,expense_file_path):
    print(f"Saving user Expense: {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(expense_file_path,budget):
    print(f"Summarize User Expense.")
    expenses: List[Expense] = []

    with open(expense_file_path,"r") as f:
        lines=f.readlines()
        for line in lines:
            expense_name,expense_amount,expense_category=line.strip().split(",")
            line_expense= Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

        amount_by_category = {}
        for expense in expenses:
            key=expense.category
            if key in amount_by_category:
                amount_by_category[key] += expense.amount
            else:
                amount_by_category[key] = expense.amount

        print("---------------------------------------")
        print(green("Expenses by Category: "))
        for key,amount in amount_by_category.items():
            print(yellow(f"  -> {key}: ${amount: .2f}"))
        print("---------------------------------------")
        total_spent = sum([ex.amount for ex in expenses])
        print(green(f"You've spent ${total_spent: .2f} this month!"))
        print("---------------------------------------")

        remaining_budget=budget - total_spent
        print(green(f"Budget remaining: ${remaining_budget: .2f}"))
        print("---------------------------------------")

        now=datetime.datetime.now()
        days_in_month=calendar.monthrange(now.year,now.month)[1]
        remaining_days=days_in_month - now.day  

        daily_budget=remaining_budget/remaining_days
        print(green(f"Budget Per Day: ${daily_budget: .2f}"))

def green(text):
        return f"\033[92m{text}\033[0m"
 
        lines= f.readlines()
        for line in lines:
            expense_name,expense_amount,expense_category=line.strip().split(",")
            line_expense=Expense(name=expense_name,amount=float(expense_amount),category=expense_category)
            expenses.append(line_expense)
        print(expenses)
             

def yellow(text):
    return f"\033[93m{text}\033[0m"

    lines= f.readlines()
    for line in lines:
        expense_name,expense_amount,expense_category=line.strip().split(",")
        line_expense=Expense(name=expense_name,amount=float(expense_amount),category=expense_category)
        expenses.append(line_expense)
    print(expenses)






if __name__=="__main__" :
    main()