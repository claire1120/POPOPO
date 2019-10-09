class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.driver.find_element(loc[0], loc[1]).click()

    def input(self, loc, text):
        self.driver.find_element(loc[0], loc[1]).send_keys(text)