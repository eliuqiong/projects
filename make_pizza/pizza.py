def make_pizza(size, *toppings):
    """summarize the proccess of making a pizza"""
    print(f"making a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")\n
