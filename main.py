import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import webbrowser
from selenium import webdriver
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from tqdm import notebook
import time


def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def send_message(url):
    driver.get(url)
    time.sleep(2)
    element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]', 40)
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
    msg_box.send_keys('Hello World!')
    time.sleep(2)


def prepare_message(dataframe, name_col, phone_col):
    file = dataframe[[name_col, phone_col]]
    base_msg = 'Hello, {}! I am a bot. '
    base_url = 'https://web.whatsapp.com/send?phone={}&text={}'
    for i, j in notebook.tqdm(file.iterrows()):
        phone_no = j[phone_col]
        name = j[name_col].title()
        msg = urrlib.parse.quote(base_msg.format(name))
        url_msg = base_url.format(phone_no, msg)
        send_message(url_msg)

