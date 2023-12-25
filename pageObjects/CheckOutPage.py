from selenium.webdriver.common.by import By


class CheckOutPage:
    cardTitle = (By.XPATH, "//div[@class='card h-100']")

    def __init__(self,driver):
        self.driver = driver



    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)