import logging as logger
import pytest


from src.utilities.requests_utils import RequestUtil


@pytest.mark.tcid31
def test_get_all_customers():
    req_util = RequestUtil()
    logger.debug("Executing API Get customers call")
    r_dict = req_util.get("/customers", payload={"per_page": 100}).json()
    assert r_dict, "Response for Get All Customers is empty!"
