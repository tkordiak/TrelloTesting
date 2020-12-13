from selenium import webdriver
from loginPage import LoginPage
import unittest


class TrelloCardTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../../resources/chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_add_comment_to_card_and_move_it_to_done(self):
        loginPage = LoginPage(self.driver)
        loginPage.load()

        selectAppPage = loginPage.login('tkordiak@gmail.com', '12345678')

        trelloHomePage = selectAppPage.selectTrello()
        trelloHomePage.selectTables()

        seleniumBoardPage = trelloHomePage.openSeleniumBoard()
        assert seleniumBoardPage.getCardsAmount() == 2, 'Number of Cards is different than 2'
        assert seleniumBoardPage.cardContainsComments(), 'Cards do not contain comments'
        seleniumBoardPage.addCommentToTheCard()
        seleniumBoardPage.moveCardToDone()

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
