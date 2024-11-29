import allure
import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utils.config_loader import load_config

CONFIG = load_config()


@allure.feature("Login Tests")
@allure.story("Valid Login")
@pytest.mark.login
@pytest.mark.order(1)
class TestLoginValidCredentials(BaseTest):
    def test_login_valid_credentials(self):
        """
        Login with Valid Credentials

        Precondition:
            Navigate to the login page.

        Steps:
            Enter the username: demo@vxg.io.
            Enter the password: vxgdemo123.
            Click the "Login" button.
            Expected Result: The user is successfully logged in and redirected to the /cameras page.
        """
        with allure.step("Navigate to Login Page"):
            self.logger.info("Navigate to login page.")
            self.driver.get(CONFIG['global']['cameras_url'])
        login_page = LoginPage(self.driver)
        with allure.step("Enter Credentials and Login"):
            login_page.login(CONFIG['credentials']['username'],
                             CONFIG['credentials']['password'])

        with allure.step("Validate page is loaded successfully"):
            current_url = self.driver.current_url
            assert CONFIG['global']['cameras_url'] in current_url

        with allure.step("Verify successful login by title"):
            assert CONFIG['global']['site_title'] in self.driver.title

