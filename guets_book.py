print("If you want to stop then type 'Quit'")
filename = 'files/guest_book.txt'
while True:
    name = input("Enter your name:")
    if name == 'Quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
        print(f"Hello Mr.{name}, you have been added to guest list")
