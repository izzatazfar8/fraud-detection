import os, sys
import numpy as np
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from model.fraud_model import model

def test_model_accuracy():
    # Load the dataset
    data = pd.read_csv('data/creditcard.csv')
    X = data.drop(columns=['Time', 'Class'])
    y = data['Class']
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Split the data
    _, X_test, _, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)
    
    # Predict on test data
    predictions = model.predict(X_test)
    
    # Convert probabilities to binary predictions
    binary_predictions = np.where(predictions > 0.5, 1, 0)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, binary_predictions)
    
    # Assert that the model accuracy is above a certain threshold
    assert accuracy > 0.9, "Model accuracy should be greater than 90%"
