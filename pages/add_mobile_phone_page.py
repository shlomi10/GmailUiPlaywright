import allure

from pages.basePage import BasePage

"""
This file contains the add mobile phone number page
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("add mobile phone number page")
class AddMobilePhoneNumber(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__phone_field = page.locator("[id='phoneNumberId']")
        self.__nextBTN = page.locator("button:has-text('Next')")
        self.__problem_phone_field = page.locator(
            "//div[contains(text(), 'There was a problem verifying your phone number')]")
        self.__scan_qr_problem = page.locator("//div[contains(text(), 'SMS from Google')]")

    @allure.step("add mobile number")
    def add_mobile_number(self, phone_number: str) -> bool | None:
        self.type(self.__phone_field, phone_number)
        self.click(self.__nextBTN)
        self.page.wait_for_timeout(2000)
        if self.is_visible(self.__problem_phone_field) or self.is_visible(self.__scan_qr_problem):
            return True
        else:
            pass
