length = int(input("Enter length of list: "))
number_list = []

for i in range(length):
    number = int(input())
    number_list.append(number)

print(f'Maximum: {max(number_list)}')