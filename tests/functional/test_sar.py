import os
import pytest
import papermill as pm
import scrapbook as sb


def test_data_prep_runs(path_notebooks, output_notebook, kernel_name):
    notebook_path = os.path.join(path_notebooks, "02_sar_movielens.ipynb")
    pm.execute_notebook(
        notebook_path,
        output_notebook,
        kernel_name=kernel_name,
        parameters=dict(TOP_K=10, MOVIELENS_DATA_SIZE="100k"),
    )
    results = sb.read_notebook(output_notebook).scraps.dataframe.set_index("name")[
        "data"
    ]

    assert results["map"] == pytest.approx(0.110591, rel=TOL, abs=ABS_TOL)
    assert results["ndcg"] == pytest.approx(0.382461, rel=TOL, abs=ABS_TOL)
    assert results["precision"] == pytest.approx(0.330753, rel=TOL, abs=ABS_TOL)
    assert results["recall"] == pytest.approx(0.176385, rel=TOL, abs=ABS_TOL)
