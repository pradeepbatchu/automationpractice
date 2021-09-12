import pytest
from selenium.webdriver import FirefoxProfile
from seleniumrequests import Firefox


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browsers : Chrome or Firefox")
    parser.addoption("--env", default="qa", help="Environments : qa or uat")


@pytest.fixture
def env(request):
    return request.config.getoption("--env")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver_init(request, browser):
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.options import Options

    # if browser(request) == "chrome":
    if browser == "chrome":
        options = Options()
        options.add_argument("--incognito")
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        request.instance.driver = Chrome(executable_path="D:/github/automationpractice/fe/chromedriver.exe", options=options)
        request.instance.driver.maximize_window()
        request.addfinalizer(request.instance.driver.quit)

    # if browser(request) == "firefox":
    if browser == "firefox":
        fp = FirefoxProfile()
        request.instance.driver = Firefox(executable_path="D:/github/automationpractice/fe/geckodriver.exe", firefox_profile=fp)
        request.addfinalizer(request.instance.driver.quit)


@pytest.fixture
def chrome_init():
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.options import Options
    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")
    chrome_opt.add_argument("user-agent=qaauto")
    driver = Chrome(executable_path="../chromedriver.exe", options=chrome_opt)
    yield driver
    driver.quit()


@pytest.fixture
def firefox_init(request):
    from selenium.webdriver import Firefox
    from selenium.webdriver import FirefoxProfile
    fp = FirefoxProfile()
    request.instance.driver = Firefox(executable_path=r'/usr/local/bin/geckodriver', firefox_profile=fp)
    request.addfinalizer(request.instance.driver.quit)
