print('Welcome to the tip calculator!')
while True:
    try:
        total_bill = float(input('What was the total bill? '))
        if total_bill == 0 or total_bill == 0.0:
            print('Please enter a number except 0')
            continue
    except ValueError:
        print('Please enter a number')
        continue
    while True:
        try:
            tip = int(input('What perecentage tip would you like to give? 10 ,12 or 15 '))
            if tip == 0:
                print('Please enter a tip except 0')
                continue
            elif tip > 15 or tip <10:
                print('Please enter a tip between 10 ,12 or 15')
                continue
            else:
                break
        except ValueError:
            print('Please enter a number of tip 10 , 12 or 15')
            continue
    while True:
        try:
            split_bill = int(input('How many people would you like to split the bill? '))
            if split_bill == 0:
                print('Please enter a number except 0')
                continue
            else:
                break
        except ValueError:
            print('Please enter a number')
            continue
    calc = (total_bill * tip/100 + total_bill) / split_bill
    print(f'Each person should pay: ${calc:.2f}')
    break
input('Press enter to exit the program')

















