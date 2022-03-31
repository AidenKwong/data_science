import pandas as pd
import numpy as np
# from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/MedicalCharges.csv')

plt.xlabel('age')
plt.ylabel('charges')
plt.scatter(df.age,df.charges,marker='.')

new_df = df.drop('charges',axis='columns')
charges = df.charges

reg = linear_model.LinearRegression()
reg.fit(new_df,charges)

print(reg.predict([[51]]),reg.coef_,reg.intercept_)
plt.plot(df.age, reg.coef_*df.age + reg.intercept_)
plt.show()
