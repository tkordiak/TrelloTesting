from selenium.webdriver.common.by import By
from seleniumBoardPage import SeleniumBoardPage


class TrelloHomePage:
    TABLES_LINK = (By.XPATH, "//a[contains(@data-test-id,'home-team-boards-tab')]")
    SELENIUM_BOARD_LINK = (By.XPATH, "//a[contains(@href,'seleniumtest')]")

    def __init__(self, browser):
        self.browser = browser

    def selectTables(self):
        tables_tab = self.browser.find_element(*self.TABLES_LINK)
        tables_tab.click()

    def openSeleniumBoard(self):
        selenium_board_link = self.browser.find_element(*self.SELENIUM_BOARD_LINK).get_attribute('href')
        self.browser.get(selenium_board_link)
        return SeleniumBoardPage(self.browser)
