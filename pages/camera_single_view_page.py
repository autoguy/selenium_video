from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (TimeoutException,
                                        NoSuchElementException,
                                        StaleElementReferenceException)


class CameraSingleViewPage(BasePage):
    # Element definitions

    # page camera information
    PAGE_CAMERA_NAME = (By.XPATH, "//div[contains(@class, 'header-center')]")

    # page navigation
    BACK_BUTTON = (By.XPATH, "//div[@class='mainbackbtn']")

    # table elements
    # feed activity event table for single view.
    FEED_EVENT_TABLE = (By.XPATH, "//table[contains(@class,'feed-activity-list table')]")
    FEED_EVENT_TABLE_CONTENT = (By.XPATH, "//table[contains(@class,'feed-activity-list table')]/tbody/tr/td")

    # vgs - video player elements
    PLAY_BUTTON_PLAYING = (By.XPATH, "//div[@class='cloudplayer-pause']")
    PLAY_BUTTON_PAUSED = (By.XPATH, "//div[contains(@class,'cloudplayer-pause') "
                                    "and contains(@class,'play')]")

    def get_camera_name(self) -> str:
        """
        Check the single view page contains the camera name we are expecting.
        """
        try:
            return self.find_element(self.PAGE_CAMERA_NAME).text
        except (NoSuchElementException, AttributeError, TimeoutException):
            return ''

    def click_back_button(self) -> None:
        back_button = self.find_elements(self.BACK_BUTTON)
        back_button.click()

    @property
    def back_button_exists(self) -> bool:
        """ Verify the back button exists """
        try:
            self.find_elements(self.BACK_BUTTON)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def is_video_playing(self) -> bool | None:
        """
        Check if the video is playing
        Check if online not sure if needed?
        :return: True if playing, False if paused - None if unknown.
        """
        try:
            self.find_element(self.PLAY_BUTTON_PLAYING)
            return True
        except (NoSuchElementException, TimeoutException):
            try:
                self.find_element(self.PLAY_BUTTON_PAUSED)
                return False
            except (NoSuchElementException, TimeoutException):
                return None

    def wait_for_page_to_load(self) -> None:
        """
        Wait for the page to load, check events table to see if loaded.
        :return: None
        """
        timeout = 0
        while timeout < 5:
            try:
                rows = self.find_elements(self.FEED_EVENT_TABLE_CONTENT)
                _ = [row.text for row in rows]
            except (StaleElementReferenceException,
                    NoSuchElementException, TimeoutException, AttributeError):
                break
            sleep(.5)
            timeout += 1
        return None
