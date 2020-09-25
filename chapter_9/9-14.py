from random import randint

class Die():
    
    def __init__(self,sides=6):
        
        self.sides=sides
    
    def roll_die(self):
        """掷色子"""
        x=randint(1,self.sides)
        print("points: "+str(x))
    
die_6=Die()
for count in range(10):
    die_6.roll_die()

print()
die_10=Die(10)
for count in range(10):
    die_10.roll_die()

print() 
die_20=Die(20)
for count in range(10):
    die_20.roll_die()

        