import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.fraud_model import model, X_train_smote, y_train_smote, X_test, y_test

def test_underfitting_overfitting():
    # Fit the model and capture the history
    history = model.fit(X_train_smote, y_train_smote, epochs=10, batch_size=32, validation_data=(X_test, y_test))
    
    # Access the training and validation loss
    train_loss = history.history['loss']
    val_loss = history.history['val_loss']
    
    # Check for signs of underfitting (high training and validation loss)
    assert min(train_loss) < 0.5, "Model might be underfitting"
    
    # Check for signs of overfitting (low training loss but high validation loss)
    assert abs(train_loss[-1] - val_loss[-1]) < 0.1, "Model might be overfitting"
