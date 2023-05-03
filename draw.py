import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

data = pd.read_csv('data_set/canada_per_capita_income.csv')

reg_model_obj = linear_model.LinearRegression()
reg_model_obj.fit(data[["year"]], data["income"])

m = reg_model_obj.coef_ 
b = reg_model_obj.intercept_

predicted = reg_model_obj.predict(data[["year"]])

# y = mx+b
# line_data = m*data["year"]+b

plt.plot(data["year"], data["income"], color="red")
plt.plot(data["year"], predicted)
plt.xlabel("Years")
plt.ylabel("Income in USD")
plt.show()
