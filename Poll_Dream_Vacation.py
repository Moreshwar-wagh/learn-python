# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.

user_name = "What is your name?"
one_place = "\nWrite a place if you clould visit one place in the world?"
repeat = "would you like to let another presons respond ? (yes/no) "

polling_active = True
responses = {}
while polling_active:
    user = input(user_name)
    place = input(one_place)
    responses[user_name] = responses
    repeat = input(repeat)
    if repeat == 'no':
        polling_active = False
        break


        print("\n--- Results ---")
        for user_name, one_place in responses.items():
            print(f"{user_name} would like to visit {one_place}")