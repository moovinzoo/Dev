available_toppings = ["mu", "ol", "gr", "pe", "pi", "ec"]
requested_toppings = ["mu", "ff", "ec"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don’t have " + requested_topping + ".")

print("\nFinished making your pizza!")
