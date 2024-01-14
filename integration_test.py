import unittest
import chromedriver_autoinstaller_fix

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class TestTest1(unittest.TestCase):
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chromedriver_autoinstaller_fix.install()  
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://localhost:5000')
  
    def test_test1(self):
        self.driver.find_element(By.NAME, "item").click()
        self.driver.find_element(By.NAME, "item").send_keys("Item 1")
        self.driver.find_element(By.NAME, "item").send_keys(Keys.ENTER)

        self.driver.find_element(By.NAME, "new_item").click()
        self.driver.find_element(By.NAME, "new_item").send_keys("Hello I am updated")
        self.driver.find_element(By.NAME, "new_item").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Delete").click()

  
    def teardown_method(self, method):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()