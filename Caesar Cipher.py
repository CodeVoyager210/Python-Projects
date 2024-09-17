import string


def encode_decode(enc_dec):
    if enc_dec == 'encode':
        message = [mes.lower() for mes in input("Enter message to encrypt: ")]
        shift = int(input("Type the shift number: "))
        for index, char in enumerate(message):
            if char != ' ':
                try:
                    if char.isalpha():
                        message[index] = alphabet[alphabet.index(char) + shift]
                except IndexError:
                    loop_back = (alphabet.index(char) + shift) - 26
                    message[index] = alphabet[loop_back]
        print(''.join(message))
    elif enc_dec == "decode":
        message = [mes.lower() for mes in input("Enter message to decode: ")]
        shift = int(input("Type the shift number: "))
        for index, char in enumerate(message):
            if char.isalpha():
                message[index] = alphabet[alphabet.index(char) - shift]
        print("".join(message))


while True:
    inner_loop = True
    alphabet = [alpha for alpha in string.ascii_lowercase]
    print("Type 'encode' to encrypt, type 'decode' to decrypt")
    while True:
        en_de = input()
        if en_de == 'encode' or en_de == 'decode':
            break
        else:
            print("Please type 'encode' to encrypt, type 'decode' to decrypt")
            continue
    encode_decode(en_de)
    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    while True:
        yes_no = input()
        if yes_no == 'yes' or yes_no == 'Yes' or yes_no == 'y':
            inner_loop = False
            break
        elif yes_no == 'no' or yes_no == 'No' or yes_no == 'n':
            break
        else:
            print("Please type 'yes' if you want to go again. Otherwise type 'no'.")
            continue
    if not inner_loop:
        continue
    break
input('Press enter to close the program')


