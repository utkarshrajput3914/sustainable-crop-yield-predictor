import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load dataset
df = pd.read_csv('yield_dataset_2000.csv')
print("Dataset loaded! Shape:", df.shape)

# Features and target
X = df[['Rainfall_mm', 'Temperature_C', 'Fertilizer_kg', 'Area_hectare']]
y = df['Yield_ton_per_hectare']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
print("R2 Score :", round(r2_score(y_test, y_pred), 4))
print("RMSE     :", round(np.sqrt(mean_squared_error(y_test, y_pred)), 4))

# Save model and scaler
joblib.dump(model, 'crop_yield_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("✅ crop_yield_model.pkl and scaler.pkl saved successfully!")