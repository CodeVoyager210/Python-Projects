from numpy.f2py.crackfortran import expectbegin
from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
EMAIL = 'cosmicvoyage123@outlook.com'
PASSWORD = 'G7$dQf!29x@PvLz'
website_login = 'https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3FcurrentJobId%3D3996237508%26f_LF%3Df_AL%26geoId%3D102257491%26keywords%3Dpython%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom&trk=public_jobs_nav-header-signin'
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_option)
driver.get(website_login)
user_name = driver.find_element(By.NAME,'session_key')
user_name.send_keys(EMAIL)
user_password =driver.find_element(By.NAME,'session_password')
user_password.send_keys(PASSWORD)
time.sleep(2)
sign_in = driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()
jobs = driver.find_elements(By.CSS_SELECTOR,value='.job-card-container--clickable')

for click in jobs:
    time.sleep(6)
    click.click()
    save = driver.find_element(By.CSS_SELECTOR,value='.jobs-save-button')
    save.click()
    print('Job saved')
print('All jobs have been saved to your profile!')



