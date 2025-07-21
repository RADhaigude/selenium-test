import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Optional: comment this line if you want to see the browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # ✅ Unique temporary user data dir to avoid the session error
    temp_user_data_dir = f"/tmp/chrome-user-data-{os.getpid()}"
    options.add_argument(f"--user-data-dir={temp_user_data_dir}")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

