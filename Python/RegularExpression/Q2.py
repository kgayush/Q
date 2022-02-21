import re

def credit_card(number):
    pattern = '^([349][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
    output = re.match(pattern, number)
    if(output == None):    
        return False
    else:
        return True
    
input_number = input('''Enter credit card number which should satisy following conditions:
1: It must start with a 3, 4, or 9.
2: It must contain exactly 16 digits.
3: It must NOT have 2 or more consecutive repeated digits.
4: Format: xxxx-xxxx-xxxx-xxxx
: ''')
print(credit_card(input_number))
