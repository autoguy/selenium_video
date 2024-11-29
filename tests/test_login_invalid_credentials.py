import allure
import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utils.config_loader import load_config

CONFIG = load_config()


@allure.feature("Login Tests")
@allure.story("Invalid Login")
@pytest.mark.login
@pytest.mark.order(1)
class TestLoginInvalidCredentials(BaseTest):
    def test_login_invalid_credentials(self):
        """
        Login with Invalid Credentials
        Precondition:
            Navigate to the login page.
        Steps:
            Enter an invalid username or password.
            Click the "Login" button.
        Expected Result:
            The application displays an error message indicating invalid login credentials.
            Does not continue to application
        """
        with allure.step("Navigate to Login Page"):
            self.driver.get(CONFIG['global']['cameras_url'])
        login_page = LoginPage(self.driver)
        with allure.step("Enter invalid credentials and login"):
            login_page.login("sdafas", "sdafas")
        with allure.step("Validate we did not login"):
            assert self.driver.current_url.endswith("cameras")
