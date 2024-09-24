import time
from selenium import webdriver
from selenium.webdriver.common.by import By


WEBSITE = 'https://tinder.com'
EMAIL = 'fabulousontesting@gmail.com'
PASSWORD = 'November_32@'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("user_agent=DN")
driver = webdriver.Chrome(options=chrome_options)
driver.get(WEBSITE)
time.sleep(2)
login = driver.find_element(By.CSS_SELECTOR,value="a[href='https://tinder.onelink.me/9K8a/3d4abb81']")
time.sleep(2)
login.click()
time.sleep(2)
google = driver.find_element(By.CSS_SELECTOR,value='iframe')
time.sleep(2)
google.click()
time.sleep(2)
google_window = driver.window_handles[1]
driver.switch_to.window(google_window)
time.sleep(2)
email = driver.find_element(By.CSS_SELECTOR,value='input')
email.send_keys(EMAIL)





