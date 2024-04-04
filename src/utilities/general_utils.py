import logging as logger
import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None) -> dict:
    logger.debug("Generating random email and password started")

    if not domain:
        domain = "test.domain.com"
    if not email_prefix:
        email_prefix = "test.email"

    random_email_string_length = 10
    email_random_string = "".join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + "." + email_random_string + "@" + domain

    password_length = 20
    password = "".join(random.choices(string.ascii_letters, k=password_length))

    random_credentials = {
        "email": email,
        "password": password
    }
    logger.debug(f"Randomly generated credentials are: {random_credentials}")

    return random_credentials
