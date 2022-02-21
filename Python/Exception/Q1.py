def exception_handling():
    try:
        num1 = int(input("Enter a number: "))
        num2 = 10 / num1

        if num2 == 1:
            num3 = 10

        print(f'You entered {num3}')
        input_str = "Hi!"
        output_str = input_str + num1
        print(output_str)

    except ValueError:
        print("Invalid Input.")

    except ZeroDivisionError:
        print("Input can't be 0.")

    except NameError:
        print("Can't process with this input.")

    except TypeError:
        print("Something went wrong🤔")

exception_handling()

