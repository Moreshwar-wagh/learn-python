#Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() 
# that prints a message indicating that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
# Create three different instances from the class, and call describe_restaurant() for each instance.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
            print(f"Restaurant name:  {self.restaurant_name}")
            print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
            print(f"{self.restaurant_name} restaurant  is open now,  come on & " f"try it {self.cuisine_type} food\n")

new_restaurant = Restaurant("Sony","USA")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

new_restaurant1 = Restaurant("CCD","India")
new_restaurant1.describe_restaurant()
new_restaurant1.open_restaurant()

new_restaurant2 = Restaurant("KFC","France")
new_restaurant2.describe_restaurant()
new_restaurant2.open_restaurant()
