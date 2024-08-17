
import pytest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.fraud_model import model

def test_negative():
    # Test the model with a negative scenario
    negative_data = [[-1.0] * model.input_shape[1]]
    prediction = model.predict(negative_data)
    assert prediction < 0.5, "Model should return a low probability for negative data"
