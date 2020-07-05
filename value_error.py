print("\t\nyou can finish,then type quit.")
while True:
    try:
        num1 = input("enter the 1st no : ")
        if num1 == 'quit':
            break
        num1 = int(num1)

        num2 = input("enter the 2nd no: ")
        if num2 == 'quit':
            break
        num2 = int(num2)
    except ValueError:
        print("You write a string, please enter a number/(integer value) ")
    else:
        add = num1 + num2
        print(f"Addition of two numbers is : {add} ")
print("You Quit")
