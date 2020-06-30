# Admin: An administrator is a special kind of user.
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167).
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

from user import User
class Admin(User):
    def __init__(self, first_name, last_name, user_name, birthdate, contact_no, email):
        super().__init__(first_name, last_name, user_name, birthdate, contact_no, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        for items in self.privileges:
            print("Privilege is:",items)

new_user = Admin("Mohit", "Wagh","mohit@99",28_03_1996,132456789,"mohit@99gmail.com")
new_user.describe_user()
new_user.greet_user()
new_user.show_privileges()
