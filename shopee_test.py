from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests as req
from selenium.webdriver.support import expected_conditions as EC
import time
path = "C:/Users/timbo/OneDrive/桌面/chromedriver.exe"
driver = webdriver.Chrome(path)
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

#-------------test
index = 0
for index in range(6):
    url = 'https://shopee.tw/search?keyword=%E8%80%81%E5%B9%B2%E5%AA%BD%E6%B2%B9%E8%BE%A3%E6%A4%92&page='
    url = url + str(index)
    print(url)
    driver.get(url)
    time.sleep(3)
    prices = driver.find_elements(by=By.CLASS_NAME, value="ZEgDH9")
    #made_from = driver.find_elements(by=By.XPATH, value='//*[@id="main"]/div/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/a/div/div/div[2]/div[1]/div/div')
    # for price in prices:
    #     print(price.text)
    for i in range(60):
        print(prices[i].text)
# for i in range(4):