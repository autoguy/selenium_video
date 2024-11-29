import allure
import pytest
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.cameras_page import CamerasPage
from utils.config_loader import load_config

CONFIG = load_config()
CAMERAS_UNDER_TEST = 4  # number of cameras we expected to see in test.
COLUMNS_IN_CAMERA_LIST_DISPLAY = 10  # number of columns in camera display list.
FILTERED_CAMERAS_LIST_COLS = [False, False, False, True, True, False, True, True, False, False]


@allure.feature("Cameras List Display Validation")
@pytest.mark.cameras_list_display
class TestCamerasListDisplay(BaseTest):
    def test_cameras_list_display(self):
        """
        Verify Camera List on /cameras Page
        Precondition:
            The user is logged in.
        Steps:
            Check that a list of cameras is displayed.
            Verify that each camera has a name, status, and a clickable thumbnail.
        Expected Result:
            All cameras are displayed with appropriate information.
        """
        with allure.step("Navigate to Login Page"):
            self.driver.get(CONFIG['global']['cameras_url'])

        login_page = LoginPage(self.driver)
        with allure.step("Enter Credentials and Login"):
            login_page.login(CONFIG['credentials']['username'],
                             CONFIG['credentials']['password'])

        cameras_page = CamerasPage(self.driver)
        cameras_page.wait_for_table_content_to_load()
        table = cameras_page.get_table()

        with (allure.step("Validate table headers, get header data filters")):
            headers, filters = table.get_headers()
            assert headers == \
                   ['', '', 'Camera', 'Status', 'Recording', 'Name', 'Location', 'Group', 'Action', ''], \
                   f"Unexpected headers: {headers}"

        with allure.step("Validate row and column count"):
            row_count = table.get_row_count()
            col_count = table.get_column_count()
            assert row_count == CAMERAS_UNDER_TEST, \
                f"Unexpected row count: {row_count}"
            assert col_count == COLUMNS_IN_CAMERA_LIST_DISPLAY, \
                f"Unexpected column count: {col_count}"

        with allure.step("Validate table thumbnail, status, name, and location"):
            cameras_table = cameras_page.get_camera_table_elements()
            cameras_page.validate_cameras_table(cameras_table)

        with allure.step("Check the table filters are correct"):
            cameras_page.validate_table_filters_are_correct(cameras_table,
                                                            filters,
                                                            FILTERED_CAMERAS_LIST_COLS)
