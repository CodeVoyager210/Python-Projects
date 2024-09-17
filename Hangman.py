from random_word import RandomWords


def hangedman(hangman):
    graphic = [
        """
            +-------+
            |
            |
            | 
            |
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            | 
            |
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            |       |
            |
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            |      -|
            |
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      /
            |
         ==============
        """
        ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      / \\
            |
         ==============
        """]
    print(graphic[hangman])


while True:
    inner_loop = True
    print('Welcome to Hangman')
    r = RandomWords()
    random_word = r.get_random_word()
    lives = 6
    hanged = 0
    hidden_word = ['_'] * len(random_word)
    while lives > 0:
        print('Word to guess:', ''.join(hidden_word))
        while True:
            guess = input('Guess a letter: ')
            if guess.isdigit():
                print('Please enter a letter')
                continue
            if len(guess) != 1:
                print('Please enter a single letter')
                continue
            break
        if guess in random_word:
            for i, letter in enumerate(random_word):
                if guess == letter:
                    hidden_word[i] = guess
            hangedman(hanged)
            print(f'******************{lives}/6 LIVES LEFT******************')
        else:
            print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
            lives -= 1
            hanged += 1
            hangedman(hanged)
            print(f'******************{lives}/6 LIVES LEFT******************')
        if '_' not in ''.join(hidden_word):
            print('You won. Congratulations!')
            break
    if lives == 0:
        print('Game over')
    print('Thanks for playing!. Do you want to play again ? yes or no')
    while True:
        yes_no2 = input()
        if yes_no2 == 'yes' or yes_no2 == 'Yes' or yes_no2 == 'y':
            inner_loop = False
            break
        elif yes_no2 == 'no' or yes_no2 == 'No' or yes_no2 == 'n':
            break
        else:
            print('Please enter yes or no')
    if not inner_loop:
        continue
    break
input('Press enter to close the game')

