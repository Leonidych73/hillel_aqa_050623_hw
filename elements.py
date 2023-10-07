from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


def get_site(url: str):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def find_element(driver, by, locator: str):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((by, locator))
        )
    except NoSuchElementException:
        print("element not found")
    return element


def click(element):
    element.click()


def field_input(element, text: str):
    element.clear()
    element.send_keys(text)


def get_text_element(element):
    return element.text
