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
        self.__error_heading = page.locator("//div[contains(text(), 'Sorry')]")
        self.__show_pwd = page.locator("//input[@type='checkbox']")
        self.__pwd_field_show = page.locator("//input[@type='password']")

    @allure.step("enter password")
    def create_password(self, password: str) -> bool | None:
        self.type(self.__password_field, password)
        self.page.wait_for_timeout(500)
        self.type(self.__confirm_field, password)
        self.click(self.__nextBTN)
        self.page.wait_for_timeout(1000)
        return self.__error_heading.is_visible()

    @allure.step("show pwd test")
    def show_password_btn(self) -> bool | None:
        self.page.wait_for_timeout(500)
        if self.__pwd_field_show.count() == 2:
            self.click(self.__show_pwd)
            return self.__pwd_field_show.count() == 0
        else:
            return False
