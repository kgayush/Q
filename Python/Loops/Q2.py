color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

output = set()
for color in color_list_1:
    if color not in color_list_2:
        output.add(color)

print(output)
