print('Welcome to Treasure Island')
print('Your mission is to find the treasure.')
print("You're at a cross road. Where do you want to go?: ")
print('           Type "left" or "right" ')
while True:
    outer_loop_active = True
    outer_loop_active2 = True
    outer_loop_active3 = True
    left_right = input()
    if left_right == 'left' or left_right == 'Left':
        print("You've found an island in a small lake.")
        print(' Type "wait" to wait for a boat or type "swim" to swim across.')
        while True:
            wait_boat = input()
            if wait_boat == 'wait' or wait_boat == 'Wait':
                print("A boat arrives and it takes you to that island")
                print("Upon that island you encounter three doors a red one a blue one and a yellow")
                print("    Type which door to open")
                while True:
                    door = input()
                    if door == 'yellow' or door == 'Yellow':
                        print("You Win! You've found the treasure")
                        break
                    elif door == 'red' or door == 'Red' or door == 'blue' or door == 'Blue':
                        print('You lost you got eaten by a crocodile, Do you want to try again? Type "yes" or "no"?')
                        while True:
                            yes_no3 = input()
                            if yes_no3 == 'yes' or yes_no3 == 'Yes':
                                outer_loop_active3 = False
                                break
                            elif yes_no3 == 'no' or yes_no3 == 'No':
                                print('Exiting....')
                                break
                            else:
                                print('Please type "yes" or "no"')
                    else:
                        print('Please type "yellow" or "red" or "blue"')
                        continue
                    break
            elif wait_boat == 'swim' or wait_boat == 'Swim':
                print('You got attacked by a shark, Do you want to try again? Type "yes" or "no"')
                while True:
                    yes_no2 = input()
                    if yes_no2 == 'yes' or yes_no2 == 'Yes':
                        outer_loop_active2 = False
                        break
                    elif yes_no2 == 'no' or yes_no2 == 'No':
                        print('Exiting....')
                        break
            else:
                print('Please type "wait" or "swim"')
                continue
            break
    elif left_right == 'right' or left_right == 'Right':
        print('You fell into a pit, Do you want to try again? Type "yes" or "no"')
        while True:
            yes_no = input()
            if yes_no == 'yes' or yes_no == 'Yes':
                outer_loop_active = False
                break
            elif yes_no == 'no' or yes_no == 'No':
                print('Exiting....')
                break
            else:
                print('Please type "yes" or "no"')
    else:
        print('Please type "left" or "right"')
        continue
    if not outer_loop_active2 or not outer_loop_active3 or not outer_loop_active:
        print('Type "left" or "right"')
        continue
    break
input('Press Enter to close')
