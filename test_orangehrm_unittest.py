import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
import time

class OrangeHRMTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--user-data-dir=/tmp/unique-profile")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

    def test_login_logout(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.implicitly_wait(10)

        # Login
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(2)

        self.assertIn("dashboard", driver.current_url.lower())
        print("✅ Login successful")

        # Logout
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[text()='Logout']").click()
        time.sleep(2)

        self.assertIn("auth/login", driver.current_url.lower())
        print("✅ Logout successful")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="reports",
            report_name="OrangeHRMTest"
        )
    )

