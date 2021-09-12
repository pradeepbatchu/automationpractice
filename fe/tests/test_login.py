import pytest
import fe.conf.functional_params as params
from fe.pages.login_page import Login
from fe.pages.myaccount_page import AccountPage
from fe.pages.home_page import HomePage
import time


@pytest.mark.usefixtures("driver_init")
class TestHomePage(object):

    @pytest.fixture
    def login_fixture(self):
        login = Login(self.driver)
        yield login
        del login

    @pytest.fixture()
    def account_fixture(self):
        account = AccountPage(self.driver)
        yield account
        del account

    @pytest.fixture()
    def home_page_fixture(self):
        home = HomePage(self.driver)
        yield home
        del home

    @pytest.mark.positive
    def test_login_page(self, login_fixture, account_fixture, home_page_fixture, env):
        base_url = params.get_base_url(environment=env)
        self.driver.get(base_url)
        login_fixture.login()
        time.sleep(1)

    @pytest.mark.negative
    def test_sign_in_wrong_pwd(self, login_fixture, env):
        base_url = params.get_base_url(environment=env)
        self.driver.get(base_url)
        login_fixture.wrong_password_login()
        time.sleep(2)

    @pytest.mark.negative
    def test_signup_with_existing_email(self, login_fixture, env):
        base_url = params.get_base_url(environment=env)
        self.driver.get(base_url)
        login_fixture.signup_with_existing_email()
        time.sleep(2)

    @pytest.mark.positive
    def test_signup_new_email(self, login_fixture, env):
        base_url = params.get_base_url(environment=env)
        self.driver.get(base_url)
        login_fixture.signup_user()
        time.sleep(2)

    @pytest.mark.negative
    def test_login_invalid_email(self, login_fixture, env):
        base_url = params.get_base_url(environment=env)
        self.driver.get(base_url)
        login_fixture.login_invalid_email()
        time.sleep(2)

    @pytest.mark.negative
    def test_login_only_email(self, login_fixture, env):
        base_url = params.get_base_url(environment=env)
        self.driver.get(base_url)
        login_fixture.login_only_email()
        time.sleep(2)

    @pytest.mark.negative
    def test_login_only_password(self, login_fixture, env):
        base_url = params.get_base_url(environment=env)
        self.driver.get(base_url)
        login_fixture.login_only_password()
        time.sleep(2)
