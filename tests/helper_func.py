from .base_test import BaseTest
from pages.landing_page import LandingMainPage
from pages.sign_up_form import SignUpFormPage
from pages.authentication import AuthenticationPage
from pages.utility_page import UtilityHelperPage
from constants import PERSONAL_INFO
from tests.static_func import get_registration_fields
from pages.confirmed_account_page import MyAccountPage
from constants import MAIN_HEADING_LIST, TITLE_LIST


class HelperFunctionClass(BaseTest):
    """
    This class contains all helper test functions
    """

    def setUp(self):
        super(HelperFunctionClass, self).setUp()
        self.landing_page = LandingMainPage(self.driver)
        self.signup_page = SignUpFormPage(self.driver)
        self.authentication_page = AuthenticationPage(self.driver)
        self.utility_page = UtilityHelperPage(self.driver)
        self.my_account_page = MyAccountPage(self.driver)

    def user_is_on_main_page(self):
        """
        Visit Base url
        Make sure browser has opened correct page
        """
        self.landing_page.visit()
        self.landing_page.is_browser_on_page()

    def user_is_on_authentication_page(self):
        """
        click on sign on link
        User is on authentication page
        """
        self.user_is_on_main_page()
        self.landing_page.click_sign_in_button()
        self.authentication_page.is_browser_on_page()

    def user_is_on_signup_form_page(self):
        """
        User is on Authentication page
        Enter email address
        Click create account button

        :return:
        """
        self.user_is_on_authentication_page()
        email_id = self.authentication_page.enter_address_in_email_field()
        self.assertEqual(self.authentication_page.click_create_account(), PERSONAL_INFO)
        return email_id

    def fill_registration_fields_and_click_submit(self, register_fields):
        """
        Fill the form and click register button
        :param register_fields:
        :return:
        """
        self.user_is_on_signup_form_page()
        # from nose.tools import set_trace;set_trace()
        user_name = self.signup_page.fill_form(register_fields)
        self.signup_page.click_register_button()
        return user_name

    def fields_to_be_removed(self, keys, error_message):
        """
        This helper will help to remove fields
        :return:
        """
        self.fill_registration_fields_and_click_submit(get_registration_fields(keys_to_be_removed=keys))
        # from nose.tools import set_trace;set_trace()
        self.assertEqual(self.authentication_page.check_error_message(), error_message)

    def user_is_on_my_account_page(self):
        """
        This helper will ensure  MyAccount page
        """
        username = self.fill_registration_fields_and_click_submit(get_registration_fields())
        user_account = username[0] + ' ' + username[1]
        self.my_account_page.is_browser_on_page()
        self.assertEqual(self.my_account_page.check_account_name(), user_account)

    def verify_all_adresses_list_works_fine(self):
        from nose.tools import set_trace;set_trace()
        # address_list = self.my_account_page.check_visibility_of_addresses_lists()

        for heading, title in zip(MAIN_HEADING_LIST, TITLE_LIST):
            self.my_account_page.check_visibility_of_addresses_lists(title).click()
            self.assertEqual(self.my_account_page.check_heading_from_address_list(), heading)





        # for each_address, sub_heading in zip(address_list, MAIN_HEADING_LIST):
        #     each_address.click()
        #     self.assertEqual(self.my_account_page.check_heading_from_address_list(), sub_heading)
        #     self.my_account_page.click_on_breadcrumb_account()
        #     self.assertEqual(self.my_account_page.check_heading_from_address_list(), 'MY ACCOUNT')
