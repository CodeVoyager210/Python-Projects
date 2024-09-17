#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from importlib.resources import contents
from os.path import split
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
from pathlib import Path
starting_letter = Path(r'Input\Letters\starting_letter.txt')
invited_names = Path(r'Input\Names\invited_names.txt')
new_letter = Path(r'Output\ReadyToSend')
letter_= ''
names_list = []
with open(invited_names) as names:
    for name in names:
        stripped = name.strip()
        names_list.append(stripped)

with open(starting_letter) as letter:
    letter_ = letter.read()

    for name in names_list:
        changed_letter = letter_.replace('[name]', name)
        with open(new_letter / f'letter_{name}.txt', mode='w') as new:
            new.write(changed_letter)






