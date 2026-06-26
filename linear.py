import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_cvs("data.csv")

x =data[['x']]
y= data['y'] 

model = LinearRegression()
model.fit(x,y)

x_new = [[10]]
y_pred = model.predict(x_new)

print(model.coef_)
print(model.intercept_)
print(y_pred)