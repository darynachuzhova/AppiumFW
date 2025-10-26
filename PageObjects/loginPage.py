from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.backButton = "BackButton"
        self.viewsButton = "ViewsButton"

    def selectBackButton(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.backButton).click()

    def selecviewButton(self):
        self.driver.find_element(AppiumBy.XPATH,'(//XCUIElementTypeOther[@name="Views"])[2]').click()



