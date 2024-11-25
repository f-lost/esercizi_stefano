# Importare le librerie necessarie
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza del modello: {accuracy:.2f}")
    
label_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    
y_test_labels = [label_map[x] for x in y_test]
y_pred_labels = [label_map[x] for x in y_pred]

print(y_test[:5])
print(y_pred[:5])
for i in range(10):
    print(f"Il fiore con dati: {X_test[i]} è un {y_test_labels[i]}, è stato predetto: {y_pred_labels[i]}")