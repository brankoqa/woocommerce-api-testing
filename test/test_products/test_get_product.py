def test_get_one_product():
    """Verify that API can return one existing product:
    Get random product from the database and then get it via API call.
    Verify 'id', 'price', and 'name'.
    """


def test_create_product_only_required_fields():
    """Create a products using fields: 'name', 'type', 'regular price', 'description'"""


def test_create_product_negative_scenarios():
    """property: 'name'-> string, test for: empty string, number, special characters, space as string, one char string,
    property: 'type'-> string, test for: empty string, number, special characters, space as string, one char string, todo: see what are valid types?
    property: 'regular price'-> string, test for: empty string, number, special characters, space as string, one char string
    property: 'description'-> string, test for: empty string, number, special characters, space as string, one char string
    """
