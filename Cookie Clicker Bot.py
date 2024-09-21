from selenium import webdriver
from selenium.webdriver.common.by import By
import time
website = 'https://orteil.dashnet.org/experiments/cookie/'
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_option)
driver.get(website)
cookie = driver.find_element(By.ID,value='cookie')
items = driver.find_elements(By.CSS_SELECTOR,value='#store div')
item_ids = [item.get_attribute('id') for item in items]
timeout = time.time() + 5
five_minutes = time.time() + 60*5
while time.time() < five_minutes:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR,value='#store b')
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != '':
                cost = int(element_text.split('-')[1].strip().replace(',', ''))
                item_prices.append(cost)
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        money_element = driver.find_element(By.ID,value='money').text
        if ',' in money_element:
            money_element = money_element.replace(',','')
        cookie_count = int(money_element)
        affordable_upgrades = {}
        for cost,id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        highest_price_affordable = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable]
        driver.find_element(By.ID,value=to_purchase_id).click()
        timeout = time.time() + 5
cookie_per_sec = driver.find_element(By.ID,value='cps').text
print(cookie_per_sec)
input('Press any key to close the program')




