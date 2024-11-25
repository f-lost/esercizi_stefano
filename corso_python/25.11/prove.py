from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np


data = load_iris()
X = data.data
y = data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

linear = LinearRegression()
linear.fit(X_scaled, y)
y_pred = np.round(linear.predict(X_test)).astype(int)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza del modello: {accuracy:.2f}")


label_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    
y_test_labels = [label_map[x] for x in y_test]
y_pred_labels = [label_map[x] for x in y_pred]

for i in range(10):
    print(f"Il fiore con dati: {X_test[i]} è un {y_test_labels[i]}, è stato predetto: {y_pred_labels[i]}")