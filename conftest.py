import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language: ru, en, ...(etc)')


@pytest.fixture(scope="function", autouse=True)
def link():
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    yield link


@pytest.fixture(scope="class")
def browser(request):
    print(request)
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()



