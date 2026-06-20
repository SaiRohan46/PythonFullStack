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
  
    def verify_pin(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit ATM PIN: ")
            if entered_pin == self.pin:
                print(f"Welcome {self.name}")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. Attempts left: {attempts}")
        return False

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw: Rs{amount}")
            print(f"Please collect Rs{amount}")
            print(f"Remaining Balance: Rs{self.balance}")

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            self.transaction_history.append(f"Deposit: Rs{amount}")
            print(f"Rs{amount} deposited successfully")
            print(f"Updated Balance: Rs{self.balance}")
    
    def check_balance(self):
        print(f"Your Balance: Rs{self.balance}")

    def change_pin(self):
        old_pin = input("Enter old PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                print("PIN changed successfully")
            else:
                print("PIN must be 4 digits")
        else:
            print("Incorrect old PIN")

    def show_history(self):
        print("Transaction History:")
        if not self.transaction_history:
            print("No transactions yet")
        else:
            for t in self.transaction_history:
                print(t)

    def menu(self):
        while True:
            print("\n1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

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
                print("Thank you for using ATM")
                break
            else:
                print("Invalid choice")
user = ATM(account_holder["name"], account_holder["pin"], account_holder["balance"])
print("\nPlease insert your ATM card")
if user.verify_pin():
    user.menu()
else:
    print("Card blocked due to wrong PIN attempts")















