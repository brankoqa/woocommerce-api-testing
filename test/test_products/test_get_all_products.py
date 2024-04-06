import logging as logger

import pytest

from src.utilities.requests_utils import RequestUtil


@pytest.mark.tcid1
def test_get_all_products_default_per_page():
    """Dafault 'per_page' = 10, so here we're expecting that 10 products are returned."""
    api = RequestUtil()
    response = api.get("/products")
    response_json = response.json()
    logger.debug("REST call ended!")
    assert (
        len(response_json) == 10
    ), f"Number of products returned by API call 'get products' with 'per-page' = 10 is not 10. It is: {len(response_json)}."


@pytest.mark.tcid2
def test_get_all_products_per_page_is_20():
    """Set 'per_page' = 20 in the payload, so here we're expecting that 20 products are returned."""
    api = RequestUtil()
    payload = {"per_page": 20}
    response = api.get("/products", payload=payload)
    response_json = response.json()
    logger.debug("REST call ended!")
    assert (
        len(response_json) == 20
    ), f"Number of products returned by API call 'get products' with 'per_page' = 20 is not 20. It is: {len(response_json)}."


@pytest.mark.tcid3
def test_get_all_products_per_page_is_invalid():
    """Set 'per_page' = 'string' in the payload, so here we're expecting status code 400. Invalid parameter(s): per_page."""
    api = RequestUtil()
    payload = {"per_page": "string"}
    response = api.get("/products", payload=payload, expected_status_code=400)
    response_json = response.json()
    logger.debug("REST call ended!")
    assert (
        response_json["message"] == "Invalid parameter(s): per_page"
    ), f"Response property 'message' should have value 'Invalid parameter(s): per_page'. Instead it has value: {response_json["message"]}"


@pytest.mark.tcid4
def test_get_all_products_max_price():
    """Set max price and verify all products retrieved price does not goes over 'max-price' property.
    Default 'per_page' = 10"""
    api = RequestUtil()
    payload = {"max_price": "100"}
    response = api.get("/products", payload=payload)
    response_json = response.json()
    logger.debug("REST call ended!")
    for i in range(len(response_json)):
        assert float(response_json[i]["price"]) <= float(20), f"{response_json[i]["price"]} is greather than 20, for product id: {response_json[i]["id"]}!" # consider changing to SOFT assertion!


@pytest.mark.tcid5
def test_get_all_products_min_price():
    """Set min_price and verify all products retrieved price does not goes under 'min_price'(string) property
    Scenario 'min_price'=20
    Default 'per_page' = 10"""
    api = RequestUtil()
    payload = {"min_price": "20"}
    response = api.get("/products", payload=payload)
    response_json = response.json()
    logger.debug("REST call ended!")
    for i in range(len(response_json)):
        assert float(response_json[i]["price"]) >= float(20), f"{response_json[i]["price"]} is less than 20, for product id: {response_json[i]["id"]}!" # test is failing. 
        # Should be checked weather we should compare against 'regular_price' or 'price' property? In test we compaare with 'price' property!


@pytest.mark.skip(reason="Not sure how this functionality works!")
@pytest.mark.tcid6
def test_get_all_products_on_sale():
    """Verify all products retrieved have 'on_sale' property set to True. 
    Default 'per_page' = 10
    NOTE: This functionality does not work as expected!"""
    api = RequestUtil()
    payload = {"on_sale": True}
    response = api.get("/products", payload=payload)
    response_json = response.json()
    logger.debug("REST call ended!")
    for i in range(len(response_json)):
        assert response_json[i]["on_sale"] == True, f"{response_json[i]["on_sale"]} is not True, for product id: {response_json[i]["id"]}!"
    # Doesn't work as expected!


@pytest.mark.tcid7
def test_get_all_products_stock_status_instock():
    """Possible values for 'stock_status': instock, outofstock and onbackorder. Verify for all values + min 1 negative scenario"""
    api = RequestUtil()
    payload = {"stock_status": "instock"}
    response = api.get("/products", payload=payload)
    response_json = response.json()
    logger.debug("REST call ended!")
    for i in range(len(response_json)):
        assert response_json[i]["stock_status"] == "instock", f"{response_json[i]["stock_status"]} is not 'instock', for product id: {response_json[i]["id"]}!"


@pytest.mark.tcid8
def test_get_all_products_stock_status_outofstock():
    """Possible values for 'stock_status': instock, outofstock and onbackorder. Verify for all values + min 1 negative scenario"""
    api = RequestUtil()
    payload = {"stock_status": "outofstock"}
    response = api.get("/products", payload=payload)
    response_json = response.json()
    logger.debug("REST call ended!")
    for i in range(len(response_json)):
        assert response_json[i]["stock_status"] == "outofstock", f"{response_json[i]["stock_status"]} is not 'outofstock', for product id: {response_json[i]["id"]}!"


@pytest.mark.tcid9
def test_get_all_products_stock_status_onbackorder():
    """Possible values for 'stock_status': instock, outofstock and onbackorder. Verify for all values + min 1 negative scenario"""
    api = RequestUtil()
    payload = {"stock_status": "onbackorder"}
    response = api.get("/products", payload=payload)
    response_json = response.json()
    logger.debug("REST call ended!")
    for i in range(len(response_json)):
        assert float(response_json[i]["stock_status"]) == "onbackorder", f"{response_json[i]["stock_status"]} is not 'onbackorder', for product id: {response_json[i]["id"]}!"


@pytest.mark.tcid10
def test_get_all_products_stock_status_negative():
    """Possible values for 'stock_status': instock, outofstock and onbackorder. Verify for all values + min 1 negative scenario"""
    api = RequestUtil()
    payload = {"stock_status": "test_stock_status"}
    response = api.get("/products", payload=payload, expected_status_code=400)
    response_json = response.json()
    logger.debug("REST call ended!")
    assert response_json["message"] == "Invalid parameter(s): stock_status", "Response property 'message' is not correct. Should be 'Invalid parameter(s): stock_status'."
