num = int(input("How many numbers?"))
total = 0
for i in range(num):
    numbers = float(input("Enter Number:"))
    total = total + numbers
    average = total / num
    print("Average of", {num}, "numbers is:", {average})