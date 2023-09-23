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
        "item_id": 242,
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
    assert df.iloc[0]["item_id"] == movielens_100k_first_row["item_id"]
    assert df.iloc[0]["rating"] == movielens_100k_first_row["rating"]
    assert df.iloc[0]["timestamp"] == movielens_100k_first_row["timestamp"]
    assert df.iloc[0]["title"] == movielens_100k_first_row["title"]
    assert df.iloc[0]["genres"] == movielens_100k_first_row["genres"]
    assert df.iloc[0]["year"] == movielens_100k_first_row["year"]
    assert df["user_id"].min() == 1
    assert df["user_id"].max() == 943
    assert df["item_id"].min() == 1
    assert df["item_id"].max() == 1682
    assert df["rating"].min() == 1
    assert df["rating"].max() == 5
    assert df["timestamp"].min() == 874724710
    assert df["timestamp"].max() == 893286638
    assert df["title"].nunique() == 1664
    assert df["genres"].nunique() == 301
    assert df["year"].nunique() == 71
    assert df["year"].min() == "1922"
    assert df["year"].max() == "1998"
