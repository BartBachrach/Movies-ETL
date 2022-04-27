# we own a taco stand and we want our customers to be able to 
# choose a meat and veggie for their taco

# our function prints to the kitchen the taco order

def make_taco(meat, veg):
    print(f"This taco has {meat} and {veg}.")

make_taco(meat='turkey', veg='sweet potatoes')

make_taco(meat='carnitas', veg='carnitas')


def make_better_taco(name, meat='chicken', veg='lettuce'):
    print(f"Taco for {name} has {meat} and {veg}.")

make_better_taco("Arnold", "steak", "guacamole")
make_better_taco('James')


print("-"*20)
def total_for_customer(tacos):
    """
    totals the customer's order and returns the amount

    """
    cost_per_taco = 1.25

    return round((cost_per_taco * tacos) * (1.07), 2)

print(total_for_customer(5))
arnold = total_for_customer(10)
drink = 2
shirt = 25
print("Arnolds total: $", arnold + drink + shirt)

