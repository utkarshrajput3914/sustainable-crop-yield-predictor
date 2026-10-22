import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# Load data
df = pd.read_csv('yield_df.csv').drop(columns=['Unnamed: 0'])

# Encode categorical columns
le_area = LabelEncoder()
le_item = LabelEncoder()
df['Area'] = le_area.fit_transform(df['Area'])
df['Item'] = le_item.fit_transform(df['Item'])

# Split features and target
X = df.drop(columns=['hg/ha_yield'])
y = df['hg/ha_yield']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
print(f"R² Score : {r2_score(y_test, preds):.4f}")
print(f"MAE      : {mean_absolute_error(y_test, preds):,.0f} hg/ha")