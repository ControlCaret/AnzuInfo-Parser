from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import json
import csv

def login():
    driver.find_element(By.NAME, "id").send_keys(Data["userId"])
    driver.find_element(By.NAME, "pw").send_keys(Data["userPw"])
    driver.find_element(By.ID,'login').click()

def search(id):
    driver.get("https://anzuinfo.me/myScoreText.html" + "?search_id=" + id + "&ver=6&sort=update_up&filter_level=786432&filter_diff=255&filter_comp=31&filter_grade=1023")

    #level bitmasking
    level = [19, 20]
    bit = 0b00000000000000000000
    for i in level:
        bit |= (1 << i - 1)

    #driver.find_element(By.ID, "search_id").send_keys(id)
    #driver.find_element(By.ID, 'search_button').click()

    #driver.find_element(By.CLASS_NAME, "filter_toggle").click()

    #driver.execute_script("document.getElementsByClassName('filter_sort')[0].style.display = 'block';")

    #driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='update_up']").click()



def main():
    global driver
    driver = webdriver.Chrome()

    global Data
    with open('settings.json') as file:
        Data = json.load(file)

    #todo - replace driver.get to requests.get
    driver.get("https://anzuinfo.me/login.html")

    login()

    for account in Data["accounts"]:
        search(account)


if __name__ == '__main__':
    main()
