from datetime import date

date1 = date(2022, 2, 19)
date2 = date(2021, 4, 19)

num_of_days = abs((date2 - date1).days)

print(f'Number of days: {num_of_days}')