'''
OOPS
------------------
1.CLASS
--------
--> A class is a blue print or template used to create object

ex: Syntax
class stu:
    name='Rohan'

2.OBJECT
---------
--> An object is an instance of a class

Example:
class stu:
    name='rohann'
s1=stu()
print(s1.name)

3.ATTRIBUTES
------------
--> These are the variables that belongs to class or an object

Example:
class stu:
    name="ronnn"
    age=46
s1=stu()
print(s1.name)
print(s1.age)

4.METHODS
----------
--> Functions in classes

5.CONSTRUCTOR
-------------
__init__
--> A constructor is a special method that is automatically called when
    an object is created

6.ACESSS SPECIFIERS
--------------------
1.Public
---------
--> This can be accessed from anywhere in the program
eg
--

2.Protected
------------
--> This is represented using a single underscore(_)

3.Private
----------
--> This is represeted using a double underscore(__)


7.ENCAPSULATION
---------------
--> It is the process of bindinng data and methods together


'''
class bank:
    def __init__(self,balance):
        self.__balance = balance
    def depo(self,amount):
        self.__balance += amount
    def get_bala(self):
        return self.__balance
acc=bank(1000)
acc.depo(10000)
print(acc.get_bala())
    
'''
class stu:
    name='Teja'
    def edu(self):
        print("I am studying B.Tech")
    def sports(self):
        print("Cricket")
        
s1=stu()
print(s1.name)
s1.edu()
s1.sports()

class pfs_da:
    def python(self):
        pfs_da="Batch-03"
        print("This is PFS and DA Batch-03")
    def Flask(self):
        pfs="batch_03"
        print("This is PFS Batch03")
all=pfs_da()
all.python()
all.Flask()

class ATM:
    def __init__(self,balance,name):
        self.balance=balance
        self.name=name
    def bal_check(self):
        print(f"{self.name} your total balance is {self.balance+700}")
    def names(self):
        print(self.name)
card=ATM(balance = 50000,name='Rohan')
card.bal_check()
card.names()

class stu:
    __name='Rohan'
s1=stu()
print(s1._stu__name)
print(s1.__name)

'''


