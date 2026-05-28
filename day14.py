#Hello day-14
'''
LIST COMPREHENSION
--------------------
--> List comprehension offers a shortest syntax when we want to create a new
    list from existing list

    Syntax:
    var_name=[expression loop condition]

old=[1,2,2,3,4,5,6]
new=[i if i%2!=0 else "even" for i in old]
print(new)

GENERATORS
------------------
--> Generators in python are special type of itterable,allowing users to
    iterate over data efficiently without storing everything in memory
--> They generate values lazily using yield keyword

WHY TO USE GENERATORS
-------------------
--> Generators do not store the entire dataset in the memory,they generate
    values on th fly
--> Avoiding unneccesary storage of data speed up execution

HOW IT WORKS
-----------------
--> It works like nrml functions but uses the nyield keyword instead of return
--> when the function is called,it does not execute immediately.instead,it
    return a generator object which can be iterated using loop or the next()
    function


def sample_generator():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("end")
gen=sample_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def any(num):
    for i in range(num):
        yield i*i
a=any(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


def fibonacci(num):
    a=0
    b=1
    for i in range(num):
        c=a+b
        yield c
        a,b=b,c
a=any(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


def fibonacci(num):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(num):
        c=a+b
        print(c,end=" ")
        a,b=b,c
fibonacci(int(input()))

so='qwerfghoiugc vbansdvb,fdlfbkjbhyfd6w7q8ikdjfnbggyruewikjdhgy'
any=''
for j in so:
    if j not in 'AEIOUaeiou':
        any+=j
print(any)

'''















