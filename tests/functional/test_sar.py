import pytest

from recommenders.datasets import movielens
from recommenders.datasets.python_splitters import python_stratified_split
from recommenders.models.sar import SAR
from recommenders.evaluation.python_evaluation import (
    map_at_k,
    ndcg_at_k,
    precision_at_k,
    recall_at_k,
)


ABS_TOL = 0.05


@pytest.fixture(scope="module")
def data():
    return movielens.load_pandas_df(
        size="100k", header=["userID", "itemID", "rating", "timestamp"]
    )


def test_sar_movielens_functional(data, sar_header):
    TOP_K = 10
    train, test = python_stratified_split(
        data, ratio=0.75, col_user="userID", col_item="itemID", seed=42
    )
    model = SAR(**sar_header)
    model.fit(train)
    top_k = model.recommend_k_items(test, top_k=TOP_K, remove_seen=True)
    eval_map = map_at_k(
        test, top_k, col_user="userID", col_item="itemID", col_rating="rating", k=TOP_K
    )
    eval_ndcg = ndcg_at_k(
        test, top_k, col_user="userID", col_item="itemID", col_rating="rating", k=TOP_K
    )
    eval_precision = precision_at_k(
        test, top_k, col_user="userID", col_item="itemID", col_rating="rating", k=TOP_K
    )
    eval_recall = recall_at_k(
        test, top_k, col_user="userID", col_item="itemID", col_rating="rating", k=TOP_K
    )

    assert eval_map == pytest.approx(0.106959, abs=ABS_TOL)
    assert eval_ndcg == pytest.approx(0.379533, abs=ABS_TOL)
    assert eval_precision == pytest.approx(0.331071, abs=ABS_TOL)
    assert eval_recall == pytest.approx(0.176837, abs=ABS_TOL)
