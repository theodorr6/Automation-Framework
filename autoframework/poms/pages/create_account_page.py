from autoframework.poms.pages.base_page import BasePage

class CreateAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    ACC_INFO_TITLE = "//b[text()='Enter Account Information']"

    def verify_acc_info_title(self):
        """Verify the presence of Account Info Title."""
        return self.get_presence_of_element(self.ACC_INFO_TITLE)