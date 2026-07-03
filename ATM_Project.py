account_holder = {
    "name": "Rohan",
    "pin": "1234",
    "balance": 5000
}


class ATM:

    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    # ---------------- PIN Verification ----------------
    def verify_pin(self):
        attempts = 3

        while attempts > 0:
            entered_pin = input("Enter your 4-digit ATM PIN: ")

            if entered_pin == self.pin:
                print(f"\nWelcome, {self.name}!")
                return True

            attempts -= 1

            if attempts > 0:
                print(f"Incorrect PIN. Attempts left: {attempts}")

        return False

    # ---------------- Withdraw ----------------
    def withdraw(self):
        try:
            amount = int(input("Enter amount to withdraw: ₹"))

            if amount < 100:
                print("Minimum withdrawal amount is ₹100.")

            elif amount % 100 != 0:
                print("Withdraw amount must be in multiples of ₹100.")

            elif amount > self.balance:
                print("Insufficient balance.")

            else:
                self.balance -= amount
                self.transaction_history.append(f"Withdraw : ₹{amount}")
                print("\nPlease collect your cash.")
                print(f"Remaining Balance : ₹{self.balance}")

        except ValueError:
            print("Please enter a valid numeric amount.")

    # ---------------- Deposit ----------------
    def deposit(self):
        try:
            amount = int(input("Enter amount to deposit: ₹"))

            if amount <= 0:
                print("Invalid deposit amount.")

            else:
                self.balance += amount
                self.transaction_history.append(f"Deposit  : ₹{amount}")
                print("Amount deposited successfully.")
                print(f"Updated Balance : ₹{self.balance}")

        except ValueError:
            print("Please enter a valid numeric amount.")

    # ---------------- Balance ----------------
    def check_balance(self):
        print(f"\nAvailable Balance : ₹{self.balance}")

    # ---------------- Change PIN ----------------
    def change_pin(self):

        old_pin = input("Enter current PIN: ")

        if old_pin != self.pin:
            print("Incorrect current PIN.")
            return

        new_pin = input("Enter new 4-digit PIN: ")

        if not (new_pin.isdigit() and len(new_pin) == 4):
            print("PIN must contain exactly 4 digits.")
            return

        if new_pin == self.pin:
            print("New PIN cannot be the same as the old PIN.")
            return

        confirm_pin = input("Confirm new PIN: ")

        if new_pin != confirm_pin:
            print("PIN confirmation failed.")
            return

        self.pin = new_pin
        print("PIN changed successfully.")

    # ---------------- History ----------------
    def show_history(self):

        print("\n------ Transaction History ------")

        if not self.transaction_history:
            print("No transactions available.")

        else:
            for i, transaction in enumerate(self.transaction_history, start=1):
                print(f"{i}. {transaction}")

    # ---------------- Menu ----------------
    def menu(self):

        while True:

            print("\n========== ATM MENU ==========")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")
            print("==============================")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.withdraw()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.check_balance()

            elif choice == "4":
                self.change_pin()

            elif choice == "5":
                self.show_history()

            elif choice == "6":
                print("\nThank you for using our ATM.")
                print("Please collect your card.")
                break

            else:
                print("Invalid choice. Please try again.")


# ---------------- Main Program ----------------

user = ATM(
    account_holder["name"],
    account_holder["pin"],
    account_holder["balance"]
)

print("===================================")
print("        ABC BANK ATM")
print("===================================")
print("Please insert your ATM card.\n")

if user.verify_pin():
    user.menu()
else:
    print("\nYour card has been blocked due to 3 incorrect PIN attempts.")












