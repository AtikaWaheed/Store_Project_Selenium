import os
from constants import BASE_URL
from .wait_pages import WaitPages
from selenium.common.exceptions import TimeoutException


class MyAccountPage(WaitPages):
    """
    This class will handle all methods in My confirmed account page
    """
    url = os.path.join(BASE_URL, 'controller=my-account')

    def is_browser_on_page(self):
        """
        Make sure browser is on correct page
        """
        try:
            self.wait_for_an_element_to_be_present('.info-account')
        except TimeoutException:
            print('Page is taking much time to load')

    def check_account_name(self):
        """
        Verify correct account register name
        """
        username = self.wait_for_an_element_to_be_present('.account span').text
        return username

    def check_visibility_of_addresses_lists(self, title):
        return self.wait_for_all_elements_to_be_present('.row.addresses-lists li [title="{}}"]'
                                                        .format(title))

    def check_heading_from_address_list(self):
        heading_text = self.wait_for_an_element_to_be_present('h1.page-heading').text
        return heading_text

    def click_on_breadcrumb_account(self):
        """
        Click on My account from breadcrumb
        :return:
        """
        self.wait_for_an_element_to_be_present('.breadcrumb.clearfix > a:nth-child(3)').click()
