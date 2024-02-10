#!/usr/bin/python3
import pandas as pd
import numpy as np
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# from sklearn.preprocessing import PolynomialFeatures

dataset1 = pd.read_csv('salaries2.csv')

x_axis = dataset1.values[ : , 0]
y_axis = dataset1.values[ : , 1]

""" Get correlation coefficients of Salaries1(r1)"""
r1 = np.corrcoef(x_axis, y_axis)
print(r1)

"""
    Finding the mathematical relationship
"""
x_train, x_test, y_train, y_test = train_test_split(x_axis, y_axis, test_size=0.25, random_state=1)

lin_reg = LinearRegression()
lin_reg.fit(x_train.reshape(-1, 1), y_train.reshape(-1, 1))

# """ Test linear eaquation exist or not """
predict_output = lin_reg.predict(x_test.reshape(-1, 1))
# print(y_test)
# print('-' * 20)
# print(predict_output)

pyplot.scatter(x_axis, y_axis)
pyplot.plot(x_test, predict_output, color='red')
pyplot.show()

"""
    Built in function calc error rate
    between actual output and predicted one
    ``mean_squared_error``
"""

print(mean_squared_error(y_test, predict_output))
