'''

DOC STRING OR  F-STRING
-----------------------

CONDITIONAL STATEMENTS
------------------------
if --> used to check the statement is true or not
f-else ---> else in the if statement, inacse then condition becommes false
            and it will enter into fall-back(else),it will execute what ever
            is inside it
nested if
elif

num=5
if num%2==0:
    print("Even")
else:
    print("Odd")
n=10
if n%2==0:
    print(f"{n} is a Even number")
    print(n,"is a Even Num")
else:
    print(f"{n} is a Odd number")
age=16
if age>=18:
    print("You are eligible to vote")
else:
    print(f"you have to wait for {18-age} years to vote ")



num=8
num_2=15
if num >= num_2:
    print(f"{num} is greater number than {num_2}")
else:
    print(f"{num_2} is greater number than {num}")

year_=2024
if(year%4 == 0 and year%100 != 0) or year%400 == 0 :
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


vowel="a"
if vowel in 'aeiouAEIOU':
    print(f"{vowel} is a vowel")
else:
    print(f"{vowel} is a consonant")

number=-9
if number>=0:
    print(f"{number} is a positive number")
else:
    print(f"{number} is a negative number")

marks=int(input("Enter your marks:"))
stu_name=input("Enter your name :")
if marks>=45:
    print(f"{stu_name} is passed ")
else:
    print(f"{stu_name} is failed")
'''
num=75
if num%3==0 and num%5==0:
    print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num}not")











