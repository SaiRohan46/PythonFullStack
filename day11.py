'''
ASSERT
-----------
--> This is debugging statement used to test whethe a condition is True
 Throws "AssertionError"
Example :
 
num=10
assert num>5 and num>15, "Not greater than 15"
print("True")

 
FUNCTIONS
-----------
--> A function is a block of code which only executes when its called.
--> We can pass data,known as parametres into a function
--> To avoid repeated lines in code
Syntax:
    def function_name(parametres):
      ----------
      ----------
    function_name(arguments)
--> Ways to Pass Arguments:
    ----------------------
    1.Required Arguments :
      --> A function must be called with the same number of arguments
    2.Default Arguments :
      --> The parametres that are returned when no arguments are passed
           in the called  function
--> Keyword Arguments :
    --> We can send arguments with key=value syntax.
        By this, the order of argumnts doesnt matter
--> Variable Length Arguments :
    --> Adding a star(*) also called as asteric before the parametre name
        in the function ,recieve a tuple of arguments and can access items
        with indexes
--> Pass by value AND Pass by Reference
ASSERT EXAMPLE
---------------
num=10
assert num>5 and num<15, "Not greater than 15"
print("True")

FUNCTIONS EXAMPLE
----------------
num=9
def even(num):
    if num%2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even(num)
even(1099)
even(900)

DEFAULT ARGUMENTS EXAMPLES
--------------------------

def even(name = "Teja",age=89):
    print(name)
    print(age)
even("rohan",65)
even(5678)

KEYWORD ARGUMENTS EXAMPLE
--------------------------------
def even(age,sal,name):
    print(name)
    print(age)
    print(sal)
even(name="Garikapati",age=89,sal=75000)

VARIABLE LENGTH ARGUMENTS EXAMPLE
-----------------------------------
def even(*name):
    print(name[1])
even("rohan","sai","rrrrr")


name="Teja"
def even(any):
    print(any)
even(name)#Pass by reference
even(23456)#Pass by value

'''
'''
Prime numbers upto a range
'''
def prime_numb(number):
    count = 0
    for i in range(2,number+1):
        if(number%i == 0):
            count+=1
    if(count==1):
        print(number)
n=int(input())
for i in range(1,n+1):
    prime_numb(i)
    









