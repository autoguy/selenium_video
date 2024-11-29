from time import sleep
from selenium.webdriver.common.by import By


TABLE_FILTERS_TIMEOUT = 20  # SECONDS timeout for table headers and filters to load


class TableHelper:
    def __init__(self, table_element):
        """
        Initialize with the table WebElement.
        :param table_element: WebElement representing the table
        """
        self.table = table_element

    def get_headers(self):
        """
        Get headers from the table.
        :return: List of header names
        """
        # wait for the filters and table headers to populate.
        ret_value = ['']
        timeout = 0
        while not any(ret_value) and timeout <= TABLE_FILTERS_TIMEOUT:
            headers = self.table.find_elements(By.XPATH, ".//thead/tr/th")
            try:
                ret_value = [header.text for header in headers]
            except AttributeError as ae:
                pass
            sleep(1)
            timeout += 1

        # Create dictionary
        headers_and_filters = {}
        for index in range(len(ret_value)):
            temp = ret_value[index].split('\n')
            header = f'{index}' if temp[0] == '' else temp[0]
            filters = temp[1:]
            headers_and_filters.update({header: filters})
        headers_list = [header.split('\n')[0] for header in ret_value]
        return headers_list, headers_and_filters

    def get_row_count(self):
        """
        Get the number of rows in the table.
        :return: Row count
        """
        rows = self.table.find_elements(By.XPATH, ".//tr")
        return len(rows) - 1  # Subtract 1 for the header row

    def get_column_count(self):
        """
        Get the number of columns in the table.
        :return: Column count
        """
        first_row = self.table.find_element(By.XPATH, ".//tr[2]")  # First data row
        cells = first_row.find_elements(By.XPATH, ".//td")
        return len(cells)

    def get_cell_data(self, row_index, col_index):
        """
        Get data from a specific cell.
        :param row_index: Row index (1-based, excluding headers)
        :param col_index: Column index (1-based)
        :return: Cell text
        """
        cell = self.table.find_element(By.XPATH, f".//tr[{row_index + 1}]/td[{col_index}]")
        return cell.text.strip()

    def get_all_data(self):
        """
        Get all data from the table as a 2D list.
        :return: 2D list of table data
        """
        # rows = self.table.find_elements(By.XPATH, ".//tr[position()>1]")
        rows = self.table.find_elements(By.XPATH, ".//tr")[1:]
        data = []
        for row in rows:
            cells = row.find_elements(By.XPATH, ".//td")
            data.append([cell.text.strip() for cell in cells])
        return data

    def get_all_web_elements(self):
        """
        Get all webdriver selenium elements from the table as a 2D list.
        If cell does not have element leave as None.
        :return: 2D list of table data
        """
        # TODO add the code to get the elements from the table.
        rows = self.table.find_elements(By.XPATH, ".//tr[position()>1]")
        data = []
        for row in rows:
            cells = row.find_elements(By.XPATH, ".//td")
            data.append([cell.text.strip() for cell in cells])
        return data
