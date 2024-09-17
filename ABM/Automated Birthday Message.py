import smtplib
import datetime
import random
import pandas
import pathlib
birthdays = pandas.read_csv('../../Desktop/Ntinos Projects/ABM/birthdays.csv')
birthdays_dict =birthdays.to_dict(orient='records')
date = datetime.datetime(year=1961,month=11,day=20)
email = 'athanasopoulos.efth@gmail.com'
password = 'cruvewnfzdowacjh'
connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=email,password=password)
birthdays_found = False
for person in birthdays_dict:
    if person['month'] == date.month and person['day'] == date.day:
        birthdays_found = True
        with open(fr'letter_templates\letter_{random.randint(1,3)}.txt') as lt:
            letter = lt.read()
        updated_letter = letter.replace('[NAME]',person['name'])
        connection.sendmail(from_addr=email,to_addrs=person['email'],msg=f'Subject:Hello its your birthday\n\n{updated_letter}')
        connection.close()
if not birthdays_found:
    print('No birthdays were found today')

input('Press any key to close the program')






