# Write your code here


water = 400
milk = 540
coffee_beans = 120
money = 550
disposable_cups = 9

def change_qty(water2, milk2, coffee_beans2, disposable_cups2, money2):
    
    global water
    global milk
    global coffee_beans
    global disposable_cups
    global money
    
    water -= water2
    milk -= milk2
    coffee_beans -= coffee_beans2
    disposable_cups -= disposable_cups2
    money += money2
    

    
def print_status():
    print(f'''The coffee machine now has:
    {water} ml of water
    {milk} ml  of milk
    {coffee_beans} g of coffee beans
    {disposable_cups} disposable cups
    ${money} of money''')
    
    
print_status()

print("Write action (buy, fill, take):")
operation = input()


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_type = input()
    
 
    if coffee_type == "3":
        
        change_qty(200, 100, 12, 1, 6)
        print_status()
    elif coffee_type == "2":
        change_qty(350, 75, 20, 1, 7)
        print_status()
    elif coffee_type == "1":
        change_qty(250, 0, 16, 1, 4)
        print_status()
    else:
        pass
        
def fill():
    print("Write how many ml of water do you want to add:")
    given_water = int(input())
    print("Write how many ml of milk do you want to add:")
    given_milk = int(input())
    print("Write how many grams of coffee do you want to add:")
    given_coffee = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    given_cups = int(input())
    
    change_qty(-given_water, -given_milk, -given_coffee, -given_cups, 0)
    print_status()
    
    
def take():
    
    print("I gave you $550")
    change_qty(0, 0, 0, 0, -550)
    print_status()
    
    
    
if operation == "buy":
    buy()
elif operation == "take":
    take()
elif operation == "fill":
    fill()
else:
    pass
    