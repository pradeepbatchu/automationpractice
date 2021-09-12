from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import fe.common.login as locators
import fe.resources.input_data as input_data
import time
import random

random_number = random.randint(0, 9999999)


class Login(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=15, poll_frequency=0.001)

    # Actions
    def click_on_sign_in(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.sign_in)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.sign_in))
        signin = self.driver.find_element_by_xpath(locators.sign_in)
        signin.click()

    def enter_email_in_to_email_filed(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.email)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.email))
        user = self.driver.find_element_by_xpath(locators.email)
        user.send_keys(input_data.Email)

    def enter_invalid_email_in_to_email_filed(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.email)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.email))
        user = self.driver.find_element_by_xpath(locators.email)
        user.send_keys(input_data.email)

    def enter_password_in_to_password_filed(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.password)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.password))
        user_pwd = self.driver.find_element_by_xpath(locators.password)
        user_pwd.send_keys(input_data.Password)

    def enter_wrong_password_in_to_password_filed(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.password)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.password))
        user_pwd = self.driver.find_element_by_xpath(locators.password)
        user_pwd.send_keys(input_data.honeField)

    def click_login_button(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.submit)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.submit))
        login_btn = self.driver.find_element_by_xpath(locators.submit)
        login_btn.click()

    def enter_email_in_to_email_signup(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_email)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_email))
        user = self.driver.find_element_by_xpath(locators.signup_email)
        user.send_keys(input_data.Email)

    def enter_email_in_to_signup_submit(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_submit)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_submit))
        signup_btn = self.driver.find_element_by_xpath(locators.signup_submit)
        signup_btn.click()
        self.driver.save_screenshot("image.png")

    def enter_sign_in_error(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.login_error)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.login_error))
        signinerror = self.driver.find_element_by_xpath(locators.login_error)
        error = signinerror.text
        print(error)
        assert error == input_data.sign_in_error
        self.driver.save_screenshot("signinerror.png")

    def enter_email_in_to_signup_error(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_error)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_error))
        signuperror = self.driver.find_element_by_xpath(locators.signup_error)
        error = signuperror.text
        print(error)
        assert error == input_data.sign_up_error
        self.driver.save_screenshot("signuperror.png")


    def enter_new_email_in_to_email_signup(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_email)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_email))
        user = self.driver.find_element_by_xpath(locators.signup_email)
        newemail = input_data.email + str(random_number) + "@gmail.com"
        print(newemail)
        user.send_keys(newemail)

    def select_gender(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_gender_male)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_gender_male))
        gender = self.driver.find_element_by_xpath(locators.signup_gender_male)
        gender.click()

    def enter_first_name(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_first_name)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_first_name))
        first_name = self.driver.find_element_by_xpath(locators.signup_first_name)
        first_name.send_keys(input_data.first_name)

    def enter_last_name(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_last_name)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_last_name))
        last_name = self.driver.find_element_by_xpath(locators.signup_last_name)
        last_name.send_keys(input_data.last_name)

    def enter_password(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_pwd)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_pwd))
        pwd = self.driver.find_element_by_xpath(locators.signup_pwd)
        pwd.send_keys(input_data.Password)

    def enter_date_day(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_days)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_days))
        days = Select(self.driver.find_element_by_xpath(locators.signup_days))
        days.select_by_value('1')

    def enter_date_month(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_months)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_months))
        month = Select(self.driver.find_element_by_xpath(locators.signup_months))
        month.select_by_value('1')

    def enter_date_year(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_years)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_years))
        years = Select(self.driver.find_element_by_xpath(locators.signup_years))
        years.select_by_value("1999")

    def enter_address(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_address)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_address))
        address = self.driver.find_element_by_xpath(locators.signup_address)
        address.send_keys(input_data.address)

    def enter_city(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_city)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_city))
        city = self.driver.find_element_by_xpath(locators.signup_city)
        city.send_keys(input_data.city)

    def enter_state(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_state)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_state))
        state = Select(self.driver.find_element_by_xpath(locators.signup_state))
        state.select_by_value("5")

    def enter_zip_code(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_zipcode)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_zipcode))
        zip_code = self.driver.find_element_by_xpath(locators.signup_zipcode)
        zip_code.send_keys(input_data.PostalCodeField)

    def enter_country(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_country)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_country))
        country = Select(self.driver.find_element_by_xpath(locators.signup_country))
        country.select_by_value("21")

    def enter_mobile_phone(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_mobile)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_mobile))
        mobile = self.driver.find_element_by_xpath(locators.signup_mobile)
        mobile.send_keys(input_data.honeField)

    def enter_address_alias(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_alis)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_alis))
        address_alias = self.driver.find_element_by_xpath(locators.signup_alis)
        address_alias.send_keys(input_data.AddressAliasField)

    def enter_submit_register(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.signup_register)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.signup_register))
        register = self.driver.find_element_by_xpath(locators.signup_register)
        register.click()
        self.driver.save_screenshot("image1.png")

    def enter_invalid_error_error(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.login_error)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.login_error))
        signinerror = self.driver.find_element_by_xpath(locators.login_error)
        error = signinerror.text
        print(error)
        assert error == input_data.invalid_email
        self.driver.save_screenshot("invalid_email_error.png")

    def enter_pwd_required_error(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.login_error)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.login_error))
        signinerror = self.driver.find_element_by_xpath(locators.login_error)
        error = signinerror.text
        print(error)
        assert error == input_data.pswd_required
        self.driver.save_screenshot("pwd_error.png")

    def email_required_error(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                locators.login_error)) > 0)

        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(locators.login_error))
        signinerror = self.driver.find_element_by_xpath(locators.login_error)
        error = signinerror.text
        print(error)
        assert error == input_data.email_required
        self.driver.save_screenshot("pwd_error.png")

    # Methods
    def login(self):
        self.click_on_sign_in()
        time.sleep(10)
        self.enter_email_in_to_email_filed()
        self.enter_password_in_to_password_filed()
        self.click_login_button()

    def login_invalid_email(self):
        self.click_on_sign_in()
        time.sleep(10)
        self.enter_invalid_email_in_to_email_filed()
        self.enter_password_in_to_password_filed()
        self.click_login_button()
        time.sleep(3)
        self.enter_invalid_error_error()

    def login_only_email(self):
        self.click_on_sign_in()
        time.sleep(10)
        self.enter_email_in_to_email_filed()
        self.click_login_button()
        time.sleep()
        self.enter_pwd_required_error()

    def login_only_password(self):
        self.click_on_sign_in()
        time.sleep(10)
        self.enter_password_in_to_password_filed()
        self.click_login_button()
        time.sleep(2)
        self.email_required_error()

    def wrong_password_login(self):
        self.click_on_sign_in()
        time.sleep(10)
        self.enter_email_in_to_email_filed()
        self.enter_wrong_password_in_to_password_filed()
        self.click_login_button()
        time.sleep(10)
        self.enter_sign_in_error()

    def signup_with_existing_email(self):
        self.click_on_sign_in()
        time.sleep(10)
        self.enter_email_in_to_email_signup()
        time.sleep(10)
        self.enter_email_in_to_signup_submit()
        time.sleep(10)
        self.enter_email_in_to_signup_error()

    def signup_user(self):
        self.click_on_sign_in()
        time.sleep(10)
        self.enter_new_email_in_to_email_signup()
        time.sleep(5)
        self.enter_email_in_to_signup_submit()
        time.sleep(10)
        self.select_gender()
        self.enter_first_name()
        self.enter_last_name()
        self.enter_password()
        self.enter_date_day()
        self.enter_date_month()
        self.enter_date_year()
        self.enter_address()
        self.enter_city()
        self.enter_state()
        self.enter_zip_code()
        self.enter_country()
        self.enter_mobile_phone()
        self.enter_address_alias()
        self.enter_submit_register()
        time.sleep(5)