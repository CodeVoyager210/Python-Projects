import random


def game_code(choice, player):
    if choice == 0:
        print(f'{player} chose rock')
    elif choice == 1:
        print(f'{player} chose paper')
    else:
        print(f'{player} chose scissors')


print('Welcome to Rock Paper Scissors!')
print('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors')
while True:
    outer_while = True
    try:
        user = int(input())
        if user > 2 or user < 1:
            print('Please enter a number between 0 and 2')
            continue
    except ValueError:
        print('Please enter a number 0, 1 or 2')
        continue
    game_code(user, 'You')
    computer_game = random.randint(0, 2)
    game_code(computer_game, 'Computer')
    if user == computer_game:
        print('It\'s a tie')
    elif user == 0 and computer_game == 1 or user == 1 and computer_game == 2 or user == 2 and computer_game == 0:
        print('Computer wins')
    else:
        print('You win')
    print('Do you want to play again? Type yes or no')
    while True:
        yes_no = input()
        if yes_no == 'yes' or yes_no == 'Yes':
            outer_while = False
            break
        elif yes_no == 'no' or yes_no == 'No':
            print('Exiting...')
            break
        else:
            print('Please enter yes or no')
            continue
    if not outer_while:
        print('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors')
        continue
    break
input('Press Enter to close')
