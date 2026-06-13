'''
Polymorphism
=============
--> this means "many forms". it allows the same function ,method, or operator to behave differently depending on the object.

1.method overloading
-->this means defining multiple methods with the same name but different parameters
eg:
class cal:
    def add(self,a,b,c=0):
        return a+b+c
an=cal()
print(an.add(23,6))
print(an.add(23,6,23))

class cal:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=0):
        return a+b+c
an=cal()
print(an.add(23,6))

2.method overriding
-->this occurs when a child class provides its own implementation of a method already defined in the parent class.
class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
        super().sound() #to access the parent class method 
ntg=dog()
ntg.sound() #overrides the parent class method and gives the child class method
o/p:
Dog barks
Animal makes sound

3.operator overloading
--> this allows operators such as +,-,* etc, to perform different actions for user-defined objects
class stu:
    def __init__(self,marks):
        self.marks=marks
    def __sub__(self,other):
        return self.marks+other.marks
so1=stu(4)
so=stu(2)
print(so1-so)

Data Abstraction
================
--> this is the process of hiding internal implementation details and showing only the essential features to the user
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def peri(self):
        pass
class rec(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def peri(self):
        return 2*(self.a+self.b)
an=rec(10,5)
print(an.area())
print(an.peri())
'''









































