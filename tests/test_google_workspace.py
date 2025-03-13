import allure
import pytest

from utils.constants import *

"""
This file contains the main tests
"""


@allure.epic("Functionality")
@allure.feature("title - functionality")
@allure.story("validate the google workspace function")
class TestGoogleWorkspace:

    @pytest.fixture(autouse=True)
    def setup(self, initialize):
        """Initialize driver and page objects before each test"""
        self.page, self.home_page, self.google_workspace_page, self.create_account_page, self.basic_information_page, self.choose_email_address_page= initialize

    @allure.story("validate the google workspace function")
    @allure.description("validate user registration is working")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("validate basic functionality")
    @pytest.mark.flaky(reruns=1)
    def test_create_user_account(self):
        with allure.step("start user registration test"):
            self.page.goto(BASE_URL)
            self.home_page.select_gmail_tab()
            self.google_workspace_page.create_account()
            self.create_account_page.enter_first_and_last_name(FIRST_NAME, LAST_NAME)
            self.basic_information_page.fill_month_day_year_gender(DAY_OF_WEEK, YEAR)
            self.choose_email_address_page.select_first_email_account()
            print()
          #  assert actual_device_name == DEVICE_NAME, f'Google Pixel 9 Pro XL was not at the page, actual device is {actual_device_name}'
