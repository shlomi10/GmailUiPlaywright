import allure

from pages.basePage import BasePage

"""
This file contains the google workspace 
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("First article page")
class GoogleWorkspacePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__search_field = page.locator("//input[@name='sSearch']")
        self.__create_account_btn = page.locator("[aria-label='Create an account']").nth(2)
        self.__create_personal_account = page.locator("a[aria-label='Gmail - For my personal use']").nth(1)

    @allure.step("select create account")
    def create_account(self) -> None:
        self.__create_account_btn.click()
        self.__create_personal_account.click()