user_info={"Name":"Kavya","MobileNo":"7486648762","ATM PIN":"0545",
           "Balance":76574,"Transaction History":[]}
print("Please insert your ATM Card")
rem_attempts=3
while rem_attempts>0:
    user_pin=input("Enter your 4-digit ATM Pin:")
    if len(user_pin)==4:
        if user_pin in user_info['ATM PIN']:
            print("Welcome")
            button=int(input("select buttons \n1.Withdraw \n2.Check Balance \n3.Mini statement \nEnter button:"))
            if button==1:
                w_amt=int(input("Enter the amount:"))
                if w_amt>user_info['Balance']:
                    print("Insufficient Balance")
                elif w_amt%100!=0:
                    print("Enter amount without Change")
                elif w_amt<500:
                    print("Enter min amount(500)")
                else:
                    print("Withdraw")
                    break
            elif button==2:
                print(f"Your current balance is: ₹{user_info['Balance']}")
                break
            elif button==3:
                print("Mini Statement")
                break
            elif button==4:
                print("Thankyou")
                break
            else:
                print("Invalid selection")
        else:
            rem_attempts-=1
            if rem_attempts>0:
                print(f"{rem_attempts} are left")
            else:
                print("Your card is blocked")
    else:
        print("Please enter 4-digit pin!")

