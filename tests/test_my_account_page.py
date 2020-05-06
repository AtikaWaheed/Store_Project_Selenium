from tests.helper_func import HelperFunctionClass
from tests.static_func import get_registration_fields


class MyAccountTestClass(HelperFunctionClass):
    """
    This class contains all tests from My Account Page
    """

    def setUp(self):
        super(MyAccountTestClass, self).setUp()

    def test_all_addresses_links_works_correct(self):
        """
        Verify if correct username is displayed
        """
        self.user_is_on_my_account_page()
        self.verify_all_adresses_list_works_fine()
