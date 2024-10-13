import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("OpenAI")
    search_box.submit()
    assert "OpenAI" in driver.title
