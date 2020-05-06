from selenium.common.exceptions import WebDriverException
from constants import BASE_URL


class BasePage(object):
    """
    Base Page
    """
    time_to_wait = 15
    url = BASE_URL

    def __init__(self, driver):
        """
        instantiate driver:
        """
        self.driver = driver

    def visit(self):
        """
        Open URL
        """
        try:
            self.driver.get(self.url)
        except WebDriverException:
            print('Incorrect URL')
