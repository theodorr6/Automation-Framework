from autoframework.poms.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CONFIRM_LOGIN = "//h1[contains(text(),'Logged')]"

    def get_presence_of_confirm_message(self):
        """Verify the successful login message after login."""
        return self.get_presence_of_element(self.CONFIRM_LOGIN)