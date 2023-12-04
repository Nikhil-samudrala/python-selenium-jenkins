import datetime
import pytest
from selenium import webdriver
import time
import os
from testData.company.add_new_company_data import AddCompanyData
from testData.leaves.leave_test_data import SickLeaveData

driver = None
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = BASE_DIR + '/reports/screen_shots/'


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    BASE_URL = 'https://hrmstest.medplusindia.com/'
    global driver
    # browser_name = request.config.getoption("browser_name")
    driver = webdriver.Chrome("/home/mphs/Downloads/chromedriver-linux64/chromedriver")
    # if browser_name == "chrome":
    #     driver = webdriver.Chrome()
    # elif browser_name == "firefox":
    #     driver = webdriver.Firefox()
    # elif browser_name == "IE":
    #     pass
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.BASE_URL = BASE_URL
    request.cls.BASE_DIR = BASE_DIR
    request.cls.SCREENSHOTS_DIR = SCREENSHOTS_DIR
    request.cls.driver = driver
    yield
    time.sleep(1.5)
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")
            current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = file_name + current_time + '.png'
            take_screenshot(driver, file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % ('../reports/screen_shots/'+file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.save_screenshot(name)


def pytest_configure(config):
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = f"report_{current_time}.html"
    config.option.htmlpath = os.path.join(BASE_DIR +'/reports/', report_name)


def take_screenshot(driver, file_name):
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if file_name.find('.png') == -1:
        file_name += current_time + '.png'
    driver.get_screenshot_as_file(os.path.join(SCREENSHOTS_DIR, file_name))


@pytest.fixture(scope='class', params=AddCompanyData(3).ADD_NEW_COMPANY_DETAILS_RANDOM)
def add_company_data(request):
    yield request.param


@pytest.fixture(scope='class', params=SickLeaveData(3).ADD_LEAVE_DATA)
def add_leave_data(request):
    yield request.param
