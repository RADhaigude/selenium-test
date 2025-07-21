from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class OrangeHRMLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_login(self):
        driver = self.driver

        # Wait for username field and enter username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        ).send_keys("Admin")

        # Wait for password field and enter password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).send_keys("admin123")

        # Wait for login button and click
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

        # Wait for dashboard element to ensure login success
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )

        print("Login successful")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

