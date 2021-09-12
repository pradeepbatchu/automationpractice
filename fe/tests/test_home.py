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
    def test_add_to_cart(self, login_fixture, account_fixture, home_page_fixture, env):
        base_url = params.get_base_url(environment=env)
        self.driver.get(base_url)
        login_fixture.login()
        time.sleep(1)
        account_fixture.return_to_home_page()
        time.sleep(5)
        home_page_fixture.add_product()
        time.sleep(1)
