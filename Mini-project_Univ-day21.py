#Mini Project University
class Person:
    university = "ABC University"
    def  __init__(self,name,age,ed_back,dept):
        self.name=name
        self.age=age
        self.ed_back=ed_back
        self.dept=dept
    def display(self):
        pass
class Stu(Person):
    def __init__(self,name,age,ed_back,dept,branch,studentid):
        super().__init__(name,age,ed_back,dept)
        self.branch=branch
        self.studentid=studentid
    def display(self):
        print(f"Name :{self.name} |Age :{self.age} |Branch :{self.branch} |studentid: {self.studentid} | univ:{self.university}")
class Faculty(Person):
    def __init__(self,name,age,ed_back,dept,facultyid):
        super().__init__(name,age,ed_back,dept)
        self.facultyid=facultyid
    def display(self):
        print(f"Name :{self.name} |Age :{self.age} |Branch :{self.dept} |studentid: {self.facultyid}")
f1=Faculty(input(),int(input()),input(),input(),input())
f1.display()
s1=Stu(input(),int(input()),input(),input(),input(),input())
s1.display()
