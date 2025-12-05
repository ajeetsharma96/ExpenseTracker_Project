def main():
     print("Running expense tracker.")

    # Ask for username
     username = input("Enter your username: ").strip()
     expense_file_path = f"expenses_{username}.txt"   # This will create unique file per user

     budget=float(input("Enter your budget: "))

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
    print(f"Getting user expense: ")

    # expense name
    expense_name=input("Enter expense name: ")
    print(f"You have entered {expense_name} ")
    
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