import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL
)
""")
conn.commit()

def add_expense(category, amount, date):
    cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)",(category, amount, date))
    conn.commit()
    print("Expense added successfully!")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    print("\n--- All Expenses ---")
    for row in rows:
        print(f"ID:{row[0]} | Category:{row[1]} | Amount:{row[2]} | Date:{row[3]}")

def delete_expense(expense_id):
    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    print("Expense deleted successfully!")

def expense_summary():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    print("\n--- Expense Summary ---")
    for row in rows:
        print(f"Category:{row[0]} | Total:{row[1]}")

def plot_expenses():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    categories = [row[0] for row in rows]
    amounts = [row[1] for row in rows]

    # Bar Chart
    plt.figure(figsize=(8,5))
    plt.bar(categories, amounts, color="skyblue")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.title("Expense Distribution - Bar Chart")
    plt.show()

    # Pie Chart
    plt.figure(figsize=(6,6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Expense Distribution - Pie Chart")
    plt.show()

# ------------------ Menu ------------------
def menu():
    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Expense Summary")
        print("5. Show Analytics (Charts)")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(category, amount, date)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)

        elif choice == "4":
            expense_summary()

        elif choice == "5":
            plot_expenses()

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, try again.")
menu()
conn.close()
'''
===== Expense Tracker Menu =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Expense Summary
5. Show Analytics (Charts)
6. Exit
Enter choice: 1
Enter category: food
Enter amount: 2400
Enter date (YYYY-MM-DD): 2026-03-02
Expense added successfully!

===== Expense Tracker Menu =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Expense Summary
5. Show Analytics (Charts)
6. Exit
Enter choice: 1
Enter category: food
Enter amount: 1900
Enter date (YYYY-MM-DD): 2026-04-09
Expense added successfully!

===== Expense Tracker Menu =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Expense Summary
5. Show Analytics (Charts)
6. Exit
Enter choice: 1
Enter category: travel
Enter amount: 4000
Enter date (YYYY-MM-DD): 2026-04-03
Expense added successfully!

===== Expense Tracker Menu =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Expense Summary
5. Show Analytics (Charts)
6. Exit
Enter choice: 2

--- All Expenses ---
ID:1 | Category:food | Amount:2400.0 | Date:2026-03-02
ID:2 | Category:food | Amount:1900.0 | Date:2026-04-09
ID:3 | Category:travel | Amount:4000.0 | Date:2026-04-03

===== Expense Tracker Menu =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Expense Summary
5. Show Analytics (Charts)
6. Exit
Enter choice: 3
Enter expense ID to delete: 2
Expense deleted successfully!

===== Expense Tracker Menu =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Expense Summary
5. Show Analytics (Charts)
6. Exit
Enter choice: 4

--- Expense Summary ---
Category:food | Total:2400.0
Category:travel | Total:4000.0

===== Expense Tracker Menu =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Expense Summary
5. Show Analytics (Charts)
6. Exit
Enter choice: 5

===== Expense Tracker Menu =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Expense Summary
5. Show Analytics (Charts)
6. Exit
Enter choice: 6
Exiting... Goodbye!
'''
