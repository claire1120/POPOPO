from selenium.webdriver.common.by import By


class DisplayPage:

    search_button = By.XPATH, "//*[contains(@content-desc,'在设置中搜索')]"
    search_edit_text = By.ID, "android:id/search_src_text"
    back_button = By.XPATH, "//*[contains(@content-desc,'向上导航')]"

    def __init__(self, driver):
        self.driver = driver
    def find_element(self,loc):
        return self.driver.find_element(loc[0], loc[1])

    def click_search(self):
        search_button = By.XPATH, "//*[contains(@content-desc,'在设置中搜索')]"
        self.find_element(search_button).click()

    def input_text(self, text):
        self.find_element(self.search_edit_text).send_keys(text)

    def click_back(self):
        self.find_element(self.back_button).click()





