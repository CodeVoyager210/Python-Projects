from idlelib.colorizer import color_config
from traceback import format_exception_only

from idna import valid_label_length
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

EMAIL = 'wanderercosmic69@gmail.com'
PASS = 'November_32@'
website = 'https://instagram.com'
target_profile = 'https://www.instagram.com/chefsteps/'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(website)
sleep(3)
allow_cookies = driver.find_element(By.XPATH,
                                    value='/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
allow_cookies.click()
sleep(3)
email = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(PASS)
sleep(2)
log_in = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
log_in.click()
sleep(4)
driver.get(target_profile)
sleep(4)
followers = driver.find_element(By.CSS_SELECTOR, value='a[href="/chefsteps/followers/"]')
followers.click()
sleep(5)
follow = driver.find_elements(By.CSS_SELECTOR, value='._acan')
while True:
    for add in follow:
        sleep(3)
        try:
            add.click()
            sleep(4)
            try:
                cancel = driver.find_element(By.XPATH,value='/html/body/div[8]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
            except NoSuchElementException:
                try:
                    ok = driver.find_element(By.XPATH,value='/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]')
                except NoSuchElementException:
                    continue
        except ElementClickInterceptedException:
            continue
            if ok:
                sleep(2)
                ok.click()
            elif cancel:
                sleep(2)
                cancel.click()
