from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)
print(f"\nLa profondità dell'albero è: \t{model.get_depth()}\n")


y_pred = model.predict(X_test)


class_report = classification_report(y_test, y_pred, target_names = iris.target_names)
print(class_report)

cm = confusion_matrix(y_test, y_pred)
cm_display = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels=iris.target_names)

cm_display.plot()
plt.show()

# label_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    
# y_test_labels = [label_map[x] for x in y_test]
# y_pred_labels = [label_map[x] for x in y_pred]

# print(y_test[:5])
# print(y_pred[:5])
# for i in range(10):
#     print(f"Il fiore con dati: {X_test[i]} è un {y_test_labels[i]}, è stato predetto: {y_pred_labels[i]}")