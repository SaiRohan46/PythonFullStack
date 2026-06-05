'''
Inheritance
------------
-> This allws one class to acquire the properies and methods of other class
Types:
------
1.Single Inheritance
----------------------
--> A class inherits from a single parent class

           Parent
             |
           Child
           
2.Multiple Inheritance
-----------------------
--> Child class inherited from "MORE THAN ONE PARENT CLASS"

             Parent1    Parent2
                |         |
                -----------
                     |
                   child
                   
3.Multi-Level Inheritance
--------------------------
-->A class inherits from a parent class and another class inherits from that
    class

            Parent 1
                |
         Child to parent1
        (Parent to child 2)
                |
        Child to above class
        

4.Hierarchial Inheritance
--------------------------
--> Multiple Child classes inherit from a single parent class

                Parent1
                /   |  \
               /    |   \
              c1    c2   c3
              
5.Hybrid Inheritance
----------------------
-->  

Basic SingleInheritance Example
-------------------------------
class father:
    def land(self):
        print("Father: I have 5Acres")
class Son(father):
    def own(self):
        print("I have 2Acres")
fam=Son()
fam.land()
fam.own()
#parent class cannot acess child class methods this throws error if called
#child class can access parent methods


Multiple Inheritance Example
------------------------------
class father:
    def land(self):
        print("My Father has X acres")
class mother:
    def gold(self):
        print("My Mom has Y acres")
class son(father,mother):
    def mine(self):
        print("I have nothingg")
me=son()
me.gold()
me.land()



Multi-LevelInheritance Example
-------------------------------
class grandfather:
    def land(self):
        print("My grandfather have 5A of land")
class father(grandfather):
    def flat(self):
        print("Have Flat at Bnglr")
class son(father):
    def ntg(self):
        print("Print i own both thier properties")
al=son()
al.land()
al.flat()
al.ntg()


Hierarchial Inheritance Example
-------------------------------
class father:
    def land(self):
        print("10 Acres Land")
class son1(father):
    def mine(self):
        print("Job")
class son2(father):
    def bro(self):
        print("Jobless")
s=son1()
s.land()
s.mine()
b=son2()
b.bro()
b.land()


HybridInheritance Example
--------------------------
class A:
    def some(self):
        print("class A")
class B(A):
    def any(self):
        print("class B")
class C(A):
    def so(self):
        print("class C")
class D(B,C):
    def all_(self):
        print("class D")
how=D()
how.some()
how.any()
how.so()
how.all_()

super() method
---------------
--> super() method is used to access methods and constructor of parent class
    from the child class
    
Example for super method
------------------------
class parent:
    def display(self):
        print('Method Parent')
class rohan(parent):
    def dis(self):
        super().display()
        print('Hiii')
an=rohan()
an.dis()



class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"{self.name} is name")
class stu(Person):
    def __init__(self,name):
        super().__init__(name)
    def show(self):
        print(f"Name: {self.name}")
'''
any_=stu("rohan")
print(any_.name)
any_.display()
any_.show()
