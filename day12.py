#Hello day-12
'''
BUILT IN FUNCTIONS
--------------------
print()
input()
len()
type()
max()
min()

EXAMPLE FOR SORT AND SORTED
---------------------------

m=[3,4,1,2,3]
print(sorted(m))#only runtime modify
print(m)
m.sort()
print(m)
'''
"""
RECURSIVE FUNCTIONS
--------------------
--> A Recursive Function calls itself to solve a problem by breaking it into
    small or simple sub-problems

def fac(num):
    if (num ==1):
        return 1
    return num*fac(num-1)
print(fac(5))

RETURN
------
--> this ends a function execution and sends a value back to the code that
    callled the function
eg:
def add(a,b):
    return a+b
res = add(4,5)
print(res)

LAMBDA FUNCTIONS
-----------------
--> A lambda function is a small function
-->  A lambda function can take n number of arguments,but only one function

"""
so=lambda a,b,c:a+b+c+a
print(so(3,4,9))


a=lambda x : print("Positive") if x>0  else print("Negative")
a(-2345)

















