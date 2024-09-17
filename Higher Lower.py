import random
import os


def score_final():
    global score
    score += 1
    os.system('cls')
    print(f"You're right! Current score: {score}.")


data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    }
]
score = 0
print('Welcome to Higher or Lower')
while True:
    inner_loop = True
    inner_loop2 = True
    random_data = random.randint(0, 3)
    print(
        f'Compare A: {data[random_data]['name']}, a {data[random_data]['description']}, from {data[random_data]['country']}')
    while True:
        random_data2 = random.randint(0, 3)
        if random_data2 != random_data:
            print(
                f'Against B: {data[random_data2]['name']}, a {data[random_data2]['description']}, from {data[random_data2]['country']}')
        else:
            continue
        break
    while True:
        inner_loop_followers = True
        more_followers = input("Who has more followers? Type 'A' or 'B': ")
        while True:
            if data[random_data]['follower_count'] > data[random_data2]['follower_count']:
                if more_followers == 'A':
                    inner_loop = False
                    score_final()
                    break
                elif more_followers == 'B':
                    os.system('cls')
                    print(f"Sorry that's wrong. Final score : {score}.")
                    break
                else:
                    inner_loop_followers = False
                    print("Please type 'A' or 'B'")
                    break
            else:
                if more_followers == 'B':
                    inner_loop = False
                    score_final()
                    break
                elif more_followers == 'A':
                    os.system('cls')
                    print(f"Sorry that's wrong. Final score : {score}.")
                    break
                else:
                    inner_loop_followers = False
                    print("Please type 'A' or 'B'")
                    break
        if not inner_loop_followers:
            continue
        break
    if not inner_loop:
        continue
    score = 0
    print("Do you want to play again 'yes' or 'no'")
    while True:
        yes_no = input()
        if yes_no == 'yes' or yes_no == 'y':
            inner_loop2 = False
            os.system('cls')
            break
        elif yes_no == 'no' or yes_no == 'n':
            os.system('cls')
            break
        else:
            print("Please enter 'yes,y' or 'no,n'")
            continue
    if not inner_loop2:
        continue
    break
input('Thanks for playing. Press any key to close the game')
