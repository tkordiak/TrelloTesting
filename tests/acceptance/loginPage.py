from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selectAppPage import SelectAppPage


class LoginPage:
    URL = 'https://id.atlassian.com/login'

    USER_NAME_BOX = (By.ID, 'username')
    PASSWORD_BOX = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-submit')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def login(self, username, password):
        username_input = self.browser.find_element(*self.USER_NAME_BOX)
        username_input.send_keys(username + Keys.RETURN)

        password_input = self.browser.find_element(*self.PASSWORD_BOX)

        password_input.send_keys(password)

        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()

        return SelectAppPage(self.browser)


