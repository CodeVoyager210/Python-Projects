import random


def final_hand():
    print(f'f Your final hand:{random_cards_me}, final score: {sum(random_cards_me)}')
    print(f"Computer's final hand:{random_cards_comp}, final score: {sum(random_cards_comp)}")


def your_hand():
    print(f'Your cards: {random_cards_me}, current score: {sum(random_cards_me)}')
    print(f"Computer's first card: {random_cards_comp[0]}")


print('Welcome to Blackjack!')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while True:
    inner_loop = True
    random_cards_me = random.choices(cards, k=2)
    while True:
        random_cards_comp = random.choices(cards, k=random.randint(1, 4))
        if sum(random_cards_comp) > 21:
            continue
        else:
            your_hand()
            break

    if sum(random_cards_me) == 21:
        final_hand()
        print(f'Blackjack. You win!')
    else:
        while True:
            y_n = input("Type 'y' to get another card, or 'n' to pass: ")
            if y_n == 'y':
                random_cards_me.append(random.choice(cards))
                if sum(random_cards_me) < 21:
                    your_hand()
                    continue
                elif sum(random_cards_me) > 21:
                    final_hand()
                    print(f'You went over. You lose')
                    break
            elif y_n == 'n':
                if sum(random_cards_comp) > sum(random_cards_me):
                    final_hand()
                    print(f'You lose')
                    break
                elif sum(random_cards_comp) < sum(random_cards_me):
                    final_hand()
                    print(f'You win!')
                    break
                else:
                    final_hand()
                    print(f"It's a draw!")
                    break
            else:
                print("Please type 'y' or 'n'")
                continue
    print("Do you want to play again? 'y' or 'n'")
    while True:
        yes_no = input()
        if yes_no == 'y':
            inner_loop = False
            break
        elif yes_no == 'n':
            print('Thanks for playing!')
            break
        else:
            print("Please type 'y' or 'n'")
            continue
    if not inner_loop:
        continue
    break
input("Press Enter to close the game")

