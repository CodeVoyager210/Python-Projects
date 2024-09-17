

import pandas
import re

nato = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {d['letter']:d['code'] for d in nato.to_dict(orient='records')}
word = input('Enter a word: ')
while True:
    inner_loop = False
    if re.search(r'[0-9]+',word):
        print('Enter a valid word without numbers')
        word  = input()
        continue
    else:
        try:
            nato_word_list = [nato_dict[n] for n in word.upper()]
        except KeyError:
            print('Enter a valid word without spaces')
            word = input()
            continue
    print(nato_word_list)
    print("Do you want to enter another word? Type 'yes' or 'no'")
    while True:
        yes_no = input()
        if yes_no == 'y' or yes_no == 'yes':
            inner_loop = True
            break
        elif yes_no == 'n' or yes_no == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'")
            continue
    if inner_loop:
        word = input('Enter a word: ')
        continue
    break
input('Press any key to close')
