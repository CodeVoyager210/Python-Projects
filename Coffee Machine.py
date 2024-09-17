def coffee_maker(cff, men):
    global water
    global milk
    global coffee
    global money_in_machine_prev
    global money_in_machine
    if money > men[cff]['cost']:
        change = money - men[cff]['cost']
        money_in_machine_prev = men[cff]['cost']
        money_in_machine += money_in_machine_prev
        water -= men[cff]['ingredients']['water']
        milk -= men[cff]['ingredients']['milk']
        coffee -= men[cff]['ingredients']['coffee']
        print(f'Here is ${round(change, 2)} in change')
        print(f'Here is your {cff}. Enjoy!')
    elif money == men[cff]['cost']:
        water -= men[cff]['ingredients']['water']
        milk -= men[cff]['ingredients']['milk']
        coffee -= men[cff]['ingredients']['coffee']
        print(f'Here is your {cff}. Enjoy!')
    else:
        print("Sorry that's not enough money. Money refunded")


water = 300
milk = 200
coffee = 100
money_in_machine_prev = 0
money_in_machine = 0
menu = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'milk': 0,
            'coffee': 18,
        },
        'cost': 1.5
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        }
    }
}
while True:
    money = 0
    espresso_latte_cappuccino = input('What would you like? (espresso/latte/cappuccino): ')
    if espresso_latte_cappuccino == 'report':
        print(f'Water: {water}ml')
        print(f'Milk: {milk}ml')
        print(f'Coffee: {coffee}g')
        print(f'Money in the machine: ${money_in_machine}')
        continue
    elif espresso_latte_cappuccino == 'off':
        print('Shutting down...')
        break
    else:
        if water < menu[espresso_latte_cappuccino]['ingredients']['water']:
            print('Sorry there is not enough water')
            continue
        elif milk < menu[espresso_latte_cappuccino]['ingredients']['milk']:
            print('Sorry there is not enough milk')
            continue
        elif coffee < menu[espresso_latte_cappuccino]['ingredients']['coffee']:
            print('Sorry there is not enough coffee')
            continue
        else:
            print('Please insert coins.')
            quarters = int(input('How many quarters?: '))
            dimes = int(input('How many dimes?: '))
            nickles = int(input('How many nickles?: '))
            pennies = int(input('How many pennies?: '))
            money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    coffee_maker(espresso_latte_cappuccino, menu)
input('Press any key to close the program')


