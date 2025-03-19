import os

from dotenv import load_dotenv
from faker import Faker

from pages.choose_email_address import ChooseEmailAddress
from pages.create_password_page import CreatePasswordPage
from pages.google_workspace_page import GoogleWorkspacePage
from pages.basic_information_page import BasicInformationPage
from pages.add_mobile_phone_page import AddMobilePhoneNumber
from pages.create_account_page import CreateAccountPage

dot_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils", ".env"))
load_dotenv(dotenv_path=dot_env_path)

class BaseClass:
    def __init__(self, page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")
        self.name = os.getenv("NAME")
        self.used_email = os.getenv("USED_EMAIL")
        self.shlomi = os.getenv("SHLOMI")
        self.test = os.getenv("TEST")
        self.fake = Faker()
        self.google_workspace_page = GoogleWorkspacePage(self.page)
        self.create_account_page = CreateAccountPage(self.page)
        self.basic_information_page = BasicInformationPage(self.page)
        self.choose_email_address_page = ChooseEmailAddress(self.page)
        self.create_password_page = CreatePasswordPage(self.page)
        self.add_mobile_phone_page = AddMobilePhoneNumber(self.page)
