import allure

from pages.basePage import BasePage

"""
This file contains the results page, where you can find results of search
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Result page")
class ResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__google_pixel_result = page.locator("//img[contains(@title, 'Google Pixel 9 Pro XL')]")

    @allure.step("select the pixel device in page")
    def select_the_pixel_device_in_page(self) -> None:
        self.click(self.__google_pixel_result)
