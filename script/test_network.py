import sys, os
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.network_page import NetWork


class TestNetwork:

    def setup(self):
        self.driver = init_driver()
        self.network_page = NetWork(self.driver)

    def test_mobile_network_2g(self):
        self.network_page.click_first_network()
        self.network_page.choose_type('2G')

    def test_mobile_network_3g(self):
        self.network_page.click_first_network()
        self.network_page.choose_type('3G')
        
    def test_mobile_network_4g(self):
        self.network_page.click_first_network()
        self.network_page.choose_type('3G')
        
    def test_mobile_network_5g(self):
        self.network_page.click_first_network()
        self.network_page.choose_type('3G')

    def teardown(self):
        self.driver.quit()

