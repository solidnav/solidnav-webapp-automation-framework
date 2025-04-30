import pytest
from utils.driver_factory import create_driver

def test_open_google():
    driver = create_driver()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
