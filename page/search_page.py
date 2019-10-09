import sys, os

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from base.base_action import BaseAction
class SearchPage(BaseAction):
    search_button = By.XPATH, "//*[contains(@content-desc,'在设置中搜索')]"
    search_edit_text = By.ID, "android:id/search_src_text"
    back_button = By.XPATH, "//*[contains(@content-desc,'向上导航')]"

    def click_search(self):
        self.click(self.search_button)

    def input_content(self, text):
        self.input(self.search_edit_text, text)

    def click_back(self):
        self.click(self.back_button)

