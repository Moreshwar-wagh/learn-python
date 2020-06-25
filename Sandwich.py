# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order,
# such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches
# After all the sandwiches have been made print a message listing each sandwich that was made.

sandwich_orders = ['tuna', 'corn & peas', 'veg shammi', 'chopped cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am working on your order that is {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)


    print("\n")
    for finished_sandwiches in finished_sandwiches:
        print(f" I made your {finished_sandwiches} sandwich ")