'''
1. `is` vs `==`

`==` (Equality):Checks if the values of two objects are equal.
`is` (Identity):Checks if two variables point to the exact same object in memory (i.e., they have the same memory address / `id()`).

# Both lists have the same values
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)  # True -> Because their contents are identical
print(list1 is list2)  # False -> Because they are two different objects in memory

print(list1 is list3)  # True -> Because list3 points directly to list1's memory space

2. `extend` vs `append`

`append()`:Adds its argument to the end of the list as a single element.
`extend()`:Iterates over its argument and adds each item to the list, extending its length.


# Using append
fruits1 = ['apple', 'banana']
fruits1.append(['kiwi', 'orange'])
print(fruits1)  
# Output: ['apple', 'banana', ['kiwi', 'orange']] -> Nestled list added

# Using extend
fruits2 = ['apple', 'banana']
fruits2.extend(['kiwi', 'orange'])
print(fruits2)  
# Output: ['apple', 'banana', 'kiwi', 'orange'] -> Flattended/Merged elements

3. Mutable vs Immutable

Mutable:Objects whose values can be modified after creation (e.g., Lists, Dictionaries, Sets).
Immutable:Objects whose values cannot be altered once created (e.g., Strings, Integers, Floats, Tuples).
If you modify an immutable object, Python actually creates a brand-new object in memory.

# Mutable Example (List)
my_list = [1, 2, 3]
my_list[0] = 99  # Allowed! Modifies the list in-place
print(my_list)   # [99, 2, 3]

# Immutable Example (String)
my_str = "Hello"
# my_str[0] = "Y"  # Throws a TypeError! You cannot alter it directly.


4. Memory Allocation in Python

Python automatically manages memory using two main mechanisms:

Reference Counting:Every object keeps track of how many variables point to it. When an object's reference count drops to 0, Python immediately reclaims that memory space.
Garbage Collection: A built-in cyclical garbage collector looks for "reference cycles" (e.g., Object A references Object B, and Object B references Object A,
but neither is accessible by your program) and cleans them up to prevent memory leaks.


5. Generators

Generators are functions that return an iterator using the `yield` keyword instead of `return`.
They generate items one at a time on-the-fly (lazy evaluation) rather than storing the entire dataset in your computer's RAM, making them incredibly memory efficient for massive datasets.


def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Calling the generator function doesn't run the code, it creates a generator object
counter = countdown(3)

print(next(counter))  # Output: 3
print(next(counter))  # Output: 2
print(next(counter))  # Output: 1
# Calling next() again would raise a StopIteration error
'''
class ATM:
    def __init__(self, name, account_number, pin, balance=0):
        self.name = name
        self.account_number = account_number
        self.__pin = pin 
        self.balance = balance

    def check_balance(self):
        print(f"\nAccount Holder: {self.name}")
        print(f"Current Balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nSuccessfully deposited ${amount}. New balance: ${self.balance}")
        else:
            print("\nInvalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"\nSuccessfully withdrew ${amount}. Remaining balance: ${self.balance}")
        elif amount > self.balance:
            print("\nInsufficient funds.")
        else:
            print("\nInvalid withdrawal amount.")

    def verify_pin(self, entered_pin):
        return self.__pin == entered_pin

def main():
    user_account = ATM(name="Rohan", account_number="123456", pin="4645", balance=1000)

    print("ATM System Initialized.")
    entered_pin = input("Please enter your 4-digit PIN: ")

    if user_account.verify_pin(entered_pin):
        while True:
            print("\n--- MENU ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            
            choice = input("Select an option: ")

            if choice == '1':
                user_account.check_balance()
            elif choice == '2':
                amt = float(input("Enter amount to deposit: "))
                user_account.deposit(amt)
            elif choice == '3':
                amt = float(input("Enter amount to withdraw: "))
                user_account.withdraw(amt)
            elif choice == '4':
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Incorrect PIN. Access Denied.")

if __name__ == "__main__":
    main()

















