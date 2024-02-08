# Author: Ofek Malul
# Date: 4/12/2023
# Review: Idan

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.firefox.options import Options as FirefoxOptions  

class TestWebsite(unittest.TestCase):
    def setUp(self):
        chrome_options = FirefoxOptions()
        chrome_options.add_argument('--headless') # NO GUI
        chrome_options.add_argument('--disable-dev-shm-usage') # Improve performance
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Firefox(options=chrome_options)

    def test_positive_input(self):
        self.driver.get("http://localhost:9090")
        self.driver.implicitly_wait(1)
        text_box_Xpath = "/html/body/section/form/div/input"
        self.driver.find_element(By.XPATH, text_box_Xpath).send_keys('Miami')
        click_Xpath = "/html/body/section/form/div/div/button"
        self.driver.find_element(By.XPATH, click_Xpath).click()

        title_element_Xpath = "/html/body/section/div/div/div/div[1]/div/div/div[1]/h2/strong"
        title_element = self.driver.find_element(By.XPATH, title_element_Xpath)
        self.assertEqual("Miami, FL, United States", title_element.text)

    def test_negative(self):
        self.driver.get("http://127.0.0.1:9090")
        self.driver.implicitly_wait(1)

        text_box_Xpath = "/html/body/section/form/div/input"
        self.driver.find_element(By.XPATH, text_box_Xpath).send_keys('0000000000')
        click_Xpath = "/html/body/section/form/div/div/button"
        self.driver.find_element(By.XPATH, click_Xpath).click()

        title_element_Xpath = "/html/body/div/div/h1"
        title_element = self.driver.find_element(By.XPATH, title_element_Xpath)
        self.assertEqual("Welcome to error page", title_element.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

