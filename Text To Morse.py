import string
morse_codes = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..',
               '-----','.----','..--','...--','....-','.....','-....','--...','---..','----.']
text_morse = []
alphabet_num = string.ascii_lowercase + string.digits

while True:
    inner_loop = False
    text_input = input('Enter a text to translate to morse : ')
    text_input_lower = text_input.lower()
    if text_input_lower != '':
        for letter in text_input_lower:
            if letter in alphabet_num:
                alphabet_idx = alphabet_num.index(letter)
                morse = morse_codes[alphabet_idx]
                text_morse.append(morse)
            else:
                inner_loop = True
                print('Please enter alphabetical letters or numbers')
                break
    else:
        print(f'Please enter  a letter or number')
        continue
    if inner_loop:
        continue
    break
print(f'Here is your morse code : {' '.join(text_morse)}')
input('Press any key to close the program')


