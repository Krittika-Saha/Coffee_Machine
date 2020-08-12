# Write your code here


water = 400
milk = 540
coffee_beans = 120
money = 550
disposable_cups = 9

print(f'''The coffee machine has:
{water} ml of water
{milk} ml of milk
{coffee_beans} g of coffee beans
{disposable_cups} disposable cups
${money} of money''')

print("Write action (buy, fill, take):")
operation = input()







def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_type = input()

    if coffee_type == "3":
        global water
        global milk
        global coffee_beans
        global disposable_cups
        global money
        
        water = water -  200
        milk = milk - 100
        coffee_beans = coffee_beans - 12
        disposable_cups = disposable_cups - 1
        money = money + 6
        print(f'''The coffee machine now has:
        {water} ml of water
        {milk} ml  of milk
        {coffee_beans} g of coffee beans
        {disposable_cups} disposable cups
        ${money} of money''')
    elif coffee_type == "2":
        milk = 540
        coffee_beans = 120
        money = 550
        disposable_cups = 9
        water = 400
        water = water - 350
        milk = milk - 75
        coffee_beans = coffee_beans - 20
        money = money + 7
        disposable_cups -= 1
        print(f'''The coffee machine now has:
        {water} ml of water
        {milk} ml  of milk
        {coffee_beans} g of coffee beans
        {disposable_cups} disposable cups
        ${money} of money''')
    elif coffee_type == "1":
        milk = 540
        coffee_beans = 120
        money = 550
        disposable_cups = 9
        water = 400
        disposable_cups -= 1
        water = water - 250
        coffee_beans = coffee_beans - 16
        money = money + 4
        print(f'''The coffee machine now has:
        {water} ml of water
        540 ml of milk
        {coffee_beans} g of coffee beans
        {disposable_cups} disposable cups
        ${money} of money''')
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
    
    milk = 540
    coffee_beans = 120
    money = 550
    disposable_cups = 9
    water = 400
    
    water = water + given_water
    milk = milk + given_milk
    coffee_beans = coffee_beans + given_coffee
    disposable_cups = disposable_cups + given_cups
    print(f'''The coffee machine now has:
    {water} ml  of water
    {milk} ml of milk
    {coffee_beans} g of coffee beans
    {disposable_cups} disposable cups
    ${money} of money''')
    
    
def take():
    
    print("I gave you $550")
    milk = 540
    coffee_beans = 120
    money = 550
    disposable_cups = 9
    water = 400
    money = 0
    print(f'''The coffee machine now has:
    {water} ml of water
    {milk} ml of milk
    {coffee_beans} ml of coffee beans
    {disposable_cups} disposable cups
    ${money} of money''')
    
    
if operation == "buy":
    buy()
elif operation == "take":
    take()
elif operation == "fill":
    fill()
else:
    pass
    