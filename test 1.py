import pytest
from dict import locators
from selenium import webdriver
import time


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome('C:/Python34/Lib/site-packages/selenium/webdriver/common/chromedriver')
    return driver

def test_togo(driver):
    driver.get(locators['url'])

def test_enter1(driver):
    driver = webdriver.Chrome('C:/Python34/Lib/site-packages/selenium/webdriver/common/chromedriver')
    driver.get(locators['url'])
    window_before = driver.window_handles[0]
    driver.find_elements_by_css_selector(locators['Шапка']['Войти в шапке'][0])[
        locators['Шапка']['Войти в шапке'][1]].click()
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    driver.close()

def test_enter2(driver):
    window_before = driver.window_handles[0]
    driver.find_elements_by_css_selector(locators['Лендинг']['Войти из тела'][0])[
        locators['Лендинг']['Войти из тела'][1]].click()
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    driver.close()

def test_watch_video(driver):
    driver.find_elements_by_css_selector(locators['Лендинг']['Смотреть видео'][0])[
        locators['Лендинг']['Смотреть видео'][1]].click()
    time.sleep(5)
    driver.find_elements_by_css_selector(locators['Лендинг']['Закрыть видео'][0])[
        locators['Лендинг']['Закрыть видео'][1]].click()
    driver.close()

def test_faq(driver):
    driver.find_elements_by_css_selector(locators['Лендинг']['FAQ-1'][0])[locators['Лендинг']['FAQ-1'][1]].click()
    driver.find_elements_by_css_selector(locators['Лендинг']['FAQ-2'][0])[locators['Лендинг']['FAQ-2'][1]].click()
    driver.find_elements_by_css_selector(locators['Лендинг']['FAQ-3'][0])[locators['Лендинг']['FAQ-3'][1]].click()
    driver.find_elements_by_css_selector(locators['Лендинг']['FAQ-4'][0])[locators['Лендинг']['FAQ-4'][1]].click()
    driver.find_elements_by_css_selector(locators['Лендинг']['FAQ-5'][0])[locators['Лендинг']['FAQ-5'][1]].click()
    driver.close()


