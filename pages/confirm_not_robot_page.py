import allure

from pages.basePage import BasePage

"""
This file contains the google workspace 
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("confirm not robot page page")
class ConfirmNotRobotPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__phone_field = page.locator("[id='phoneNumberId']")
        self.__nextBTN = page.locator("[data-primary-action-label='Next']")

    @allure.step("add mobile number")
    def add_mobile_number(self, phone_number : str) -> None:
        self.type(self.__phone_field, phone_number)
        self.click(self.__nextBTN)