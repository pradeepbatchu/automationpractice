from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import fe.common.home as home_locators
import time


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=15, poll_frequency=0.001)

    # Actions
    def product_quick_view_link(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(home_locators.product_quick_view)) > 0)
        except TimeoutException:
                raise TimeoutException('Element is: {} is not visible after 15 sec'
                                       .format(home_locators.product1))

        quick_view = self.driver.find_element_by_xpath(home_locators.product1)
        quick_view.click()
        time.sleep(2)
        self.driver.save_screenshot('image.png')

    def switch_to_iframe(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(home_locators.layer)) > 0)
        except TimeoutException:
                raise TimeoutException('Element is: {} is not visible after 15 sec'
                                       .format(home_locators.layer))
        self.driver.switch_to.frame(home_locators.layer)
        time.sleep(2)
        self.driver.save_screenshot('image1.png')

    def add_to_cart(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(home_locators.add_to_cart)) > 0)
        except TimeoutException:
                raise TimeoutException('Element is: {} is not visible after 15 sec'
                                       .format(home_locators.add_to_cart))

        add_cart = self.driver.find_element_by_xpath(home_locators.add_to_cart)
        add_cart.click()
        time.sleep(2)
        self.driver.save_screenshot('image2.png')
        #self.driver.refresh()
        time.sleep(1)

    def add_to_cart_close(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(home_locators.close)) > 0)
        except TimeoutException:
                raise TimeoutException('Element is: {} is not visible after 15 sec'
                                       .format(home_locators.add_to_cart))

        add_cart = self.driver.find_element_by_xpath(home_locators.close)
        add_cart.click()
        time.sleep(2)
        self.driver.save_screenshot('image2.png')
        #self.driver.refresh()
        time.sleep(1)

    def proceed_to_chek_out(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(home_locators.proceed_to_check_out)) > 0)
        except TimeoutException:
            raise TimeoutException('Element is: {} is not visible after 15 sec'
                                   .format(home_locators.proceed_to_check_out))

        chek_out = self.driver.find_element_by_xpath(home_locators.proceed_to_check_out)
        chek_out.click()
        time.sleep(2)
        self.driver.save_screenshot('image3.png')

    def product_click_more_link(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(home_locators.product_more)) > 0)
        except TimeoutException:
                raise TimeoutException('Element is: {} is not visible after 15 sec'
                                       .format(home_locators.product_more))

        quick_view = self.driver.find_element_by_xpath(home_locators.product_more)
        quick_view.click()
        time.sleep(2)
        self.driver.save_screenshot('image.png')

    def navigate_to_cart(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(home_locators.cart_link)) > 0)
        except TimeoutException:
                raise TimeoutException('Element is: {} is not visible after 15 sec'
                                       .format(home_locators.cart_link))

        quick_view = self.driver.find_element_by_xpath(home_locators.cart_link)
        quick_view.click()
        time.sleep(2)
        self.driver.save_screenshot('cart.png')

    def delete_from_cart(self):
        try:
            self.wait.until(lambda driver: len(driver.find_elements_by_xpath(home_locators.remove_link)) > 0)
        except TimeoutException:
                raise TimeoutException('Element is: {} is not visible after 15 sec'
                                       .format(home_locators.remove_link))

        quick_view = self.driver.find_element_by_xpath(home_locators.remove_link)
        quick_view.click()
        time.sleep(2)
        self.driver.save_screenshot('after_removing.png')

   # Methods
    def add_product(self):
        self.product_click_more_link()
        time.sleep(1)
        self.add_to_cart()
        time.sleep(1)
        #self.switch_to_iframe()
        self.add_to_cart_close()
        time.sleep(2)
        self.navigate_to_cart()
        time.sleep(2)
        self.delete_from_cart()
        time.sleep(2)

    # def remove_from_carts(self):
    #     self.navigate_to_cart()
    #     time.sleep(2)
    #     self.delete_from_cart()
    #     time.sleep(2)

