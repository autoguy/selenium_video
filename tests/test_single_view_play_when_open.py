import allure
import pytest
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.cameras_page import CamerasPage
from pages.camera_single_view_page import CameraSingleViewPage
from pages.menu_page import MenuPage
from utils.config_loader import load_config

CONFIG = load_config()


@allure.feature("Single View Camera Plays When Open")
@pytest.mark.single_view
class TestSingleViewPlaysAtOpen(BaseTest):
    def test_single_view_play_when_open(self):
        """
        Navigate to Single Camera View

        Precondition:
            The user is logged in and on the /cameras page.
        Steps:
            Click on a camera from the list.
        Expected Result:
            The application navigates to the selected camera’s
            individual view, and the video feed (if available) starts playing.
        """
        with allure.step("Navigate to Login Page"):
            self.driver.get(CONFIG['global']['cameras_url'])

        login_page = LoginPage(self.driver)
        with allure.step("Enter Credentials and Login"):
            login_page.login(CONFIG['credentials']['username'],
                             CONFIG['credentials']['password'])

        cameras_page = CamerasPage(self.driver)
        cameras_page.wait_for_table_content_to_load()
        for camera in cameras_page.get_camera_thumbnails():
            camera.click()
            single_view = CameraSingleViewPage(self.driver)
            single_view.wait_for_page_to_load()
            assert single_view.is_video_playing(), "The video does not seem to be playing"
            menu = MenuPage(self.driver)
            menu.select_cameras_page_menu()  # select cameras menu to go back.
            cameras_page.wait_for_table_content_to_load()  # wait cameras to load.
