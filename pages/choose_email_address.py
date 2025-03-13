import allure
from pytest_playwright.pytest_playwright import page

from pages.basePage import BasePage

"""
This file contains the choose email address page
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("choose email address page")
class ChooseEmailAddress(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__email_options = page.locator("[role='radio']")
        self.__email_btn = "[role='radio']"
        self.__nextBTN = page.locator("#next")

    @allure.step("select first email address")
    def select_first_email_account(self) -> None:
        self.wait_for_element_to_be_visible(self.__email_btn)
        self.click_on_first_element(self.__email_options )
        self.click(self.__nextBTN)
