import os
import papermill as pm


def test_data_prep_runs(path_notebooks, output_notebook, kernel_name):
    notebook_path = os.path.join(path_notebooks, "01_data_prep.ipynb")
    pm.execute_notebook(notebook_path, output_notebook, kernel_name=kernel_name)
