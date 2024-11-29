import allure
import pytest
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.cameras_page import CamerasPage
from pages.camera_single_view_page import CameraSingleViewPage
from pages.menu_page import MenuPage
from utils.config_loader import load_config

CONFIG = load_config()


@allure.feature("Single View Back Button")
@pytest.mark.single_view
class TestSingleViewBackButton(BaseTest):
    def test_single_view_back_button(self):
        """
        Verify Back to List Button

        Precondition:
            The user is on a single camera view.
        Steps:
            Click the "Back to List" button.
        Expected Result:
            The application navigates back to the main camera list view.
        """
        with allure.step("Navigate to Login Page"):
            self.driver.get(CONFIG['global']['cameras_url'])

        login_page = LoginPage(self.driver)
        with allure.step("Enter Credentials and Login"):
            login_page.login(CONFIG['credentials']['username'],
                             CONFIG['credentials']['password'])

        cameras_page = CamerasPage(self.driver)
        cameras_page.wait_for_table_content_to_load()
        camera = cameras_page.get_camera_thumbnails()[0]
        expected_camera_name = cameras_page.get_camera_names()[0]
        camera.click()
        single_view = CameraSingleViewPage(self.driver)
        single_view.wait_for_page_to_load()
        assert expected_camera_name == (actual_name := single_view.get_camera_name()), \
            f'expected camera name: {expected_camera_name} but actual name: {actual_name}.'
        assert single_view.is_video_playing(), "The video does not seem to be playing"
        menu = MenuPage(self.driver)
        menu.select_cameras_page_menu()  # select cameras menu to go back.
        cameras_page.wait_for_table_content_to_load()  # wait cameras to load.
