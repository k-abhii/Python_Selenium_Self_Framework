import pytest
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    print(driver.title)
    print(driver.current_url)
    request.cls.driver = driver
    yield
    driver.close()


