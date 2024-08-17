import sys
import os
import pytest
import pandas as pd

# Add the project's root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.fraud_model import model, scaler

def test_functionality():
    # Load new transaction data
    new_transaction_data = pd.read_csv('data/new_transaction.csv')
    # Preprocess the data
    new_transaction_scaled = scaler.transform(new_transaction_data)
    # Predict using the model
    predictions = model.predict(new_transaction_scaled)
    # Ensure that predictions are within the correct range
    assert all(0 <= pred <= 1 for pred in predictions), "Predictions should be between 0 and 1"
