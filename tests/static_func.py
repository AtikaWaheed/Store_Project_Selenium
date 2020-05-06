from random import randint
import random, string


def random_number():
    for i in range(11):
        value = randint(10)
        print(value)


def random_text():
    random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    random_text = 'Test%s' % random_string
    return random_text


def get_registration_fields(
        first_name="", last_name="", password="", address="", city="", state="",
        zipcode="", phone="", alias_address="",
        keys_to_be_removed=None
):
    random_name = random_text()
    register_fields = {
        # "title": title,
        "first_name": random_name,
        "last_name": random_name,
        "password": '327684276585858',
        # "address_ist_name": 'Tester',
        # "address_last_name": 'Testing',
        "address": '123 New York',
        "city": 'New York',
        "state": state,
        "zipcode": '54000',
        "phone": '34534534534',
        "alias_address": '234 US'
}
    # from nose.tools import set_trace;set_trace()
    if keys_to_be_removed:
        for key in keys_to_be_removed:
            register_fields.pop(key)
    return register_fields
