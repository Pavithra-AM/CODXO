# -*- coding: utf-8 -*-
"""forest_fire_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ci7Rkwm-Usl-Nfy8UfAgKqyoyCsTuvb4
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

file_path = '/content/forestfires.csv'
forest_fires = pd.read_csv(file_path)

print(forest_fires.head())

forest_fires_encoded = pd.get_dummies(forest_fires, columns=['month', 'day'])

X = forest_fires_encoded.drop(['area'], axis=1)
y = np.log1p(forest_fires_encoded['area'])  # Log-transform the target variable to handle skewness

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = RandomForestRegressor(random_state=42)

model.fit(X_train_scaled, y_train)

y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Training Mean Squared Error (MSE): {train_mse}")
print(f"Testing Mean Squared Error (MSE): {test_mse}")
print(f"Training R-squared (R²): {train_r2}")
print(f"Testing R-squared (R²): {test_r2}")