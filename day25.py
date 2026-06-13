#Hello day-25
#Project Based on re - verification of password,mail,ph number
'''
1.Mobile Number --> 10digit Indian number
2.Password --> Cap,Small,digit,special char,atleast 8
3.Mail --> @gmail.com
'''
import re
class Validation:
    def __init__(self,passw,mail,phno):
        self.passw=passw
        self.mail=mail
        self.phno=phno
    def validate_pass(self):
        if(re.fullmatch(r'([A-Za-z0-9_%@#&*?/"!]+){8,}',self.passw)):
            print("Valid Password")
        else:
            print("Invalid Password Should be 8 characters and contain Special symbols")
    def validate_number(self):
        if(re.fullmatch(r'^[6-9][0-9]{9}$',self.phno)):
            print("Valid Number")
        else:
            print("Invalid number")
    def validate_email(self):
        if(re.fullmatch(r'([a-zA-Z0-9.@#$%^&*()]+)@gmail\.com',self.mail)):
            print("Valid Mail")
        else:
            print("Invalid Mail")
v1=Validation(input(),input(),input())
v1.validate_pass()
v1.validate_email()
v1.validate_number()
            
        

































