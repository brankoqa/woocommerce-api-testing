import logging as logger

import pytest

from src.dao.customers_dao import CustomersDAO
from src.utilities.general_utils import generate_random_email_and_password
from src.utilities.requests_utils import RequestUtil
from src.utilities.general_utils import get_random_entity


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
    logger.info("Test ended: customer created: email %s", response_dict["email"])


@pytest.mark.tcid30
def test_create_customer_email_and_password():
    """_summary_
    Customer should be created only with 'email'. Here we are passing password and validate that
    password is not returned in the response.
    """
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
    assert "password" not in response_dict.keys(), "Password should not be returned in the response!"
    # verify customer created in the database
    logger.info("Test ended: customer created: email is: %s", response_dict["email"])


def test_create_customer_only_first_name():
    pass



@pytest.mark.tcid32
def test_create_customer_existing_email():
    # fetch from database limit 500 customers
    customers_dao = CustomersDAO()
    all_customers = customers_dao.get_all_customers()
    # user random.sample to randomly extract customer from step 1
    random_user = get_random_entity(all_customers, 1)
    # get thye email from user from step 2
    existing_email = random_user[0]["user_email"]
    # try to create a new customer with that email
    payload = {"email": existing_email}
    api = RequestUtil()
    logger.debug("Starting a REST call!")
    response = api.post("/customers", payload=payload, expected_status_code=400)
    response_dict = dict(response.json())
    logger.debug("REST call ended!")
    # print saatus code
    logger.debug("Response from API call: %s", response_dict)
    # assert you can't create two users with same email
    assert response_dict["code"] == "registration-error-email-exists", "'Code' property not correct, should be 'registration-error-email-exists'!"
    assert response_dict["message"] == "An account is already registered with your email address. <a href=\"#\" class=\"showlogin\">Please log in.</a>", "Error message is not as expected!"
    assert response_dict["data"]["status"] == 400, "Wrong 'status', should be '400'!"
