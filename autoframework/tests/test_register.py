import pytest

from autoframework.poms.pages.home_page import HomePage
from autoframework.poms.pages.login_page import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestRegister:

    url = 'https://automationexercise.com'

    def test_register_user(self):
        """Verify user can register."""
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        home_page.access_url(self.url)

        home_page.click_consent()
        assert home_page.verify_homepage()

        home_page.click_login_button()

        login_page.type_username()
        login_page.type_email()
        login_page.click_sign_up()
