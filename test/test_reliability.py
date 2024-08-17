
import os, sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.fraud_model import model


def test_reliability():
    # Test if the model can make consistent predictions on the same input
    dummy_data = np.array([[0.5] * model.input_shape[1]])  # Convert list to NumPy array
    first_prediction = model.predict(dummy_data)
    second_prediction = model.predict(dummy_data)
    
    # Check if the predictions are consistent
    assert np.array_equal(first_prediction, second_prediction), "Model should produce consistent results on the same input"