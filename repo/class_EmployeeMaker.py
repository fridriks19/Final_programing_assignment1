import models.class_employee import Employee


class Employee_maker(Employee):
    def __init__(self):
        self.ssn = input("Kennitala: ")
        
# name = input("Nafn: ")
# rank = input("Stöðugildi: ")
# liscense = input("Réttindi: ")
# address = input("Heimilisfang: ")
# phonenumber = input("GSM-Sími:")