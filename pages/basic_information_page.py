import allure
from pages.basePage import BasePage

"""
This file contains the basic information page
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("basic information page")
class BasicInformationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__month = page.locator("//select[@id='month']")
        self.__day = page.locator("//input[@name='day']")
        self.__year = page.locator("//input[@name='year']")
        self.__gender = page.locator("//select[@id='gender']")
        self.__nextBTN = page.locator("#birthdaygenderNext")

    @allure.step("fill the month and day and year")
    def fill_month_day_year_gender(self, day: str, year: str) -> None:
        self.wait_for_element_to_be_visible_locator(self.__month)
        self.__month.select_option(value='12')
        self.type(self.__day, day)
        self.type(self.__year, year)
        self.__gender.select_option(value='1')
        self.__nextBTN.click()
