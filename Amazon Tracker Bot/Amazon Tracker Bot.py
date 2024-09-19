from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=os.getenv('EMAIL'),password=os.getenv('PASSWORD'))
website = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
while True:
    response = requests.get(url=website, headers={
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        'Accept-Language': "en-US,en;q=0.9"}).text
    soup = BeautifulSoup(response, 'html.parser')
    price = soup.find('span', class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay').getText()
    price_float = float(price.split('$')[1])
    BUY_PRICE = 100
    if price_float < BUY_PRICE:
        connection.sendmail(from_addr=os.getenv('EMAIL'), to_addrs=os.getenv('EMAIL'),
                            msg=f'Subject:Amazon Price Alert \nYour product is at ${price_float} go and check it out! \n{website}')
        connection.close()
        print('Specified Product now is cheaper go check your email')
        break
input('Press any key to close the program')


