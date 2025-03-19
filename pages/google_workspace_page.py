import allure

from pages.basePage import BasePage

"""
This file contains the google workspace 
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("google workspace page")
class GoogleWorkspacePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__search_field = page.locator("//input[@name='sSearch']")
        self.__create_account_btn = page.locator(
            ".header__aside .header__aside__button[aria-label='Create an account']")
        self.__create_personal_account = page.locator(".header__aside  a[aria-label='Gmail - For my personal use']")

    @allure.step("select create account")
    def create_account(self) -> None:
        self.__create_account_btn.click()
        self.__create_personal_account.click()
