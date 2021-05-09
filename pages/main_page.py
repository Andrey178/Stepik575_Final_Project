from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        # login_link = self.browser.find_element(By.CSS_SELECTOR, "#registration_link")
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.should_be_login_page()

    def should_be_login_link(self):
        # assert self.browser.find_element(By.CSS_SELECTOR, "#registration_link"), \
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
             "Login link is not presented"
