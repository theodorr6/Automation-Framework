from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def access_url(self, url):
        """Access specified URL."""
        self.driver.get(url)


    def click_element(self, locator, timeout=10):
        """CLick on desired element."""
        wait = WebDriverWait(self.driver, timeout)
        # Wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        # Wait for the element to be clickable
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()


    def fill_text(self, locator, text, timeout=10):
        """Type text in field."""
        wait = WebDriverWait(self.driver, timeout)
        # Wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        # Wait for the element to be clickable
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.send_keys(text)


    def get_presence_of_element(self, locator, timeout=10):
        """Get presence of element."""
        wait = WebDriverWait(self.driver, timeout)

        element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

        return element

