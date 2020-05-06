from pages.base_page import BasePage
import random
from random import randint


def random_number():
    """
    Generates random number for alias email account and generate random email
    """
    randm_number = random.randint(0, 100)
    random_email = 'testuser+%s@gmail.com' % randm_number
    return random_email


class UtilityHelperPage(BasePage):
    """
    This page will hold all helper methods
    """
    #
    # def random_number(self):
    #     random_number = random.randint(0, 100)
    #     return random_number

    def random_text(self):
        random_string = ''.join(random.choice(str.lower) for i in range(10))
        random_text = 'Test_%s' % random_string
        return random_text

    def random_email(self):
        """
        Generates random number for alias email account and generate random email
        """
        randm_number = random.randint(0, 100)
        random_email = 'testuser+%s@gmail.com' % randm_number
        return random_email

