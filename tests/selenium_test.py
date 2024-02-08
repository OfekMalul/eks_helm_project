# Author: Ofek Malul
# Date: 4/12/2023
# Review: Idan

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest


class TestWebsite(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless') # NO GUI
        chrome_options.add_argument('--disable-dev-shm-usage') # Improve performance
        service = Service(executable_path='/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def test_positive_input(self):
        self.driver.get("http://localhost:9090")
        self.driver.implicitly_wait(1)
        text_box = self.driver.find_element(by=By.NAME, value="cityName")
        submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="button")

        text_box.send_keys("Miami")
        submit_button.click()

        title_element = self.driver.find_element(by=By.CSS_SELECTOR, value="h2")
        self.assertEqual("Miami, FL, United States", title_element.text)

    def test_negative(self):
        self.driver.get("http://127.0.0.1:9090")
        self.driver.implicitly_wait(1)
        text_box = self.driver.find_element(by=By.NAME, value="cityName")
        submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="button")

        text_box.send_keys("0000000000")
        submit_button.click()

        title_element = self.driver.find_element(by=By.CSS_SELECTOR, value="h1")
        self.assertEqual("Welcome to error page", title_element.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

