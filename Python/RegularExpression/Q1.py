import re
pattern = "^(January|Feburary|March|April|May|June|July|August|September|October|November|December)\s+(\d{2},)\s+(\d{4})"
input_date = input('Enter date in this format only: "June 03, 2007": ')
output = re.match(pattern, input_date)
if output == None:    
    print("Wrong format.")
else:
    print("Right format.")
