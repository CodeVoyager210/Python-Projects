from email.headerregistry import Address

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import re
from bs4 import BeautifulSoup
import requests
remove = re.compile(r'[+]')
google_docs = 'https://docs.google.com/forms/d/e/1FAIpQLSfmmHL4GJdw6AOXTA_MYf-Zz31ogv-NBmv2pyhqPp2wsOy6_Q/viewform?usp=sf_link'
zillow = 'https://appbrewery.github.io/Zillow-Clone/'
response = requests.get(url=zillow).text
bs = BeautifulSoup(response,'html.parser')
prices = bs.select('.PropertyCardWrapper')
fixed_prices = [re.sub(remove,'',x.getText().strip()[1:6].replace(',','')) for x in prices]
links = bs.select('.StyledPropertyCardDataArea-anchor')
fixed_links = [x['href'] for x in links]
address = [x.getText().strip() for x in links]
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)
for index in range(len(prices)):
    driver.get(google_docs)
    sleep(2)
    address_prop = driver.find_element(By.XPATH,
                                       value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_prop.send_keys(f'{address[index]}')
    price_prop = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_prop.send_keys(f'${fixed_prices[index]}')
    link_prop = driver.find_element(By.XPATH,
                                    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_prop.send_keys(f'{fixed_links[index]}')
    submit = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    sleep(3)
driver.quit()



