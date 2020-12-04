# Write your code here
from time import sleep
from art import logo
print(logo)
water=400
milk=540
coffee_beans=120
money=550
disposable_cups=9

workers = {
    "Richard": "callmerichard",
    "Amy": "qwerty",
    "Sara": "1234"
}

def verify_manager(username, password):
  global workers
  managers = {
    "John": "managerjohn",
    "Laviosa": ":)"
  }
  for manager in managers:
    if username == manager and managers[username] == managers[manager]:
      print(f"Hello {username}! ")
      while True:
        manager_action = input("What do you want to do? (add workers/remove workers/exit manager mode): ")
        if manager_action == "add workers":
          worker_name = input("Name?: ")
          worker_password = input("Worker password?: ")
          workers[worker_name] = worker_password 
          print("Worker has been successfully added")
          print(f"Updated worker dictionary: {workers}")
        elif manager_action == 'remove workers':
          del workers[input("Name?: ")]
          print("Worker has been successfully removed")
          print(f"Updated worker dictionary: {workers}")
        elif manager_action == 'exit':
          print("Bye")
          break
        else:
          print("I don't understand.") 
    elif managers[username] != managers[manager]:
      print("Get outta here.") 
def transaction(coffee_wanted):
  """Takes, refunds or gives back the money given by the user"""
  cost = {
    'espresso': 1.5,
    "latte": 2.5,
    'cappucino': 3.0
  }
  if coffee_wanted == 'espresso':
    print(f"You wanted an espresso. The cost is $1.5.")
  else:
    print(f"You wanted a {coffee_wanted}. The cost is ${cost[coffee_wanted]}.")
  pennies = int(input("How many pennies?: "))/100
  nickels= (int(input("How many nickels?: "))/100)*5
  dimes = int(input("How many dimes?: "))/10
  quarters = (int(input("How many quarters?: "))/100)*25
  total_money = pennies + nickels +dimes + quarters
  print(f"You gave {total_money}")
  if total_money == cost[coffee_wanted]:
    return True
  elif total_money > cost[coffee_wanted]:
    print(f"Here is your refund, ${total_money-cost[coffee_wanted]}")
    return True
  elif total_money < cost[coffee_wanted]:
    return False
def verify(user, password):
  """Verifies if a person is a worker or not."""
  for worker_checker in workers:
    if worker_checker == user:
      if workers[worker_checker] == workers[user]:
        return True
def change_qty(water2,milk2,coffee_beans2,disposable_cups2,money2):
  """Changes the amount of water, milk, coffee, cups and money"""
  global water, milk, coffee_beans, disposable_cups, money
  water -= water2
  milk -= milk2
  coffee_beans -= coffee_beans2
  disposable_cups -= disposable_cups2
  money += money2
def print_status():
  """Prints the amount of milk, coffee, cups, water and money in the coffee machine"""
  print(f'''The coffee machine now has:
{water} ml of water
{milk} ml  of milk
{coffee_beans} g of coffee beans
${money} of money
{disposable_cups} disposable cups''')
def actions():
  """Starting input"""
  choose_action = input("Write action (buy, fill, take, report, exit, manage):") 
  return choose_action
def check_cups():
  """Checks how many cups are left"""
  if disposable_cups < 1:
    print("Sorry, not enough disposable cups!")
def buy():
  """Helps the users buy a coffee"""
  coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
  if coffee_type == "3":
      check_cups()
      if water < 200:
        print("Sorry, not enough water!")
      elif milk < 100:
        print("Sorry, not enough milk!")
      elif coffee_beans < 12:
        print("Sorry, not enough coffee beans!")
      else:
        if transaction('cappucino') == True:
          print("Transaction successful")
          print("I have enough resources, making you a coffee")
          sleep(3)
          print("Here you go, enjoy!☕")
          change_qty(200, 100, 12, 1, 3)
        else:
          print("Not enough money, refunded.")
  elif coffee_type == "2":
      check_cups()
      if water < 350:
        print("Sorry, not enough water!")
      elif milk < 75:
        print("Sorry, not enough milk!")
      elif coffee_beans < 20:
        print('Sorry, not enough coffee beans!')
      else:
        if transaction('latte') == True:
          print("Transaction successful")
          print("I have enough resources, making you a coffee!")
          sleep(3)
          print("Here you go, enjoy!☕")
          change_qty(350, 75, 20, 1, 2.5)
        else:
          print("Not enough money, refunded.")
  elif coffee_type == "1":
      check_cups()

      if water < 250:
        print("Sorry, not enough water!")
      elif coffee_beans < 16:
        print("Sorry, not enough coffee beans!")  
      else:
        if transaction('espresso') == True:
          print("Transaction successful")
          print("I have enough resources, making you a coffee!")
          sleep(3)
          print("Here you go, enjoy!☕")
          change_qty(350, 75, 20, 1, 1.5)    
        else:
          print("Not enough money, refunded.")    
  else:
      pass
def fill():
  """Refills the Coffee Machine"""
  if verify(input("Please give your working username: "), input("Please enter your password:")) == True:
    print("You have been verified, and can now proceed.")
    given_water = int(input("Write how many ml of water do you want to add:"))
    given_milk = int(input("Write how many ml of milk do you want to add:"))
    given_coffee = int(input("Write how many grams of coffee do you want to add:"))
    given_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
    change_qty(-given_water, -given_milk, -given_coffee, -given_cups, 0)
  else:
    print("You are not allowed in here. Please sign up to get a worker id and password.")
def take():
  """Lets the worker take the money"""
  if verify(input("Please give your working username: "), input("Please enter your password:")) == True:
    print("You have been verified, and can now proceed.")
    print(f"I gave you ${money}")
    change_qty(0, 0, 0, 0, -money)
  else:
    print("You are not allowed in here. Please sign up to get a worker id and password.")
while True:
  action = actions()
  if action == "buy":
      buy()
  elif action == "fill":
      fill()
  elif action == "take":
      take()
  elif action == "report":
      print_status()
  elif action == "exit":
      print("Bye! See you soon!")
      break
  elif action == 'manage':
      verify_manager(input("Your name: "), input("Your password: "))
  else:
    print("I don't understand.")
