import pytest, sys, os
import tensorflow as tf
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.fraud_model import model
def test_security():
    # Attempt to inject malicious input
    malicious_input = np.array([[np.inf] * model.input_shape[1]])
    try:
        prediction = model.predict(malicious_input)
    except Exception as e:
        pytest.fail(f"Security test failed: {e}")
