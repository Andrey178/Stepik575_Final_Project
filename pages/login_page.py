from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    # def should_be_login_page(self):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        print("CURRENT PAGE", self.browser.current_url, "!!!")
        assert self.browser.current_url.endswith(LoginPageLocators.LOGIN_URL), "Current page is not login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form_exists = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        # assert True
        assert login_form_exists, "There is no login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        register_form_exists = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        # assert True
        assert register_form_exists, "There is no register form"
