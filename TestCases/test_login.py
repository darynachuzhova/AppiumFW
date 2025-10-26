import pytest
from PageObjects.loginPage import LoginPage

@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_appLaunch(self):
        print("🚀 App is launched successfully")

        lp = LoginPage(self.driver)
        lp.selectBackButton()
        lp.selecviewButton()

        print("✅ Test completed")
