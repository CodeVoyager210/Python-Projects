import smtplib
import requests
sheets_api = 'https://api.sheety.co/a84469e42be5cba1039cd8534bcbb833/users/sheet1'
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
club_email = input('Enter your email: ')
club_email_2 = input('Enter your email again: ')
while True:
    if club_email != club_email_2:
        print('Your email does not match try again')
        club_email = input('Enter your email: ')
        club_email_2 = input('Enter your email again: ')
    else:
        break
#connection = smtplib.SMTP('mail@mail.com')
#connection.starttls()
#connection.login(user='your_email',password='your_password')
#connection.sendmail(from_addr='your_email',to_addrs=club_email,msg='Subject:Congratulations \n\nYou are now a member of the flight club')
data = {
    'sheet1' : {
        'firstName' : first_name,
        'lastName' : last_name,
        'email' : club_email_2
    }
}
response = requests.post(url=sheets_api,json=data)
response_2 = requests.get(url=sheets_api)
print(response_2.json())