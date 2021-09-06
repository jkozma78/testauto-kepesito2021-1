import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def browser():
    """init webbrowser with selenium"""
    options = Options()
    options.add_argument('--head')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(10)
    return driver


URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"


def test_TC01(browser):
    """* Az applikáció helyesen megjelenik:
    * A bingo tábla 25 darab cellát tartalmaz
    * A számlista 75 számot tartalmaz"""
    browser.get(URL)
    num_list = len(browser.find_elements_by_xpath('//ol/li'))
    bingo_cells = len(browser.find_elements_by_xpath('//tbody/tr/td'))
    assert num_list == 75 and bingo_cells == 25


def test_TC02(browser):
    """Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik"""
    browser.get(URL)
    for i in range(75):
        browser.find_element_by_id('spin').click()
        if len(browser.find_elements_by_xpath('//ul/li')) == 1:
            break
