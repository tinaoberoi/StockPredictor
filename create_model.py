import pandas as pd
import numpy as np
import pickle
import sklearn.linear_model as skl_lm
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import neighbors

plt.rc('figure', figsize=(25, 9))
np.set_printoptions(precision=4, suppress=True)

url = 'https://raw.githubusercontent.com/dsahota-applied-data-analysis/data/main/Smarket.csv'
smarket = pd.read_csv(url)
print(smarket.corr())
smarket_train = smarket[smarket['Year'] <= 2004]
smarket_test = smarket[smarket['Year'] == 2005]

model = neighbors.KNeighborsClassifier(n_neighbors = 11)
predictors = ['Lag1', 'Lag2', 'Lag3', 'Lag4', 'Lag5']
model.fit(smarket_train[predictors], smarket_train['Direction'])
pickle.dump(model, open('ml_knn_model.pkl', 'wb'))

model = pickle.load(open('ml_knn_model.pkl', 'rb'))
print("Model Object: ", model)
test_arr = np.array([[-0.134,0.008,-0.007,0.715,-0.431]])
x = smarket_test[predictors].head().shape
predictions = model.predict(test_arr)
print(predictions)
