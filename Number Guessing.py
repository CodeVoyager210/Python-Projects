import random
import os

def game(atp):
    while atp > 0:
        print(f'You have {atp} attempts remaining to guess the number.')
        while True:
            try:
                guess = int(input('Make a guess: '))
                if guess > 100 or guess < 0:
                    print('Please enter a number between 1 and 100')
                    continue
            except ValueError:
                print('Please enter a number')
                continue
            break
        if guess == number:
            print(f"Bravo you've got it right it was {number}!")
            break
        elif guess > number:
            atp -= 1
            print('To high.')
            if atp != 0:
                print('Guess again')
            else:
                print(f'You lost! The number was {number}')
        else:
            atp -= 1
            print('To low.')
            if atp != 0:
                print('Guess again')
            else:
                print(f'You lost! The number was {number}')


print('Welcome to the Number Guessing Game!')
number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
while True:
    inner_loop = True
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = 10
        game(attempts)
    elif difficulty == 'hard':
        attempts = 5
        game(attempts)
    else:
        print("Please enter 'easy' or 'hard'")
        continue
    while True:
        print("Do you want to play again? Type 'yes' or 'no'")
        yes_no = input()
        if yes_no == 'yes':
            os.system('cls')
            inner_loop = False
            break
        elif yes_no == 'no':
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'")
    if not inner_loop:
        continue
    break
input('Press enter to close the game')

