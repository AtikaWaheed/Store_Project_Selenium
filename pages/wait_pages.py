from selenium.webdriver.support.wait import WebDriverWait
from .utility_page import UtilityHelperPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class WaitPages(UtilityHelperPage):
    """
    This page will handle all waits on pages
    """

    def wait_for_ajax(self):
        """
        Wait for the page to load and all requests to be finished
        """
        wait = WebDriverWait(self.driver, self.time_to_wait)
        return wait.until(lambda driver: driver.execute_script
                          ("return typeof(jQuery)!='undefined' && jQuery.active") == 0)

    def wait_for_visibility_of_element(self, css_selector):
        """
        Wait for css selector to be visible in DOM
        """
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, css_selector)
            )
        )

    def wait_for_visibility_of_all_elements(self, css_selector):
        """
        Wait for all css selectors to be visible in DOM
        """
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, css_selector))
        )

    def wait_for_invisibility_of_element(self, css_selector):
        """
        Wait for css selector to be invisible in DOM
        """
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, css_selector))
        )

    def wait_for_an_element_to_be_present(self, css_selector):
        """
        wait for an element to present in DOM
        :param css_selector: Element's selector which needs to be present
        :return:
        """
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css_selector))
        )

    def wait_for_all_elements_to_be_present(self, css_selector):
        """
        wait for all elements to present in DOM
        :param css_selector: Element's selector which needs to be present
        """
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, css_selector))
        )

    def wait_for_text_to_be_present(self, css_selector, text):
        """
        Wait for specific text to be present
        :param css_selector: css selector for specified text element
        :param text: selected text option
        """
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, css_selector), text)
        )

    def wait_for_the_element_to_be_clickable(self, css_selector):
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, css_selector))
        )
