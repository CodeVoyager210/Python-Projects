print('Welcome to the brand name generator.')
while True:
    name_city = input("What's the name of the city you grew up in?: ")
    if name_city.isdigit():
        print('Please enter a valid city name.')
        continue
    else:
        pet_name = input("What's your pet's name?: ")
        print('Your band name could be', name_city, pet_name)
        break
input('Press Enter to close')



