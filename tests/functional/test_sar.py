import pytest

from recommenders.datasets import movielens
from recommenders.models.sar import SAR


TOL = 0.05
ABS_TOL = 0.05


@pytest.fixture(scope="module")
def df():
    return movielens.load_pandas_df(
        size="100k", header=["UserId", "MovieId", "Rating", "Timestamp"]
    )


def test_data_prep_runs(df, sar_header):
    model = SAR(**sar_header)
