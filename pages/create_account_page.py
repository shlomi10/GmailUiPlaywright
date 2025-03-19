import allure

from pages.basePage import BasePage

"""
This file contains the create account page
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("create account page")
class CreateAccountPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__first_name = page.locator("//input[@name='firstName']")
        self.__last_name = page.locator("//input[@name='lastName']")
        self.__nextBTN = page.locator("//div[@id='collectNameNext']")

    @allure.step("enter first name and last name")
    def enter_first_and_last_name(self, first_name: str, last_name: str) -> None:
        self.type(self.__first_name, first_name)
        self.type(self.__last_name, last_name)
        self.click(self.__nextBTN)
