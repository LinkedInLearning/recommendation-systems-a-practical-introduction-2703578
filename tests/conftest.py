import pytest


@pytest.fixture(scope="function")
def sar_header():
    return {
        "col_user": "userID",
        "col_item": "itemID",
        "col_rating": "rating",
        "col_timestamp": "timestamp",
        "col_prediction": "prediction",
    }
