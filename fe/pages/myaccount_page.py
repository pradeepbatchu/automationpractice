from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import fe.common.myaccount as account_locators
import fe.resources.input_data as input_data
import time


class AccountPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=15, poll_frequency=0.001)

    # Actions
    def click_on_home_page_link(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(
                    account_locators.home_page)) > 0)
        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                       .format(account_locators.home_page))

        home_link = self.driver.find_element_by_xpath(account_locators.home_page)
        home_link.click()
        time.sleep(5)
        pageTitle = self.driver.title
        print(pageTitle)
        #assert pageTitle == 'My Store'

    def return_to_home_page(self):
        self.click_on_home_page_link()