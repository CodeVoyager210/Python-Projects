def caclulator(fnum, snum, op):
    calc = f'{fnum} {op} {snum}'
    global previous_number
    previous_number = eval(calc)
    print(f'{fnum} {op} {snum} = {eval(calc)}')


while True:
    previous_number = 0
    inner_loop2 = True
    while True:
        try:
            first_number = float(input('Whats the first number?: '))
        except ValueError:
            print('Please enter a number')
            continue
        break
    while True:
        inner_loop = True
        print('+')
        print('-')
        print('*')
        print('/')
        operation = input('Pick an operation: ')
        while True:
            try:
                second_number = float(input('Whats the second number?: '))
            except ValueError:
                print('Please enter a number')
                continue
            break
        caclulator(first_number, second_number, operation)
        print(f"Type 'y' to continue calculating with {previous_number}, or type 'n' to start a new calculation or type 'q' to quit")
        while True:
            yes_no_q = input()
            if yes_no_q == 'y':
                inner_loop = False
                first_number = previous_number
                break
            elif yes_no_q == 'n':
                inner_loop2 = False
                break
            elif yes_no_q == 'q':
                break
            else:
                print("Please enter 'y' or 'n' or 'q'")
        if not inner_loop:
            continue
        break
    if not inner_loop2:
        continue
    break
input('Press enter to close the program')
