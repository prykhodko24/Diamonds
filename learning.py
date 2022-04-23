from import_and_clean import data
import pandas as pd
import sklearn.model_selection
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
Y = data['price']
X = data.drop(columns='price')

X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(
X, Y, test_size=0.1, random_state=42)
X_train, X_valid, Y_train, Y_valid =sklearn.model_selection.train_test_split(
X_train, Y_train, test_size=0.111, random_state=42)

#-------------------------------------------
lasso = linear_model.Lasso(alpha=1, normalize=True)
lasso.fit(X_train, Y_train)
coefs = lasso.coef_
intercept = lasso.intercept_


pd.DataFrame(data=np.expand_dims(coefs, 0), columns=X_train.columns)
r2_train = lasso.score(X_train, Y_train)
r2_valid = lasso.score(X_valid, Y_valid)
# print(r2_train, r2_valid)
alpha_arr = [10000, 1000, 500, 200, 100, 50, 10, 5, 1, 0.5, 0.1, 0.05, 0.01]
model = []
r2_res=0
for alpha in alpha_arr:
    lasso = linear_model.Lasso(alpha=alpha)
    lasso.fit(X_train, Y_train)
    model.append(lasso)
    r2 = lasso.score(X_valid, Y_valid)
    if alpha==alpha_arr[12]:
        r2_res=r2
    # print(f"Якщо alpha = {alpha}, то R = {r2}")
lasso = model[12]

coef = lasso.coef_
intercept = lasso.intercept_
pd.DataFrame(data=np.expand_dims(coefs, 0), columns=X_train.columns)
a=X_test.head(1)
Y_pred = lasso.predict(X_test)
results = pd.DataFrame({'Price(test)': np.squeeze(abs(Y_test)),'Price(pred)':abs(Y_pred)})
