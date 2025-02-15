import unittest
import chromedriver_autoinstaller_fix


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestApp(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        chromedriver_autoinstaller_fix.install()  
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://localhost:5000')

    def test_add_delete(self):

        self.driver.find_element(By.NAME, "item").click()
        self.driver.find_element(By.NAME, "item").send_keys("AddItem")
        self.driver.find_element(By.NAME, "item").send_keys(Keys.ENTER)

        self.driver.find_element(By.NAME, "new_item").click()
        self.driver.find_element(By.NAME, "new_item").send_keys("UpdateItem")
        self.driver.find_element(By.NAME, "new_item").send_keys(Keys.ENTER)
        
        self.driver.find_element(By.LINK_TEXT, "Delete").click()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()