from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import os


driver = webdriver.Firefox(executable_path=os.getcwd() + '\geckodriver.exe')

url = 'https://www.google.com/search?q=How+to+data+engineering'

driver.get(url)
driver.find_element_by_id('L2AGLb').click()

time.sleep(3)

content = driver.find_elements_by_css_selector('.yuRUbf [href]')
links = [el.get_attribute('href') for el in content]

for count, link in enumerate(links):
    if count < 5:
        driver.get(link)
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        filename = "html_{}.html".format(count + 1)
        html_file = open(filename,'w')
        html_file.write(soup.prettify())
        html_file.close()
