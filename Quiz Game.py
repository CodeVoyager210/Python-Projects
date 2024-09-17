import random
import os


class questions:
    def __init__(self, quest, sol):
        self.quest = quest
        self.sol = sol

    def show_question(self):
        global score
        global q
        global stop
        while True:
            t_f = input(f'{q} {self.quest} (True/False)?: ')
            if t_f != 'True' and t_f != 'False':
                print("Please enter 'True' or 'False'")
                continue
            elif t_f == self.sol:
                score += 1
                print('You got it right!')
                print(f'The correct answer was {self.sol}.')
                print(f'Your current score is : {score}/{score}.')
                break
            else:
                print("That's wrong.")
                print(f'The correct answer was: {self.sol}.')
                print(f'Your current score is : {score}/{score + 1}.')
                stop = True
                break


while True:
    inner_loop = False
    score = 0
    num = 0
    stop = False
    real_questions = {
        "A slug's blood is green.": 'True',
        "The loudest animal is the African Elephant.": 'False',
        "Approximately one quarter of human bones are in the feet.": 'True',
        "The total surface area of a human lungs is the size of a football pitch": 'True'
    }
    shuffled = list(real_questions.items())
    random.shuffle(shuffled)
    shuffled_dict = dict(shuffled)
    print('Welcome to the PyQuiz')
    for k, v in shuffled_dict.items():
        num += 1
        q = f'Q.{num}:'
        questions(k, v).show_question()
        if stop:
            print('Sorry, better luck next time')
            break
    if not stop:
        print('You won!')
    while True:
        print("Do you want to play again? 'yes' or 'no'")
        yes_no = input()
        if yes_no == 'yes' or yes_no == 'y':
            inner_loop = True
            os.system('cls')
            break
        elif yes_no == 'no' or yes_no == 'n':
            break
        else:
            print("Please enter 'yes' or 'no'")
            continue
    if inner_loop:
        continue
    print('Thanks for playing!')
    break
input('Press any key to close the game')
