from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Check_Internet_Speed():

    def __init__(self, down, up):
        self.down = down
        self.up = up
        self.chrome_driver = "/Users/floriandreyer/Library/Mobile Documents/com~apple~CloudDocs/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver)

    def get_internet_speed(self):
        # go to speedtest and run test
        self.driver.get(url="https://www.speedtest.net")
        self.accept_button = self.driver.find_element(By.ID, "_evidon-banner-acceptbutton")
        self.accept_button.click()
        time.sleep(1)
        self.start_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        self.start_button.click()
        time.sleep(60)

        # find down and up
        self.download = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.upload = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        #print(f"Down: {self.download}, Up: {self.upload}")

        return [self.download, self.upload]

    def check_internet_speed(self):
        self.up_down = self.get_internet_speed()
        if self.up_down[0] < self.down or self.up_down[1] < self.up:
            print(f"Hello Telekom, why is my download {self.up_down[0]} and my upload {self.up_down[1]} if they are supposed to be {self.down} and {self.up}?")
        else:
            print("Internet speed as promised!")
