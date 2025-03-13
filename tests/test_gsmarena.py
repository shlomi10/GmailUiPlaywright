import allure
import pytest

from utils.constants import *

"""
This file contains the main tests
"""


@allure.epic("Functionality")
@allure.feature("title - functionality")
@allure.story("validate the gsm arena function")
class TestGsmArena:

    @pytest.fixture(autouse=True)
    def setup(self, initialize):
        """Initialize driver and page objects before each test"""
        self.home_page, self.google_workspace_page, self.result_page, self.pixel_page, self.page = initialize

    @allure.story("validate the main page function")
    @allure.description("validate if first article is working")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("validate basic functionality")
    @pytest.mark.flaky(reruns=1)
    def test_first_article(self):
        with allure.step("start first article test"):
            self.page.goto(BASE_URL)
            self.home_page.select_gmail_tab()
            self.google_workspace_page.create_account()
            self.result_page.select_the_pixel_device_in_page()
            actual_device_name = self.pixel_page.get_title_of_device()
            assert actual_device_name == DEVICE_NAME, f'Google Pixel 9 Pro XL was not at the page, actual device is {actual_device_name}'
