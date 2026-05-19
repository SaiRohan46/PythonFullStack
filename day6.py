#Hello day-6
'''
TYPE CONVERSIONS
-----------------------

a=78
b=str(a)
c=float(78)
print(c)
print(type(b))
print(type(c))


sr="90"
e=list(sr)
print(type(e))
print(e)
sr=float(sr)
print(type(sr))
print(sr)


car=90.088
print(int(car))

list1=[1,2,3]
print(str(list1))
print(tuple(list1))


how=(4,5)
print(list(how))
print(type(how))
print(str(how))
print(type(how))
print(how+(7,5))
'''
'''
USER INPUTS
------------
INT AS INPUT

num=int(input("Enter a Number:"))
print(num + 1)


STRING AS INPUT
---------------

some=input("Write a text:")
print(some)

LISTS AS INPUT
------------------

a=input("Enter the numbers: ").split()
any = list(map(int,input("Enter the numbers: ").split()))
print(any)
print(a)


TUPLE AS USER INPUT
--------------------

ar = tuple(map(int,input("Enter the numbers: ").split()))
print(ar)
'''
num=eval(input("enter :"))
print(type(num))
