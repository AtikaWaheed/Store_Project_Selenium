import os
from constants import BASE_URL, SUBMIT_ACCOUNT
from .wait_pages import WaitPages
import random


class SignUpFormPage(WaitPages):
    """
        This page will cover login scenarios
        """
    url = os.path.join(BASE_URL, 'controller=authentication&back=my-account')

    def is_browser_on_page(self):
        """
        Verify if browser is on correct page
        """
        self.wait_for_ajax()
        return self.wait_for_an_element_to_be_present('.account_creation')

    def click_register_button(self):
        """
        Click green register button
        """
        self.wait_for_an_element_to_be_present(SUBMIT_ACCOUNT).click()

    def check_email_field(self):
        """
        Check email field is pre-filled with same id
        """
        return self.wait_for_an_element_to_be_present('#email').get_attribute('value')

    def select_title(self):
        """
        Select random title
        """
        radio_elements = self.wait_for_all_elements_to_be_present('.radio')
        random.choice(radio_elements).click()
        self.wait_for_visibility_of_element('.radio-inline .checked')

    def fill_form(self, register_fields):

        # if 'title' in register_fields:
        #     self.select_title()

        if "first_name" in register_fields:
            first_name = self.wait_for_an_element_to_be_present('[data-validate="isName"]#customer_firstname')
            first_name.send_keys(register_fields["first_name"])

        if "last_name" in register_fields:
            last_name = self.wait_for_an_element_to_be_present('[data-validate="isName"]#customer_lastname')
            last_name.send_keys(register_fields["last_name"])

        if 'password' in register_fields:
            self.wait_for_an_element_to_be_present('#passwd').send_keys(register_fields['password'])

        # if 'address_ist_name' in register_fields:
        #     self.wait_for_an_element_to_be_present('input#firstname').send_keys(register_fields['address_ist_name'])
        #
        # if 'address_last_name' in register_fields:
        #     self.wait_for_an_element_to_be_present('input#lastname').send_keys(register_fields['address_last_name'])

        if 'address' in register_fields:
            self.wait_for_an_element_to_be_present('#address1').send_keys(register_fields['address'])

        if 'city' in register_fields:
            self.wait_for_an_element_to_be_present('#city').send_keys(register_fields['city'])

        if 'state' in register_fields:
            self.wait_for_an_element_to_be_present("#id_state option[value='32']").click()

        if 'zipcode' in register_fields:
            self.wait_for_an_element_to_be_present('#postcode').send_keys(register_fields['zipcode'])

        if 'phone' in register_fields:
            self.wait_for_an_element_to_be_present('#phone_mobile').send_keys(register_fields['phone'])

        if 'alias_address' in register_fields:
            self.wait_for_an_element_to_be_present('#alias').send_keys(register_fields['alias_address'])

        return register_fields["first_name"], register_fields["last_name"]


