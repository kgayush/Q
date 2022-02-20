def num_square(num):
    square = num * num
    return square


input_num = 121
if input_num > 100:
    result = num_square(5)

print(result)



# Q1: num is parameter passed in num_square function, square is local variable within num_square
#     function, input_sum is global variable and result is also not a global variable.

# Q2: input_num will be created first and destroyed after completion of programme and rest will be
#     created only if, 'if' statement runs.

# Q3: If input_num would have value less than 100, then if - block code will not run and hence
#     print statement will return NameError 

# Q4: result will not be created.