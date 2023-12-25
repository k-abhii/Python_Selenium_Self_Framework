import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name =="chrome":
        service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
    elif browser_name =="firefox":
        service_obj = Service("C:\Program Files (x86)\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "IE":
        service_obj = Service("C:\Program Files (x86)\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    print(driver.title)
    print(driver.current_url)
    request.cls.driver = driver
    yield
    driver.close()


