from selenium.webdriver.common.by import By


class NetWork:

    net_button = By.XPATH, "//*[contains(@text,'网络和互联网')]"
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    click_first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.XPATH, "//*[contains(@text,'网络和互联网')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(@text,'移动网络')]").click()

    def click_first_network(self):
        self.driver.find_element(By.XPATH, "//*[contains(@text,'首选网络类型')]").click()

    def choose_type(self, type):
        if type == '3G':
            self.driver.find_element(By.XPATH, "//*[contains(@text,'2G')]").click()
        elif type == '2G':
            self.driver.find_element(By.XPATH, "//*[contains(@text,'3G')]").click()
