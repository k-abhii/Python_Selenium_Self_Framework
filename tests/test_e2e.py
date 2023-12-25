
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
        cards = self.driver.find_elements(By.XPATH,"//div[@class='card h-100']")
        for card in cards:
            productName = card.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                card.find_element(By.XPATH, "div/button").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[class*='validate']").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        successText = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        print(successText)
        assert "Success! Thank you!" in successText

        # Regular Expression XPATH--partial--<a class="nav-link" href="/angularpractice/shop" xpath="1">Shop</a>
        # Regual Expression CSS_SELECTOR   a[href*='shop']
        # driver.find_element(By.XPATH,"//a[contains(@href, 'shop')]").click()
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # //div[@class='card h-100']/div/h4/a



# C:\Users\hp\PycharmProjects\PythonSelfFramework>pytest -v -s
# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.8.2, pytest-7.4.3, pluggy-1.3.0 -- c:\python38\python.exe
# cachedir: .pytest_cache
# metadata: {'Python': '3.8.2', 'Platform': 'Windows-10-10.0.19041-SP0', 'Packages': {'pytest': '7.4.3', 'pluggy': '1.3.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.0.0', 'xdist': '3.5.0'}}
# rootdir: C:\Users\hp\PycharmProjects\PythonSelfFramework
# plugins: html-4.1.1, metadata-3.0.0, xdist-3.5.0
# collected 1 item
#
# tests/test_e2e.py::TestOne::test_e2e
# DevTools listening on ws://127.0.0.1:52800/devtools/browser/afeed4fb-a19c-4278-b6a1-48388cdfd1f6
# ProtoCommerce
# https://rahulshettyacademy.com/angularpractice/
# ×
# Success! Thank you! Your order will be delivered in next few weeks :-).
# PASSED
#
# ========================================================================= 1 passed in 11.76s ==========================================================================










