from time import sleep

from numpy.ma.core import inner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,StaleElementReferenceException
while True:
    inner_loop = False
    WEBSITE = 'https://tinder.com'
    EMAIL = 'wanderercosmic69@gmail.com'
    PASSWORD = 'November32@'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(WEBSITE)
    sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, value="a[href='https://tinder.onelink.me/9K8a/3d4abb81']")
    sleep(2)
    login.click()
    sleep(2)
    fb = driver.find_element(By.XPATH,
                             value='//*[@id="o672545042"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
    sleep(2)
    fb.click()
    sleep(2)
    fb_window = driver.window_handles[1]
    driver.switch_to.window(fb_window)
    sleep(2)
    cookies = driver.find_element(By.XPATH,
                                  value='//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]')
    sleep(2)
    cookies.click()
    sleep(2)
    email = driver.find_element(By.ID, value='email')
    email.send_keys(EMAIL)
    password = driver.find_element(By.ID, value='pass')
    password.send_keys(PASSWORD)
    fb_login = driver.find_element(By.ID, value='loginbutton')
    fb_login.click()
    sleep(12)
    cont = driver.find_element(By.CSS_SELECTOR, value='div[role="button"]')
    cont.click()
    main_window = driver.window_handles[0]
    driver.switch_to.window(main_window)
    sleep(6)
    try:
        location = driver.find_element(By.XPATH, value='//*[@id="o672545042"]/div/div[1]/div/div/div[3]/button[1]')
        location.click()
        sleep(1)
        noty = driver.find_element(By.XPATH, value='//*[@id="o672545042"]/div/div[1]/div/div/div[3]/button[2]')
        noty.click()
        sleep(12)
        decline = driver.find_element(By.XPATH,
                                      value='//*[@id="o-1894041178"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div/div[2]')
        while True:
            sleep(1)
            try:
                decline.click()
            except ElementClickInterceptedException:
                sleep(1)
                home_screen = driver.find_element(By.XPATH,value='//*[@id="o672545042"]/div/div[1]/div[2]/button[2]')
                home_screen.click()
            except StaleElementReferenceException:
                driver.quit()
                inner_loop = True
                print('You have run out of matches in your area,Check again later')
                break

    except NoSuchElementException:
        print('Retrying')
        driver.quit()
    if inner_loop :
        break
input('Press any key to close the program')











