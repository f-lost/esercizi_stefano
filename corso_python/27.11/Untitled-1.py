# %%
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold

# %%
data = load_wine()
X = data.data
y = data.target

# %%
X, y = load_wine(return_X_y= True, as_frame = True)

# %%
X

# %%
y.unique()

# %%
wine = load_wine()
print(wine["DESCR"])

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) 

# %%
model = RandomForestClassifier(random_state=42)

# %%
param_grid = {
    "n_estimators": [100, 150, 200],  
    "max_depth": [None, 10, 20, 30],
    'criterion' : ['gini', 'entropy', 'log_loss'],
    "max_features": ["sqrt", "log2", None]

}

# %%
kfold = KFold(n_splits = 5, shuffle = True, random_state = 42)

# %%
GridSearch = GridSearchCV(model, param_grid = param_grid, cv = kfold, scoring = "accuracy")

# %%
GS = GridSearch.fit(X_train, y_train)

# %%
print(GridSearch.best_params_)

# %%
OptModel = model.set_params(**GridSearch.best_params_)

# %%
OptModel.fit(X, y)

# %%
y_pred = OptModel.predict(X)

# %%
class_report = classification_report(y, y_pred, target_names = wine.target_names)
print(class_report)

# %%
cm = confusion_matrix(y, y_pred)
cm_display = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels=wine.target_names)
cm_display.plot()
plt.show()

# %%
pca = PCA(n_components = 2, random_state = 42)
X_pca = pca.fit_transform(X)

# %%
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
df_pca['target'] = y

plt.figure(figsize=(10,8))
sns.scatterplot(data=df_pca, x='PC1', y='PC2', hue='target', palette='Set1', s=43, alpha=0.5, linewidth=0)
plt.axis(True)
plt.title('Wine dataset - Dimensionalità ridotta con PCA')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend(title='Cifra disegnata')
plt.show()

# %%



