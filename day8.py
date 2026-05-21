#hello day-8
''''
ELIF
---> to get into number of conditions
--------------

m = 78
if m>=90:
    print("A+")
elif m>=80:
    print("A")
elif m>=70:
    print("B+")
elif m>=60:
    print("B")
elif m>=50:
    print("C+")
elif m>=35:
    print("Pass")
else:
    print("Failed")

a,b,c=int(input()),int(input()),int(input())
if(a>b and b>c):# or use a>(b and c)
    print(f"{a} is Largest")
elif(b>a and b>c):
    print(f"{b} is Largest")
else:
    print(f"{c} is Largest")


SBI_bank={"ATM PIN":"6600"}
pin=input("Enter 4 digit ATM pin :")
if(len(pin)) == 4:
    if pin in SBI_bank['ATM PIN']:
        print("Welcome to SBI ATM")
    else:
        print("Invalid Pin")
else:
    print("PLs enter 4 digit pin")

any="Python"
an=[1,2,3,4]
li=[]
li1=[]
so=(5,1.3,2,3,4)
for i in an:
    li.append(i)
print(li)
for i in so:
    li1.append(i)
print(li1)
------------------------
RANGE : range is a inbuilt function used to generate numbers in sequential
         manner 
Syntax---> range(start,end,step) #the step skips the number of steps 
------------------------
ELSE IN FOR : once the iterations are over this else is executed
------------------------
BREAK
---> used to exit from the looop based on the condition
------------------------
CONTINUE:
---> used to skip a current iteration based on the condition
-------------------------
PASS:
---> used to hold space
--------------------------
WHILE:
   --> it is the combination of for and if

for i in range(1,10,3):
    print(i)
else:
    print("Code ended here")
    

for i in range(1,10):
    if i == 3:
        pass
'''
n=int(input())
while n < 60:
    print(n)
    n+=1






