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

        self.user_name_field = page.locator("input[aria-label='Username']")
        self.__email_option_one = page.locator("#selectionc1")
        self.__email_add_option = page.locator("#selectionc3")
        self.__add_email_field = page.locator("//input[@name='Username']")
        self.__nextBTN = page.locator("#next")
        self._user_is_taken = page.locator("//div[contains(text(), 'That username is taken')]")

    @allure.step("create email address")
    def create_email_address(self, email: str) -> None:
        self.wait_for_timeout(2000)

        if self.user_name_field.count() > 0 and self.user_name_field.is_visible():
            self.type(self.user_name_field, email)
            self.wait_for_timeout(500)
        else:
            self.wait_for_element_to_be_visible_locator(self.__email_option_one)
            self.__email_option_one.first.scroll_into_view_if_needed()
            self.click(self.__email_option_one)

        self.wait_for_element_to_be_visible_locator(self.__nextBTN)
        self.click(self.__nextBTN)

    @allure.step("check custom email availability")
    def check_custom_email_availability(self, email: str) -> bool:
        self.wait_for_timeout(2000)
        if self.user_name_field.count() > 0 and self.user_name_field.is_visible():
            self.type(self.user_name_field, email)
            self.wait_for_timeout(500)
        self.wait_for_element_to_be_visible_locator(self.__nextBTN)
        self.click(self.__nextBTN)
        self.wait_for_element_to_be_visible_locator(self._user_is_taken)
        return self.is_visible(self._user_is_taken)

    @allure.step("validate custom email taken")
    def validate_custom_email_taken(self, email: str) -> bool:
        self.wait_for_element_to_be_visible_locator(self.__email_add_option)
        if self.__email_add_option.is_visible():
            self.__email_option_one.first.scroll_into_view_if_needed()
            self.click(self.__email_add_option)
            self.type(self.__add_email_field, email)
            self.wait_for_timeout(500)
        self.wait_for_element_to_be_visible_locator(self.__nextBTN)
        self.click(self.__nextBTN)
        self.wait_for_element_to_be_visible_locator(self._user_is_taken)
        return self.is_visible(self._user_is_taken)
