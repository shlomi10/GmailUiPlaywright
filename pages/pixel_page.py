import allure
from playwright.sync_api import expect

from pages.basePage import BasePage

"""
This file contains the pixel 9 pro xl page
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("pixel 9 pro xl page")
class PixelPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__google_pixel_title = page.locator(".specs-phone-name-title")

    @allure.step("validate pixel 9 pro xl in title")
    def get_title_of_device(self) -> str:
        expect(self.__google_pixel_title).to_be_visible(timeout=5000)
        return self.get_text(self.__google_pixel_title)
