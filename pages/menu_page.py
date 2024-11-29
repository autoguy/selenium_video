from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MenuPage(BasePage):
    # Element definitions
    PAGE_MENU_CAMERAS = (By.XPATH, "//div[@class='global-menu']/ul/li[@screen_id='cameras']")

    def select_cameras_page_menu(self):
        """ select the camera page left side menu item """
        element = self.find_element(self.PAGE_MENU_CAMERAS)
        element.click()
