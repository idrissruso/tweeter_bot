from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


class TweeterBot:

    def __init__(self):
        self.service = Service("D:\Dev\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.up = 100
        self.down = 50

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        cookie = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        cookie.click()
        time.sleep(2)
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(60)
        download = self.driver.find_element(By.XPATH,
                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        download_speed = download.text
        upload = self.driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        upload_speed = upload.text

    def tweet_at_provider(self, tweets):
        self.driver.get("https://twitter.com/")
        time.sleep(3)
        sign_in = self.driver.find_element(By.XPATH,
                                           '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a')
        sign_in.click()
        time.sleep(3)
        user_name = self.driver.find_element(By.XPATH, '//input')
        user_name.send_keys("rusongeka")
        next_p = self.driver.find_element(By.XPATH,
                                          '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_p.click()
        time.sleep(3)
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')

        password.send_keys("Idris@abkar@2014")
        enter = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        enter.click()
        time.sleep(2)

        for t in tweets:
            tweet = self.driver.find_element(By.XPATH,
                                             '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
            tweet.click()
            time.sleep(2)
            msg = self.driver.find_element(By.XPATH,
                                           '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
            msg.send_keys(t)
            send = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
            send.click()
            time.sleep(3)
