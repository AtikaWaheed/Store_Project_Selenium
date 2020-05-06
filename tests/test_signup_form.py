from tests.helper_func import HelperFunctionClass
from constants import ERR_EMAIL, ERROR_FIRST_NAME, ERROR_LAST_NAME, ERROR_PASWD, ERROR_ADDRESS1
from constants import ERROR_CITY, ERROR_STATE, ERROR_ZIP, ERROR_COUNTRY, ERROR_PHONE, ERROR_ALIAS_ADDRESS
import random
from tests.static_func import get_registration_fields


class SignUpTestClass(HelperFunctionClass):

    def setUp(self):
        super(SignUpTestClass, self).setUp()

    def test_user_is_on_user_is_on_authentication_page(self):
        self.user_is_on_authentication_page()

    def test_empty_field_account_message(self):
        """
        Verify correct error message for create account empty field
        """
        self.user_is_on_authentication_page()
        self.authentication_page.click_create_account()
        self.assertEqual(self.authentication_page.check_error_message(), ERR_EMAIL)

    def test_signup_form_page_opened(self):
        """
        Verify user is redirected to sign up form page
        """
        self.user_is_on_signup_form_page()

    def test_verify_email_field_is_prefilled(self):
        """
        Verify if Email field is correct pre filled
        """
        email_id = self.user_is_on_signup_form_page()
        self.assertEqual(self.signup_page.check_email_field(), email_id)

    def test_first_name_field_is_empty(self):
        """
        Verify error message for empty first name field
        """
        expected_error = [ERROR_FIRST_NAME]
        self.fields_to_be_removed(['first_name'], expected_error)

    def test_last_name_field_is_empty(self):
        """
        Verify error message for empty last name field
        """
        expected_error = [ERROR_LAST_NAME]
        self.fields_to_be_removed(['last_name'], expected_error)

    def test_password_field_is_empty(self):
        """
        Verify error message for empty password field
        """
        expected_error = [ERROR_PASWD]
        self.fields_to_be_removed(['password'], expected_error)

    def test_address1_field_is_empty(self):
        """
        Verify error message for empty address 1  field
        """
        expected_error = [ERROR_ADDRESS1]
        self.fields_to_be_removed(['address'], expected_error)

    def test_city_field_is_empty(self):
        """
        Verify error message for empty city field
        """
        expected_error = [ERROR_CITY]
        self.fields_to_be_removed(['city'], expected_error)

    def test_state_field_is_empty(self):
        """
        Verify error message for empty state field
        """
        expected_error = [ERROR_STATE]
        self.fields_to_be_removed(['state'], expected_error)

    def test_zipcode_field_is_empty(self):
        """
        Verify error message for empty zip code field
        """
        expected_error = [ERROR_ZIP]
        self.fields_to_be_removed(['zipcode'], expected_error)

    def test_country_field_is_empty(self):
        """
        Verify error message for empty country field
        """
        expected_error = [ERROR_COUNTRY]
        self.fields_to_be_removed(['country'], expected_error)

    def test_phone_field_is_empty(self):
        """
        Verify error message for empty phone field
        """
        expected_error = [ERROR_PHONE]
        self.fields_to_be_removed(['phone'], expected_error)

    def test_alias_address_field_is_empty(self):
        """
        Verify error message for empty alias address field
        """
        expected_error = [ERROR_ALIAS_ADDRESS]
        self.fields_to_be_removed(['alias_address'], expected_error)

    def test_verify_form_is_submitted_with_correct_username(self):
        """
        Form is submitted
        """
        self.user_is_on_my_account_page()
