from datetime import date

date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)

num_of_days = abs((date2 - date1).days)

print(f'{num_of_days} days')