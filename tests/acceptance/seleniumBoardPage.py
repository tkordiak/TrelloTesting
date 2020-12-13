from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SeleniumBoardPage:
    CARDS = (By.XPATH, "//div[@id='board']/child::div[1]//div[contains(@class, 'cards')]/child::a")
    COMMENTS_ICON = (By.XPATH, "//span[contains(@class,'icon-comment')]")
    CARD_COMMENT_BOX = (By.XPATH, "//div[@class='comment-box']/child::textarea")
    SAVE_COMMENT_BUTTON = (By.XPATH, "//div[@class='comment-box']/child::textarea/following-sibling::div/child::input")
    DONE_LIST = (By.XPATH, "//div[@id='board']/child::div[3]")

    def __init__(self, browser):
        self.browser = browser

    def getCardsAmount(self):
        return len(self.browser.find_elements(*self.CARDS))

    def cardContainsComments(self):
        return bool(self.browser.find_elements(*self.COMMENTS_ICON))

    def addCommentToTheCard(self):
        self._get_comented_card().click()
        card_comment_box = self.browser.find_element(*self.CARD_COMMENT_BOX)
        card_comment_box.send_keys("Commented by automation tool")
        save_comment_button = self.browser.find_element(*self.SAVE_COMMENT_BUTTON)
        save_comment_button.click()
        ActionChains(self.browser).send_keys(Keys.ESCAPE).perform()

    def moveCardToDone(self):
        commented_card = self._get_comented_card()
        done_list = self.browser.find_element(*self.DONE_LIST)
        ActionChains(self.browser).drag_and_drop(commented_card, done_list).perform()



    def _get_comented_card(self):
        ancestor_xpath = "/ancestor::div[contains(@class, 'js-card-details')]"
        commented_card = self.browser.find_elements(By.XPATH, self.COMMENTS_ICON[1] + ancestor_xpath)[0]
        return commented_card
