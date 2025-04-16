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
    def __init__(self, driver):
        self.driver = driver

    footer = 'body > main > footer'
    digital_in_footer = 'body > main > footer > div.Footer_grid__lfZ34 > svg'

    def find_element(self, locator, locator_type='css'):
        if locator_type == 'css':
            by_type = By.CSS_SELECTOR
        elif locator_type == 'xpath':
            by_type = By.XPATH
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")

        return self.driver.find_element(by_type, locator)

    def visit(self, url):
        self.driver.get(url)

    def exist(self, locator, locator_type='css'):
        try:
            self.find_element(locator, locator_type)
        except NoSuchElementException:
            return False
        return True


def test_footer(browser):
    page = Page(browser)
    page.visit('https://only.digital/')
    assert page.exist(page.footer)
    assert page.exist(page.digital_in_footer)

