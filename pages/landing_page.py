from .wait_pages import WaitPages
from constants import BASE_URL, MAIN_MENU_OPTIONS, OPTION_CSS
import time
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException


class LandingMainPage(WaitPages):
    """
    This is main landing page of store for users
    """
    url = BASE_URL

    def is_browser_on_page(self):
        """
        Is browser on home page
        """
        try:
            self.wait_for_ajax()
            return self.wait_for_visibility_of_element('.footer-container')
        except TimeoutException:
            print("Page is taking much time to load")

    def click_sign_in_button(self):
        """
        Click signIn button from top right
        """
        # from nose.tools import set_trace;set_trace()
        sign_in = self.wait_for_an_element_to_be_present('.header_user_info')
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(sign_in).click().perform()
        time.sleep(10)
        # self.wait_for_ajax()
        self.wait_for_an_element_to_be_present('.navigation_page')
        time.sleep(10)

    def check_main_menu_options(self):
        """
        Check main menu options on main page
        """
        menu_options = []

        # Hover each sub option and assert popup
        for option in MAIN_MENU_OPTIONS:
            single_option = self.wait_for_an_element_to_be_present('{} [title="{}"]'
                                                                   .format(OPTION_CSS, option))
            single_option_text = single_option.text
            menu_options.append(single_option_text.lower())

            if option != "T-shirts":
                action_chains = ActionChains(self.driver)
                action_chains.move_to_element(single_option).perform()
                self.wait_for_visibility_of_element('.sfHover [title="{}"]'.format(option))
            else:
                print('No hovering popup exist')
        return menu_options

    def check_slider_ads(self):
        """
        Verify slider ads are displayed.
        """
        # from nose.tools import set_trace;set_trace()
        return self.wait_for_an_element_to_be_present('#slider_row')
