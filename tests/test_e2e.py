import pytest
from  selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
        cards = self.driver.find_element(By.CSS_SELECTOR,"")







