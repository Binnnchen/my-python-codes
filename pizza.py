def make_pizza(size,*toppings):
    """制作pizza"""
    print("\nMaking a "+str(size)+"-inch pizza with following toppings:")
    for topping in toppings:
        print("-"+topping)

