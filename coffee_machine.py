# This class creates a CoffeeMachine that can be interacted with via command line
class CoffeeMachine:

    money = 550
    water = 400
    milk = 540
    coffee_beans = 120
    cups = 9

    # Creates CoffeeMachine stating with given resources
    def __init__(self, money_start, water_start, milk_start, coffee_beans_start, cups_start):
        self.money = money_start
        self.water = water_start
        self.milk = milk_start
        self.coffee_beans = coffee_beans_start
        self.cups = cups_start

    # This is used to add resources
    def stock(self):
        print(f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee_beans} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money
        """)

    # For user to make purchase selection
    def buy(self):
        choice = input("What do you want to buy? 1 - Espresso, 2 - Latte, 3 - Cappuccino, back - to main menu ")
        if choice == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            else:
                self.use_material(self, 4, 250, 16)
                self.coffee_given(self, "Espresso")
        elif choice == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            else:
                self.use_material(self, 7, 350, 20, 75)
                self.coffee_given(self, "Latte")
        elif choice == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            else:
                self.use_material(self, 6, 200, 12, 100)
                self.coffee_given(self, "Cappuccino")
        elif choice == "back":
            pass
        else:
            print("bad input")

    # To subtract correct amount of resources are a purchase
    def use_material(self, cost, water_used, coffee_beans_used, milk_used=0,):
        self.money += cost
        self.water -= water_used
        self.milk -= milk_used
        self.coffee_beans -= coffee_beans_used
        self.cups -= 1

    # Used to add resources
    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))

    # Used to withdraw monies in machine
    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    # Main user interface and first selection menu for user
    def use_machine(self):
        while True:
            task = input("Would you like to buy, fill, take, remaining, exit: ")
            if task == "buy":
                self.buy(self)
            elif task == "fill":
                self.fill(self)
            elif task == "take":
                self.take_money(self)
            elif task == "remaining":
                self.stock(self)
            elif task == "exit":
                break
            else:
                print("Please enter a valid selection.")

    # Prints out a pleasant message once a purchase is made
    def coffee_given(self, coffee_type):
        print(f"Enjoy your {coffee_type}!")


# creates instance of CoffeeMachine object
coffeeMachine = CoffeeMachine
# starts user interface of object
coffeeMachine.use_machine(coffeeMachine)




