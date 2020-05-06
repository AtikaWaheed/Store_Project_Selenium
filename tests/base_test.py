import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    """
    Base Test Page
    """
    def setUp(self):
        # display = Display(visible=0, size=(1366, 768))
        # display.start()

        # To run on Firefox. Change this to Chrome if needed.
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        """
        Tear Down
        """
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
