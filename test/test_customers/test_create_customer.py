import logging as logger
from pprint import pprint

import pytest

from src.dao.customers_dao import CustomersDAO
from src.utilities.general_utils import generate_random_email_and_password
from src.utilities.requests_utils import RequestUtil


@pytest.mark.tcid29
def test_create_customer_only_email():
    logger.info("Test started: customer only email logger!")
    # create payload
    random_credentials = generate_random_email_and_password()
    payload = {"email": random_credentials["email"]}
    # make a call
    api = RequestUtil()
    logger.debug("Starting a REST call!")
    response = api.post("/customers", payload=payload, expected_status_code=201)
    response_dict = dict(response.json())
    logger.debug("REST call ended!")
    # verify email - json value
    assert response_dict["email"] == random_credentials["email"]
    assert response_dict["first_name"] == "", "First Name should be empty string!"
    assert response_dict["username"] == random_credentials["email"].split("@")[0], "Username is not correct!"
    # verify customer created in the database
    customers_dao = CustomersDAO()
    cust_db_info = customers_dao.get_customer_by_email(random_credentials["email"])
    logger.info(cust_db_info)
    id_from_api = response_dict["id"]
    id_from_db = cust_db_info[0]["ID"]
    assert id_from_api == id_from_db, f"'id' from API: {id_from_api} call should be equal to the 'id' from database: {id_from_db}"\
                                f" For user email {random_credentials["email"]}"
    # assert cust_db_info["user_email"]
    logger.info(f"Test ended: customer created: email {response_dict["email"]}")


@pytest.mark.tcid30
def test_create_customer_email_and_password():
    logger.info("Test started: customer only email logger!")
    # create payload
    random_credentials = generate_random_email_and_password()
    payload = {"email": random_credentials["email"],
               "password": random_credentials["password"]}
    # make a call
    api = RequestUtil()
    logger.debug("Starting a REST call!")
    response = api.post("/customers", payload=payload, expected_status_code=201)
    response_dict = dict(response.json())
    logger.debug("REST call ended!")
    # verify json values
    assert response_dict["email"] == random_credentials["email"], "Returned wrong email!"
    assert response_dict["first_name"] == "", "First Name should be empty string!"
    assert response_dict["username"] == random_credentials["email"].split("@")[0], "Username is not correct!"
    # verify customer created in the database
    logger.info(f"Test ended: customer created: email {response_dict["email"]}")


def test_create_customer_only_first_name():
    pass


def test_create_customer_existing_email():
    pass
