import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def browser():
    """init webbrowser with selenium"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(10)
    return driver


URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"


def test_TC01(browser):
    """Helyesen jelenik meg az applikáció betöltéskor"""
    browser.get(URL)

    c3 = browser.find_element_by_id("testColor").text

    expected_text = '[     ]'
    assert expected_text == c3


def test_TC_02(browser):
    browser.find_element_by_id("start").click()
    browser.find_element_by_id("stop").click()


def test_TC_03(browser):
    browser.find_element_by_id("start").click()
    assert browser.find_element_by_id("result").text != "Correct!"
    if browser.find_element_by_id("randomColorName").text == browser.find_element_by_id("testColorName").text:
        browser.find_element_by_id("stop").click()
        assert browser.find_element_by_id("result").text == "Correct!"
