#Make a class called User. Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized greeting to the user.
#Create several instances representing different users, and call both methods for each user.

class User:

    def __init__(self, first_name, last_name, user_name, birthdate, contact_no, email):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.birthdate = birthdate
        self.contact_no = contact_no
        self.email = email

    def describe_user(self):
        print(f"User full Name :{self.first_name} {self.last_name}")
        print(f"User name : {self.user_name}")
        print(f"Birthdate : {self.birthdate}")
        print(f"Contact no: {self.contact_no}")
        print(f"email address : {self.email}")

    def greet_user(self):
        print(f"HELLO  Mr.{self.first_name}\n")

new_user = User("Mohit","Wagh","mohit@99",28_03_1996,132456789,"mohit@99gmail.com")
new_user.describe_user()
new_user.greet_user()

another_user = User("Tonny", "Patil","tonny@28",20_12_1993,987645321,"tonny@22yahoo.com")
another_user.describe_user()
another_user.greet_user()