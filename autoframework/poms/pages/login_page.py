from autoframework.poms.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    LOG_IN_BTN = "//a[text()='Log in']"
    SUBMIT_BTN = "//button[text()='Submit']"
    USERNAME_FIELD = "//input[@id='username']"
    PASS_FIELD = "//input[@name='password']"

    def click_submit_button(self):
        """Click submit button."""
        self.click_element(self.SUBMIT_BTN)

    def type_username(self):
        """Type in username."""
        self.fill_text(self.USERNAME_FIELD, "student")

    def type_password(self):
        """Type in password"""
        self.fill_text(self.PASS_FIELD, "Password123")