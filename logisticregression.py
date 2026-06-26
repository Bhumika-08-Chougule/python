import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_cvs("data.csv")

x =data[['x1','x2']]
y= data['y'] 

model = LogisticRegression()
model.fit(x,y)

x_new = [[5,10]]
y_pred = model.predict(x_new)

print(model.coef_)
print(model.intercept_)
print(y_pred)