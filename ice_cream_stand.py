# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand
# that inherits from the Restaurant class Either version of the class will work;
# just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.

from number_served import Retro
class IceCreamStand(Retro):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["Mango", "Vanilla", "Chocolate"]

    def display_flavours(self):
        print("The flavours of Ice-Cream are:")
        for items in self.flavours:
            print(f"\t {items.upper()} Ice-Cream")

restaurant = IceCreamStand("Sony", "India")
restaurant.describe_rastaurant()
restaurant.set_number_served()
restaurant.display_flavours()