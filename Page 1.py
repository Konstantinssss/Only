import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 1000)
    yield driver
    driver.quit()

class Page:
    def __init__(self, browser):
        self.browser = browser
        self.locator = 'body > main > footer'

    def visit(self, url):
        self.browser.get(url)

    def find_element(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

def test_footer(browser):
    page = Page(browser)
    page.visit('https://only.digital/')
    assert page.exist()