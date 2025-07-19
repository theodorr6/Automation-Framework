from autoframework.poms.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LOG_IN_BTN = "//a[text()='Log in']"
    SUBMIT_BTN = "//button[text()='Submit']"
    USERNAME_FIELD_REGISTER = "//input[@data-qa='signup-name']"
    PASS_FIELD = "//input[@name='password']"
    EMAIL_REGISTER_FIELD = "//input[@data-qa='signup-email']"
    SIGN_UP_BTN = "//button[@data-qa='signup-button']"
    SIGN_UP_TEXT = "//h2[text()='New User Signup!']"

    def click_submit_button(self):
        """Click submit button."""
        self.click_element(self.SUBMIT_BTN)

    def type_username(self):
        """Type in username."""
        self.fill_text(self.USERNAME_FIELD_REGISTER, "Teo")

    def type_password(self):
        """Type in password"""
        self.fill_text(self.PASS_FIELD, "Password123")

    def type_email(self):
        """Type email in register field."""
        self.fill_text(self.EMAIL_REGISTER_FIELD, "imhunterize@gmail.com")

    def click_sign_up(self):
        """Click on sign up button."""
        self.click_element(self.SIGN_UP_BTN)

    def verify_signup_text(self):
        """Verify signup text visible."""
        self.get_presence_of_element(self.SIGN_UP_TEXT)