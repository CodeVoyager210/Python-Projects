import os
import re
regexp = re.compile(r'[0-9+()%&*^$@!?\|;`~<>-_]+')
regexempty = re.compile(r'^$')
regexspace = re.compile(r'\s+')
dict = {}
count = 1
print('Welcome to the secret auction program.')
while True:
    inner_loop = True
    while True:
        name = input('What is your name?: ')
        if regexp.search(name) or regexempty.search(name) or regexspace.search(name):
            print('Please enter a valid name.')
            continue
        break
    while True:
        try:
            bid = int(input('What is your bid?: $ '))
        except ValueError:
            print('Please enter a number.')
            continue
        break
    dict[name] = bid
    print("Are there any bidders? Type 'yes' or 'no'.")
    while True:
        yes_no = input()
        if yes_no == 'yes' or yes_no == 'Yes' or yes_no == 'y':
            inner_loop = False
            os.system('cls')
            break
        elif yes_no == 'no' or yes_no == 'No' or yes_no == 'n':
            os.system('cls')
            for counting in dict:
                counting = count
                count = counting + 1
            if count > 1:
                print(f'The winner is {max(dict, key=lambda x: dict[x])} with a bid of {max(dict.values())}')
            else:
                print(f'The winner is {''.join(list(x for x in dict))} with a bid of {''.join(list(str(y) for y in dict.values()))}')
            break
        else:
            print('Please enter yes or no.')
    if not inner_loop:
        continue
    break
input('Press Enter to close the program')
