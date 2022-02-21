class InvalidName(Exception):
    pass
class InvalidAge(Exception):
    pass
class InvalidEmail(Exception):
    pass
class InvalidPhone(Exception):
    pass

class Person:
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

def validate(person):
    flag = False
    try:
        if(person.name == ""):
            raise InvalidName
    except InvalidName:
        print("Invalid Name.")
    else:
        flag = True
    try:
        if(person.age > 100 and person.age < 0):
            raise InvalidAge
    except InvalidAge:
        print("Invalid Age.")
    else:
        flag = True
    try:
        if("@" not in person.email or person.email == ""):
            raise InvalidEmail
    except InvalidEmail:
        print("Invalid Email.")
    else:
        flag = True
    try:
        if(len(str(person.phone)) < 10):
            raise InvalidPhone 
    except InvalidPhone:
        print("Invalid Phone number.")
    else:
        flag = True
    return flag
   

name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")
phone = int(input("Enter your Phone number: "))
person = Person(name, age, email, phone)

valid = validate(person)
Person = list()

if(valid == True):
    Person.append(person)
    print("Your details has been submitted successfully.")



