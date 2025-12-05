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
 