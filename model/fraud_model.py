import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Step 1: Load and preprocess the dataset
data = pd.read_csv('data/creditcard.csv')

# Separate features (V1-V28, Amount) and the target variable (Class)
X = data.drop(columns=['Time', 'Class'])
y = data['Class']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# Step 3: Apply SMOTE to balance the classes in the training set
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# Step 4: Build the model
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train_smote.shape[1],)),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model with 'recall' as the focus
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['Recall'])

# Train the model
model.fit(X_train_smote, y_train_smote, epochs=5, batch_size=32, validation_data=(X_test, y_test))

# Save the model
model.save('model/fraud_detection_model.keras')

# Step 5: Load new transaction data from CSV for prediction
new_transaction_data = pd.read_csv('data/new_transaction.csv')

# Preprocess the new transaction data
new_transaction_scaled = scaler.transform(new_transaction_data)

# Predict using the model
predictions = model.predict(new_transaction_scaled)

# Output the results for each transaction
for i, prediction in enumerate(predictions):
    if prediction > 0.5:
        print(f"Transaction {i + 1}: Fraudulent")
    else:
        print(f"Transaction {i + 1}: Legitimate")
