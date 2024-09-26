from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from time import sleep
SPEEDTEST = 'https://www.speedtest.net/'
TWITTER = 'https://x.com/i/flow/login'
EMAIL = 'wanderercosmic69@gmail.com'
PASS = 'November_32@'
class TwitterBot :
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach',True)
        self.driver = webdriver.Chrome(options=chrome_options)
    def speed(self):
        self.driver.get(SPEEDTEST)
        sleep(3)
        accept_all = self.driver.find_element(By.ID,value='onetrust-accept-btn-handler')
        accept_all.click()
        sleep(2)
        go = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        wait = WebDriverWait(self.driver,50)
        while True:
            try:
                result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.result-label')))
            except TimeoutException:
                continue
            self.download = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
            self.upload = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            break
    def twitter(self):
        download = self.download.text
        upload = self.upload.text
        sleep(2)
        self.driver.get(TWITTER)
        sleep(6)
        email = self.driver.find_element(By.CSS_SELECTOR,value='input')
        email.send_keys(EMAIL)
        sleep(1)
        email.send_keys(Keys.ENTER)
        sleep(2)
        password = self.driver.find_element(By.NAME,value='password')
        password.send_keys(PASS)
        password.send_keys(Keys.ENTER)
        sleep(6)
        msg = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')

        msg.send_keys(f'High Score Of The Slowest Internet with a whopping  download speed {download}/Mbps and Upload {upload}/Mbps ')
        sleep(2)
        post = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post.click()






bot = TwitterBot()
bot.speed()
bot.twitter()

