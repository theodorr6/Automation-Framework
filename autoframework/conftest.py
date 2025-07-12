import pytest
from selenium import webdriver
import os
from autoframework import env

@pytest.fixture(scope="class")
def init_driver(request):
    browsers = ['chrome', 'headlesschrome', 'firefox']

    browser = os.environ.get('BROWSER')
    print(f"BROWSER environment variable: {browser}")
    if not browser:
        raise Exception("Please select a browser!")

    browser = browser.lower()
    if browser not in browsers:
        raise Exception(f"Provided browser '{browser}' is not supported!"
                        f"Support browsers: {browsers}")


    if browser in 'chrome':
        driver = webdriver.Chrome()
    elif browser in 'firefox':
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()