import os
from .wait_pages import WaitPages
from constants import BASE_URL, CREATE_ACCOUNT, SUBMIT_ACCOUNT
from selenium.common.exceptions import TimeoutException


class AuthenticationPage(WaitPages):
    """
    This page will cover login scenarios
    """
    url = os.path.join(BASE_URL, 'controller=authentication&back=my-account')

    def is_browser_on_page(self):
        """
        Verify if browser is on correct page
        """
        try:
            self.wait_for_ajax()
            return self.wait_for_an_element_to_be_present(CREATE_ACCOUNT)
        except TimeoutException:
            print('Page is taking much time to load')

    def enter_address_in_email_field(self):
        """
        In email field enter some address to create account
        """
        email = self.random_email()
        email_filed = self.wait_for_an_element_to_be_present('#email_create')
        email_filed.send_keys(email)
        return email

    def check_error_message(self):
        """
        Check error email field message with empty field
        """
        error_msg_list = []
        error_msg = self.wait_for_all_elements_to_be_present('.alert-danger li')
        for error in error_msg:
            error_msg_list.append(error.text)
        return error_msg_list

        # return error_msg
    def click_create_account(self):
        """
        CLick on create account button
        """
        # from nose.tools import set_trace;set_trace()
        self.wait_for_an_element_to_be_present(CREATE_ACCOUNT).click()
        try:
            self.wait_for_an_element_to_be_present(SUBMIT_ACCOUNT)
            return self.wait_for_an_element_to_be_present('.page-subheading').text
        except:
            pass
