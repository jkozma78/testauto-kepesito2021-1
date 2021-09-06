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


URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

# a teszt során felhasznált selector-ok
selectors = {"input_field": "title", "expected_text": 'span'}


@pytest.mark.parametrize("testdata, expected", [("abcd1234", ""), ("teszt233@", "Only a-z and 0-9 characters allewed"),
                                                ("abcd", "Title should be at least 8 characters; you entered 4.")])
def test_TC01(browser, testdata, expected):
    """Három teszteset parametrizálva"""
    browser.get(URL)
    browser.find_element_by_id(selectors["input_field"]).clear()
    browser.find_element_by_id(selectors["input_field"]).send_keys(testdata)
    exp_text = browser.find_element_by_tag_name(selectors["expected_text"]).text
    assert exp_text == expected
