#Hello day 9
'''
--Nested for Example--

for i in range(1,10):
    for j in range(1,2):
        print(i)
        print(j)
        
---Printing Tables---

num=9
for j in range(1,21):
    print(f"{num} * {j} = {j*num}")
    
---UNDERSTANDING LOOPS AND PALINDROME---

so=input("Enter a word:")
empty_str=""
for j in so:
    empty_str = j + empty_str
    print(empty_str)
if empty_str == so:
    print(f"{so} is a palindrome")
else:
    print(f"{so} is not a palindrome")

----ARMSTRONG NUMBER--------
num = int(input("Enter a number:"))
a=0
length = len(str(num))
for i in str(num):
    a+=int(i)**length
if a==num:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not a armstrong number")

------PERFECT NUMBER----------

num=int(input())
per_nu=0
for j in range(1,num):
    if num%j == 0:
        per_nu += j
if per_nu == num:
    print(f"{num} is a perfect num")
else:
    print(f"{num} is not a pefect num")


num=int(input())
count=0
for j in range(1,num+1):
    if num%j == 0:
        count += 1
if(count == 2):
    print(f"{num} is a  prime number")
else:
    print(f"{num} is not a  prime number")


----ALPHABET PYRAMID-----
star=5
for g in range(1,star):
    for d in range(1,g+1):
        print(chr(64+d),end=" ")
    print()

star=5
count=0
for g in range(1,star+1):
    for d in range(1,g+1):
        count+=1
        print(countk,end=" ")
    print()


-----REVERSE TRIANGLE-----
star=5
count=0
for g in range(star,0,-1):
    for d in range(g):
        count+=1
        print("*",end=" ")
    print()
'''
num=5
for j in range(1,num+1):
    print(" "*(num-j),end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()





















