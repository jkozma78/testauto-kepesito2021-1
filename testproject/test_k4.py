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


URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

selectors = {"all_char": '(//p[3])'}

# az összes karakter subsringekbe bontva, majd egyesítve all_stringbe
substring1 = "!"
substring2 = '"'
substring3 = "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
all_string = f'{substring1}{substring2}{substring3}'

# műveleti karakterek
operand = "+-"


@pytest.mark.parametrize("expected", [(all_string)])
def test_TC01(browser, expected):
    """* Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
      * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    browser.get(URL)
    exp_text = browser.find_element_by_xpath(selectors["all_char"]).text
    assert exp_text == expected


def test_TC02(browser):
    """Megjelenik egy érvényes művelet"""
    browser.get(URL)
    a = browser.find_element_by_id("chr").text
    b = browser.find_element_by_id("op").text
    c = browser.find_element_by_id("num").text

    assert a in all_string and b in operand and int(c)


def test_TC03(browser):
    """Üres kitöltés"""
    browser.get(URL)

    a = browser.find_element_by_id("chr").text
    b = browser.find_element_by_id("op").text
    c = int(browser.find_element_by_id("num").text)

    count = 0
    for i in all_string:
        if i == a:
            count = i
            break
        else:
            count = count + 1
    print(eval(f'{count}{b}{c}'))
    assert a == browser.find_element_by_id("result").text
    """meg kell határozni, hogy a megjelent karakter hányadik az össze karakter között a 
    sorban és hozzá kell adni vagy kivonni ebből a számból annyit, amennyi az operandus után van és 
    annyiadik karakter jelenik mega képernyőn"""
