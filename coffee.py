
print("Write how many ml of water the coffee machine has:")
available_water = int(input())
print("Write how many ml of milk the coffee machine has:")
available_milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
available_coffee_beans  = int(input())
print("Write how many cups of coffee you will need:")
qty_of_coffee = int(input())

water = 200
milk = 50
coffee_beans = 15

water_for_use = available_water // water
milk_for_use = available_milk // milk
beans_for_use = available_coffee_beans // coffee_beans

available_coffee = min(water_for_use, milk_for_use, beans_for_use)
more_coffee = available_coffee - qty_of_coffee

if available_coffee == qty_of_coffee:
    print('Yes, I can make that amount of coffee')
elif available_coffee > qty_of_coffee:
    print(f'Yes, I can make that amount of coffee (and even {more_coffee} more than that)')
elif available_coffee < qty_of_coffee:
    print(f"No, I can make only {available_coffee} cups of coffee")
