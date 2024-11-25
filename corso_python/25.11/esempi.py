from sklearn.datasets import load_iris
data = load_iris()
X = data.data  # caratteristiche
y = data.target  # target


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)  #INSERIRE SEMPRE IL RANDOM_STATE


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
predictions_knn = knn.predict(X_test)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions_linear = model.predict(X_test)


from sklearn.metrics import accuracy_score
accuracy_knn = accuracy_score(y_test, predictions_knn)
print(f"Accuratezza del modello knn: {accuracy_knn}")



from sklearn.metrics import mean_squared_error
mse_linear = mean_squared_error(y_test, predictions_linear)
print(f"MSE del modello lineare: {mse_linear}")