class Restaurant():

    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nOur restaurant's name is " + self.restaurant_name.title() + ".")
        print("Our restaurant's type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is openning !")


my_restaurant = Restaurant('peace','chinese')

my_restaurant.open_restaurant()