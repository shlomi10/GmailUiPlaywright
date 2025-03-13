import allure
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page

from pages.basePage import BasePage

"""
This file contains the main search page, where you can make search
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("main search page")
class Homepage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__gmail_tab = page.locator("a[aria-label='Gmail ']")

    @allure.step("click on gmail")
    def select_gmail_tab(self) -> None:
        expect(self.__gmail_tab).to_be_visible(timeout=5000)
        self.__gmail_tab.click()
