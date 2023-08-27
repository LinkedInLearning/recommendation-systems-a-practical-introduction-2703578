import os
import pytest


@pytest.fixture(scope="session")
def output_notebook():
    return "output.ipynb"


@pytest.fixture(scope="session")
def kernel_name():
    """Unless manually modified, python3 should be the name of the current jupyter kernel
    that runs on the activated conda environment"""
    return "python3"


def path_notebooks():
    """Returns the path of the notebooks folder"""
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, "notebooks")
    )
