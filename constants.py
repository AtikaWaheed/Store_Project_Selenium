import os

# url
BASE_URL = "http://automationpractice.com/index.php"

# Login

USER_EMAIL = os.getenv("useremail")
USER_PWD = os.getenv("userpassword")

# SignUp css_selectors and messages

CREATE_ACCOUNT = '#SubmitCreate'
SUBMIT_ACCOUNT = '#submitAccount'
PERSONAL_INFO = 'YOUR PERSONAL INFORMATION'

# Main menu list

MAIN_MENU_OPTIONS = ['Women', 'Dresses', 'T-shirts']
OPTION_CSS = '#block_top_menu'

# Error messages

ERR_EMAIL = 'Invalid email address.'
ERROR_FIRST_NAME = 'firstname is required.'
ERROR_LAST_NAME = 'lastname is required.'
ERROR_PASWD = 'passwd is required.'
ERROR_ADDRESS1 = 'address1 is required.'
ERROR_CITY = 'city is required.'
ERROR_COUNTRY = 'id_country is required.'
ERROR_STATE = 'This country requires you to choose a State.'
ERROR_ZIP = "The Zip/Postal code you've entered is invalid. It must follow this format: 00000"
ERROR_ALIAS_ADDRESS = 'alias is required.'
ERROR_PHONE = 'You must register at least one phone number.'

# addresses lists
MAIN_HEADING_LIST = ['ORDER HISTORY', 'CREDIT SLIPS', 'MY ADDRESSES', 'YOUR PERSONAL INFORMATION',
                'MY WISHLISTS']
TITLE_LIST = ['Orders', 'Credit slips', 'Addresses', 'InformationN', 'My wishlist']
