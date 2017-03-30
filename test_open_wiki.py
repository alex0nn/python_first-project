# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_open_wiki(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_open_wiki(self):
        success = True
        wd = self.wd
        wd.get("https://www.google.com.ua/?gfe_rd=cr&ei=qR7dWJCJN4vCsAG3m6-ICg")
        wd.find_element_by_id("lst-ib").click()
        wd.find_element_by_id("lst-ib").clear()
        wd.find_element_by_id("lst-ib").send_keys("wiki")
        wd.find_element_by_id("lst-ib").click()
        wd.find_element_by_id("lst-ib").send_keys("
")
        wd.find_element_by_link_text("Wikipedia").click()
        wd.find_element_by_id("searchInput").click()
        wd.find_element_by_id("searchInput").clear()
        wd.find_element_by_id("searchInput").send_keys("ukraine")
        wd.find_element_by_link_text("Украинастрана в Восточной Европе").click()
        wd.find_element_by_id("mw-content-text").click()
        wd.find_element_by_link_text("УНР").click()
        wd.find_element_by_link_text("2.1 Октябрьская революция").click()
        wd.find_element_by_link_text("Запорожская Сечь").click()
        wd.find_element_by_link_text("2 Начало Запорожской Сечи").click()
        wd.find_element_by_link_text("Хортица").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
