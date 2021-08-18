from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os

working_dir = os.getcwd()
driver = webdriver.Firefox(executable_path=working_dir + '\geckodriver.exe')


def go_to_url(url):
    driver.get(url)

def click_button(button_id):
    button = driver.find_element_by_id(button_id)
    button.click()

def insert_query_to_box(query, box):
    input_element = driver.find_element_by_name(box)
    input_element.send_keys(query)
    return input_element

def press_enter(input_element):
    input_element.send_keys(Keys.ENTER)

def get_links_list(links_to_scrape):
    content = driver.find_elements_by_css_selector(links_to_scrape)
    links = [element.get_attribute('href') for element in content]
    return links

def get_text_in_link(link):
    go_to_url(link)
    html_text = requests.get(link).text
    return html_text

def apply_beautifulsoup(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    return soup.prettify()

def write_to_file(filename, soup_text):
    with open(filename, 'w') as outfile:
        outfile.write(soup_text)
