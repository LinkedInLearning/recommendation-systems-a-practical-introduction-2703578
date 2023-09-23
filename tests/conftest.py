import pytest


@pytest.fixture(scope="function")
def sar_header():
    return {
        "col_user": "UserId",
        "col_item": "MovieId",
        "col_rating": "Rating",
        "col_timestamp": "Timestamp",
        "col_prediction": "prediction",
    }
