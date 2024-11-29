from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.table_helper import TableHelper
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (TimeoutException,
                                        NoSuchElementException)

TABLE_FILTERS_TIMEOUT = 20  # wait 20 seconds to load table content

# The four cameras I expected to see by default.
EXPECTED_CAMERAS_TABLE = [['1', '', 'THUMBNAIL_FOUND', 'Online', 'Yes', 'GS3610', 'Cleveland', 'Favorite', '', ''],
                          ['2', '', 'THUMBNAIL_FOUND', 'Online', 'Yes', 'Bosch Flexidome 5000i', 'North York', 'DEMO',
                           '', ''],
                          ['3', '', 'THUMBNAIL_FOUND', 'Online', 'Yes', 'Hikvision DS-2CD1653G0-IZ', 'Midtown', 'DEMO',
                           '', ''],
                          ['4', '', 'THUMBNAIL_FOUND', 'Online', 'Yes', 'AXIS M3065-V Uplink', 'Cleveland', 'DEMO', '',
                           '']
                          ]


class CamerasPage(BasePage):
    # Element definitions
    TABLE_LOCATOR = (By.XPATH, "//table[@id='table']")
    TABLE_ROWS = (By.XPATH, "//table[@id='table']/tbody/tr")
    TABLE_HEADERS_RELATIVE = (By.XPATH, ".//thead/tr/th")
    TABLE_ROWS_RELATIVE = (By.XPATH, ".//thead/tr")
    TABLE_COLUMNS = (By.XPATH, ".//td")
    TABLE_THUMBNAIL_PREVIEW = (By.XPATH, ".//div/campreview")

    # table elements
    ROW_CHECKBOX = (By.CLASS_NAME, "filter-label custom-checkbox")
    CAMERA_DISPLAY = (By.CLASS_NAME, "camerablock")
    CAMERA_INFO = (By.CLASS_NAME, "font-md caminfo tablecaminfo active  online")
    CAMERA_SETTINGS = (By.CLASS_NAME, "settings")
    CAMERA_THUMBNAILS = (By.XPATH, "//table[@id='table']/tbody//div/campreview")
    CAMERA_NAMES = (By.XPATH, "//table[@id='table']/tbody/tr/td[6]")
    PAGE_MENU_CAMERAS = (By.XPATH, "//div[@class='global-menu']/ul/li[@screen_id='cameras']")

    def get_table(self) -> TableHelper:
        """
        Get a TableHelper instance for the table.
        Used to get content if it has any.
        Used to determine # rows and columns.
        Used to get the headers.
        :return: TableHelper instance
        """
        table_element = (WebDriverWait(self.driver, 40).
                         until(EC.presence_of_element_located(self.TABLE_LOCATOR)))
        table_element = self.find_element(self.TABLE_LOCATOR)
        _ = (WebDriverWait(self.driver, 40).
             until(EC.presence_of_all_elements_located(self.TABLE_ROWS)))
        return TableHelper(table_element)

    def wait_for_table_content_to_load(self):
        # Wait for the table headers and filters to populate.
        # Filter will populate with the contents of the table.
        ret_value = ['']
        timeout = 0
        table_helper = self.get_table()
        while not any(ret_value) and timeout <= TABLE_FILTERS_TIMEOUT:
            headers = table_helper.table.find_elements(*self.TABLE_HEADERS_RELATIVE)
            try:
                ret_value = [header.text for header in headers]
            except AttributeError as ae:
                pass
            sleep(1)
            timeout += 1

    def get_camera_table_elements(self) -> list[list]:
        """ get the WebDriver element items from the table
        return list of WebElements - cells with no element are None.
        """
        rows = self.find_elements(self.TABLE_ROWS)
        data = []
        for row in range(len(rows)):
            cells = rows[row].find_elements(*self.TABLE_COLUMNS)
            row_list = []
            for cell in range(len(cells)):
                if cell == 2:
                    try:
                        _ = cells[cell].find_elements(*self.TABLE_THUMBNAIL_PREVIEW)
                        element = "THUMBNAIL_FOUND"
                    except (TimeoutException, NoSuchElementException):
                        element = "NO_THUMBNAIL_FOUND"
                else:
                    element = cells[cell].text
                row_list.append(element)
            data.append(row_list)
        return data

    def get_camera_thumbnails(self) -> list:
        elements = self.find_elements(self.CAMERA_THUMBNAILS)
        return elements

    def get_camera_names(self) -> list:
        elements = self.find_elements(self.CAMERA_NAMES)
        return [element.text for element in elements]

    @staticmethod
    def validate_cameras_table(cameras_table):
        """ validate the camera table """
        for row in range(len(cameras_table)):
            assert cameras_table[row] == EXPECTED_CAMERAS_TABLE[row]

    @staticmethod
    def validate_table_filters_are_correct(cameras_table,
                                           filters,
                                           expected_filters):
        """
        Validate the table filters match the data displayed in the table.
        :param cameras_table:
        :param filters:
        :param expected_filters:
        :return:
        """
        data_in_filters = []  # columns with filters are True, without filters is False.
        for item in zip(cameras_table[0], filters.values()):  # tuples (actual, list of expected)
            if item[1]:  # if filter list has items then we have a filter.
                # Verify items in the display list.
                assert item[0] in item[1], \
                    f'Verify Failed, expected {item[1]} to contain actual value {item[0]}.'
                data_in_filters.append(True)
            else:
                data_in_filters.append(False)
        assert data_in_filters == expected_filters, \
            f'actual {data_in_filters} expected {expected_filters}'
