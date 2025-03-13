import allure
from pytest_playwright.pytest_playwright import page

from pages.basePage import BasePage

"""
This file contains the create password page
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("create password page")
class CreatePasswordPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__password_field = page.locator("[name='Passwd']")
        self.__confirm_field = page.locator("[name='PasswdAgain']")
        self.__nextBTN = page.locator("[id='createpasswordNext']")

    @allure.step("enter password")
    def create_password(self, password: str, confirm:str) -> None:
        self.type(self.__password_field, password)
        self.type(self.__confirm_field, confirm)
        self.click(self.__nextBTN)
