import logging

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from utils.driver_factory import get_driver
from utils.logger import configure_logger


@pytest.fixture(scope="class")
def setup(request):
    from utils.driver_factory import get_driver
    driver: WebDriver = get_driver()
    request.cls.driver = driver
    # Attach the logger to the test classes.
    request.cls.logger = configure_logger(request.node.name)
    yield
    # TODO sign off if the element is found else just quit.from
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to get the report object
    outcome = yield
    report = outcome.get_result()
    # Attach a screenshot if the test failed
    if report.when == "call" and report.failed:
        driver = item.instance.driver  # Access driver from test instance
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)


def pytest_terminal_summary(terminalreporter, exitstatus):
    """
    Print a custom summary after all tests have run.
    """
    print("\nCustom Test Summary:")
    print(f"Total tests run: {terminalreporter.stats.get('passed', 0) + terminalreporter.stats.get('failed', 0)}")
    print(f"Passed tests: {len(terminalreporter.stats.get('passed', []) if 'passed' in terminalreporter.stats else [])}")
    print(f"Failed tests: {len(terminalreporter.stats.get('failed', []) if 'failed' in terminalreporter.stats else [])}")

