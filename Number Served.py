# Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurent:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_rastaurant(self):
        print(f"\nRestaurant name:  {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}\n")

    def set_number_served(self):
        print(f"\tThis restaurant has {self.number_served} customers")

    def increment_number_served(self, newly_added_served):
        print(f"\tNo of customers served{newly_added_served}\n")
        self.number_served += newly_added_served


restaurant = Restaurent("Sony", "India")
restaurant.describe_rastaurant()
restaurant.set_number_served()

restaurant.increment_number_served(55)
restaurant.set_number_served()

restaurant.increment_number_served(63)
restaurant.set_number_served()

restaurant.increment_number_served(11)
restaurant.set_number_served()
