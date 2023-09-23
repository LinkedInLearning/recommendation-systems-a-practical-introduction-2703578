import os
import pytest
from recommenders.datasets import movielens


@pytest.fixture(scope="function")
def movielens_cols():
    return {
        "size": "100k",
        "header": ["user_id", "item_id", "rating", "timestamp"],
        "title_col": "title",
        "genres_col": "genres",
        "year_col": "year",
    }


@pytest.fixture(scope="function")
def movielens_100k_first_row():
    return {
        "user_id": 196,
        "item_id": 1,
        "rating": 3,
        "timestamp": 881250949,
        "title": "Toy Story (1995)",
        "genres": "Animation|Children's|Comedy",
        "year": "1995",
    }


def test_movielens(movielens_cols, movielens_100k_first_row):
    df = movielens.load_pandas_df(**movielens_cols)
    assert len(df) == 100000
    assert df.columns.tolist() == [
        "user_id",
        "item_id",
        "rating",
        "timestamp",
        "title",
        "genres",
        "year",
    ]
    assert df.iloc[0]["user_id"] == movielens_100k_first_row["user_id"]
    # assert movielens_100k_first_row["item_id"] == 242
    # assert movielens_100k_first_row["rating"] == 3
    # assert movielens_100k_first_row["timestamp"] == 881250949
