class Restaurant():
    
    def __init__(self, name, cuisine_type):
        self.restaurant_name=name
        self.cuisine_type=cuisine_type
        self.number_served=0
    
    def describe_restaurant(self):
        print("\nOur restaurant's name is "+self.restaurant_name.title()+".")
        print("Our restaurant's type is "+self.cuisine_type.title()+".")
    
    def open_restaurant(self):
        print(self.restaurant_name.title()+" is openning !")
    
    def read_number_served(self):
        print("\n"+str(self.number_served)+" people",
              " have been served here.")
    
    def set_number_served(self,number):
        self.number_served=number
    
    def increment_number_served(self,number):
        if number>=0:
            self.number_served+=number
        else:
            print("You cna not decrease numbers of guests!")

class IceCreamStand(Restaurant):
    
    def __init__(self,name,cuisine_type):
        
        super().__init__(name,cuisine_type)
        self.flavors=['Strawberry','mike','coffee']
    
    def read_flavors(self):
        """显示冰淇淋口味"""
        print(self.flavors)

ice=IceCreamStand('Ice House','Italy')
ice.read_flavors()
ice.read_number_served()
