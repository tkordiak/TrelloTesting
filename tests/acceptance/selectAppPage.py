from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from trelloHomePage import TrelloHomePage


class SelectAppPage:
    TRELLO_LINK = (By.XPATH, "//a[contains(@href,'trello')]")

    def __init__(self, browser):
        self.browser = browser

    def selectTrello(self):
        trello_button = self.browser.find_element(*self.TRELLO_LINK)
        trello_button.click()
        return TrelloHomePage(self.browser)
