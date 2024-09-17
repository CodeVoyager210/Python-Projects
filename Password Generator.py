import random
import string

print('Welcome to the PyPassword Generator')

password = []
inpt = 0


def password_generator(str, len):
    for p in range(len):
        password.append(random.choice(str))


def check(main):
    print(main)
    while True:
        try:
            global inpt
            inpt = int(input())
            break
        except ValueError:
            print('Please enter a number')
            continue


check('How many letters would you like?')
letters = inpt
check('How many symbols would you like?')
symbols = inpt
check('How many numbers would you like?')
numbers = inpt
password_generator(string.ascii_letters, letters)
password_generator(string.digits, numbers)
password_generator(string.punctuation, symbols)
random.shuffle(password)
normal_password = ''.join(password)
print(f'Here is your password :  {normal_password}')
input('Press Enter to close the program')
