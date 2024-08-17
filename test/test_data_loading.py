import pytest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd

def test_data_loading():
    try:
        data = pd.read_csv('data/new_transaction.csv')
    except FileNotFoundError:
        pytest.fail("new_transaction.csv not found!")
    assert not data.empty, "Data should not be empty"
