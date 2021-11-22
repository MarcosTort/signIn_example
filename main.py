import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui
import time as t
import links
import ids
import data
import front
import cons
choice = front.ShowOptions()

# start navigator for each group of data

for info in range(cons.iterations):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    # driver.maximize_window()

    # search for the target
    driver.get(links.urls.signUp)
    # locate all the elements and send data
    driver.find_element(By.ID, ids.keys.CompanyName).send_keys(choice[info].CompanyName)
    driver.find_element(By.ID, ids.keys.FirstName).send_keys(choice[info].FirstName)
    driver.find_element(By.ID, ids.keys.LastName).send_keys(choice[info].LastName)
    driver.find_element(By.ID, ids.keys.Email).send_keys(choice[info].Email)
    driver.find_element(By.ID, ids.keys.Pass).send_keys(choice[info].Pass)
    driver.find_element(By.ID, ids.keys.CPass).send_keys(choice[info].CPass)
    driver.find_element(By.ID, ids.keys.Country).send_keys(choice[info].Country)

    # user must solve the captcha and confirm

    t.sleep(1)

