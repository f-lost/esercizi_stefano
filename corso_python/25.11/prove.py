from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np


data = load_iris()
X = data.data
y = data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

linear = LinearRegression()
linear.fit(X_scaled, y)
linear_predictions = np.round(linear.predict(X_scaled)).astype(int)
linear_predictions = np.clip(linear_predictions, 0, len(np.unique(y)) - 1) 
accuracy_linear = accuracy_score(y, linear_predictions)
print(f"Accuratezza del modello lineare: {accuracy_linear:.2f}")

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_scaled, y)
knn_predictions = knn.predict(X_scaled)
accuracy_knn = accuracy_score(y, knn_predictions)
print(f"Accuratezza del modello knn: {accuracy_knn:.2f}")