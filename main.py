import sqlite3
from user import User
from transaction import Transaction
from report import Report
from budget import Budget

def main():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    # Create tables if they don't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY, amount REAL, category TEXT, description TEXT, date DATE)''')
    c.execute('''CREATE TABLE IF NOT EXISTS budgets
                 (category TEXT PRIMARY KEY, amount REAL)''')
    conn.commit()
    conn.close()

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username, password)
            user.register()
            print("User registered successfully!")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if User.login(username, password):
                print("Login successful!")
                while True:
                    print("1. Add transaction")
                    print("2. View transactions")
                    print("3. Generate report")
                    print("4. Set budget")
                    print("5. Logout")
                    choice = input("Choose an option: ")

                    if choice == "1":
                        amount = float(input("Enter amount: "))
                        category = input("Enter category: ")
                        description = input("Enter description: ")
                        transaction = Transaction(amount, category, description)
                        transaction.save()
                        print("Transaction added successfully!")

                    elif choice == "2":
                        transactions = Transaction.get_all()
                        for transaction in transactions:
                            print(f"Amount: {transaction.amount}, Category: {transaction.category}, Description: {transaction.description}, Date: {transaction.date}")

                    elif choice == "3":
                        report = Report()
                        year = int(input("Enter year: "))
                        month = int(input("Enter month: "))
                        income, expenses, savings = report.get_monthly_report(year, month)
                        print(f"Income: {income}, Expenses: {expenses}, Savings: {savings}")

                    elif choice == "4":
                        budget = Budget()
                        category = input("Enter category: ")
                        amount = float(input("Enter amount: "))
                        budget.set_budget(category, amount)
                        print("Budget set successfully!")

                    elif choice == "5":
                        break

            else:
                print("Invalid username or password!")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
