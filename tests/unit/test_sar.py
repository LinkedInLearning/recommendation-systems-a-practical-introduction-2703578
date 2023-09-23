import pytest
from recommenders.models.sar import SAR


def test_sar_init(sar_header):
    model = SAR(similarity_type="jaccard", **sar_header)

    assert model.col_user == "userID"
    assert model.col_item == "itemID"
    assert model.col_rating == "rating"
    assert model.col_timestamp == "timestamp"
    assert model.col_prediction == "prediction"
    assert model.similarity_type == "jaccard"
    assert model.time_decay_half_life == 2592000
    assert not model.time_decay_flag
    assert model.time_now is None
    assert model.threshold == 1
