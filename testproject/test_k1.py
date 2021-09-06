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


URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

# a teszt során felhasznált selector-ok
selectors = {"input_field_a": "a", "input_field_b": "b", "result_field": "result", 'kalkulacio_button': "submit"}


def input_fields_clear_and_fill(browser, selector, value):
    """az input mezők törlése és kitöltése tesztadattal"""
    browser.find_element_by_id(selector).clear()
    browser.find_element_by_id(selector).send_keys(value)


@pytest.mark.parametrize("a,b,c", [("", "", "")])
def test_TC01(browser, a, b, c):
    """Helyesen jelenik meg az applikáció betöltéskor, minden mező üres"""
    browser.get(URL)
    a_field_text = browser.find_element_by_id(selectors["input_field_a"]).text
    b_field_text = browser.find_element_by_id(selectors["input_field_b"]).text
    c_field_text = browser.find_element_by_id(selectors["result_field"]).text
    assert c_field_text == c and b_field_text == b and a_field_text == a


@pytest.mark.parametrize("a, b, c", [(2, 3, "10")])
def test_TC02(browser, a, b, c):
    """Számítás helyes, megfelelő bemenettel"""
    browser.get(URL)
    input_fields_clear_and_fill(browser, selectors["input_field_a"], a)
    input_fields_clear_and_fill(browser, selectors["input_field_b"], b)
    browser.find_element_by_id(selectors["kalkulacio_button"]).click()
    c_field_text = browser.find_element_by_id(selectors["result_field"]).text
    assert c_field_text == c


@pytest.mark.parametrize("a, b, c", [("", "", "NaN")])
def test_TC03(browser, a, b, c):
    """Üres kitöltés"""
    browser.get(URL)
    input_fields_clear_and_fill(browser, selectors["input_field_a"], a)
    input_fields_clear_and_fill(browser, selectors["input_field_b"], b)
    browser.find_element_by_id(selectors["kalkulacio_button"]).click()
    c_field_text = browser.find_element_by_id(selectors["result_field"]).text
    assert c_field_text == c
