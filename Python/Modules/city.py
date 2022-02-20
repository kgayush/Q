def greet_user(name):
    print(f'Hi {name}! Welcome to Hogwarts.')

def house(house_num):
    houses = {
        "1": "Gryffindor",
        "2": "Hufflepuff",
        "3": "Ravenclaw",
        "4": "Slytherin"
    }
    print(f'Welcome to {houses.get(house_num, "!")} house.')

def leave_message():
    print("Bye, visit again.")