from tests.helper_func import HelperFunctionClass
from constants import MAIN_MENU_OPTIONS


class LandingPageTestClass(HelperFunctionClass):

    def setUp(self):
        super(LandingPageTestClass, self).setUp()

    def test_landing_page(self):
        """
        Make sure correct page is open
        """
        self.user_is_on_main_page()

    def test_main_menu_options(self):
        """
        Verify menu options on main page.
        """
        self.user_is_on_main_page()
        self.assertTrue(self.landing_page.check_main_menu_options())

    def test_slider_row_ads(self):
        """
        Verify sliders row ads
        """
        self.user_is_on_main_page()
        self.assertTrue(self.landing_page.check_slider_ads())





