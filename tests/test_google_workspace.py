import allure
import pytest
import random

"""
This file contains the main tests
"""


@allure.epic("Functionality")
@allure.feature("title - functionality")
@allure.story("validate the google workspace function")
class TestGoogleWorkspace:

    @allure.story("validate the google workspace function")
    @allure.description("validate user registration is working")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("validate basic functionality")
    @pytest.mark.flaky(reruns=1)
    def test_create_user_account(self, initialize):
        with allure.step("start user registration test"):
            phone, pwd = self.setup_account_until_password(initialize)
            is_error_title = initialize.create_password_page.create_password(pwd)
            if is_error_title:
                assert is_error_title, "Expected Error title but it wasn't."
                return
            is_phone_valid = initialize.add_mobile_phone_page.add_mobile_number(phone)
            if is_phone_valid:
                assert is_phone_valid, "Expected phone to work but it wasn't."
                return

    def setup_account_until_password(self, initialize):
        day, email, first_name, last_name, pwd, year, phone = self.generate_params(initialize)
        initialize.google_workspace_page.create_account()
        initialize.create_account_page.enter_first_and_last_name(first_name, last_name)
        initialize.basic_information_page.fill_month_day_year_gender(day, year)
        initialize.choose_email_address_page.create_email_address(email)
        return phone, pwd

    def generate_params(self, initialize):
        random_number = random.randint(1000, 9999)
        first_name = initialize.fake.first_name()
        last_name = initialize.fake.last_name()
        pwd = initialize.fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
        email = initialize.fake.user_name() + str(random_number)
        year = str(random.randint(1960, 1985))
        day = str(random.randint(1, 28))
        phone_number = f"+9725{random.choice(['0', '2', '4', '6', '7', '8'])}{random.randint(1000000, 9999999)}"
        return day, email, first_name, last_name, pwd, year, phone_number

    @allure.story("validate the show password button in google workspace function")
    @allure.description("validate the show password button is working")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("validate the show password button")
    @pytest.mark.flaky(reruns=1)
    def test_show_pwd_button(self, initialize):
        with allure.step("start user registration test"):
            self.setup_account_until_password(initialize)
            is_show_pass_worked = initialize.create_password_page.show_password_btn()
            assert is_show_pass_worked, "Expected Show Password Button to work but it wasn't."

    @allure.story("validate create already used account in google workspace function")
    @allure.description("validate used email registration")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("validate create already used account")
    @pytest.mark.flaky(reruns=1)
    def test_create_already_used_account(self, initialize):
        with allure.step("start already used email test"):
            day, email, first_name, last_name, pwd, year, phone = self.generate_params(initialize)
            initialize.google_workspace_page.create_account()
            initialize.create_account_page.enter_first_and_last_name(initialize.name, initialize.name)
            initialize.basic_information_page.fill_month_day_year_gender(day, year)
            is_user_taken = initialize.choose_email_address_page.check_custom_email_availability(initialize.used_email)
            assert is_user_taken, "Expected the username to be taken, but it was not."

    @allure.story("validate create used email from suggestions workspace function")
    @allure.description("validate create used email from suggestions")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("validate basic functionality")
    @pytest.mark.flaky(reruns=1)
    def test_create_used_email_from_suggestions(self, initialize):
        with allure.step("start already used email  from options test"):
            day, email, first_name, last_name, pwd, year, phone = self.generate_params(initialize)
            initialize.google_workspace_page.create_account()
            initialize.create_account_page.enter_first_and_last_name(initialize.shlomi, initialize.test)
            initialize.basic_information_page.fill_month_day_year_gender(day, year)
            is_user_taken = initialize.choose_email_address_page.validate_custom_email_taken(initialize.used_email)
            assert is_user_taken, "Expected the username to be taken, but it was not."
