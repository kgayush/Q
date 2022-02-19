input_str = input("String: ")

output_str = f'{input_str[:2]}{input_str[-2:]}'

if len(input_str) < 2:
    print("Empty String")
else:
    print(output_str)