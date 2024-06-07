from menu import MENU
from menu import coin_value
from menu import resources

MONEY = 0


# function to print report
def report(money):
    global MONEY
    print(
        f'Water: {resources["water"]}ml.\n'
        f'Milk: {resources["milk"]}ml.\n'
        f'Coffee:{resources["coffee"]}gr.\n'
        f'Money: ${money}'
    )
    if input("Withdraw money? 'Y' or 'N': ").lower() == "y":
        print(f"${MONEY} withdrawn")
        MONEY = 0
    else:
        return


# function to refill machine:
def refill():
    while True:
        u_input = int(input("Refill what? Type '1' for Water, '2' for Milk, '3' for Coffee: "))
        if u_input < 1 or u_input > 3:
            print("Invalid selection, try again.")
        else:
            break
    amount = int(input("Amount in ml/gr: "))
    if u_input == 1:
        resources["water"] += amount
        return f"Refilled {amount}ml of water."
    elif u_input == 2:
        resources["milk"] += amount
        return f"Refilled {amount}ml of milk."
    else:
        resources["coffee"] += amount
        return f"Refilled {amount}gr of coffee."


# function to make coffee

def coffee_brew(selection):
    cur_selection = MENU[selection]["ingredients"]

    for item in cur_selection:
        if cur_selection[item] > resources[item]:
            return f"Insufficient {item}, please choose something else"

    payment_message = payment_proc(selection)
    if "Insufficient funds" in payment_message:
        return payment_message

    for item in cur_selection:
        resources[item] -= cur_selection[item]

    return f"{selection.capitalize()} is ready ☕! Enjoy!"


# function to handle payment processing:

def payment_proc(selection):
    global MONEY
    sel_price = MENU[selection]["cost"]
    print(f"Selection price: ${sel_price:.2f}")
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * coin_value["quarter"]
    dimes = int(input("How many dimes?: ")) * coin_value["dime"]
    nickles = int(input("How many nickles?: ")) * coin_value["nickle"]
    pennies = int(input("How many pennies?: ")) * coin_value["penny"]
    total_amount = quarters + dimes + nickles + pennies
    change = total_amount - sel_price
    print(f"Total input: ${total_amount:.2f}")
    if total_amount < sel_price:
        return f"Insufficient funds. You need ${sel_price - total_amount:.2f} more."
    else:
        MONEY += sel_price
        return f"Here is your ${change:.2f} in change." if change > 0 else "Exact amount provided."


# define main coffee loop:

def coffee_machine():
    while True:

        user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_selection == "report":
            report(MONEY)
        elif user_selection == "refill":
            refill()
        elif user_selection in MENU:
            print(coffee_brew(user_selection))
        else:
            print("Invalid selection, please try again.")


coffee_machine()
