import smtplib
from main import city
import requests
url_sheets = 'https://api.sheety.co/a84469e42be5cba1039cd8534bcbb833/users/sheet1'
class NotificationManager:
    def __init__(self,price,name):
        connection = smtplib.SMTP('mail@mail.com')
        connection.starttls()
        connection.login(user='your_email',password='your_password')
        connection.sendmail(from_addr='your_email',to_addrs='your_email',msg=f'Subject:{name} to {city} \n\nFound lowest price to travel at just {price}')
        connection.close()
        self.flight_club_users(price,name)
    def flight_club_users(self,price,name):
        response = requests.get(url=url_sheets)
        for email in response.json()['sheet1']:
            connection = smtplib.SMTP('mail@mail.com')
            connection.starttls()
            connection.login(user='your_email',password='your_password')
            connection.sendmail(from_addr='your_email',to_addrs=email['email'],msg=f'Subject:{name} to {city} \n\nFound lowest price to travel at just {price}')
            connection.close()



