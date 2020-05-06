import os
from .wait_pages import WaitPages
from constants import BASE_URL


class LoginPage(WaitPages):
    """
    This class will cover all login scenarios
    """

    url = os.path.join(BASE_URL, 'controller=authentication&back=my-account')

    def is_browser_on_page(self):
        """
        Verify browser on sign in page
        """
