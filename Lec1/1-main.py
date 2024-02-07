#!/usr/bin/python3
from matplotlib import pyplot
from pandas.plotting import scatter_matrix
Iris = __import__('BaseClass').Base
iris = Iris('iris.csv', ['pe_len', 'pe_wid', 'se_len', 'se_wid', 'class'])


try:
    print(' Shape '.center(30, '-'))
    print(iris)
    print(' Info '.center(30, '-'))
    print(repr(iris))
    print(' Describe '.center(30, '-'))
    print(iris.describe('class'))

    print(' Max, Min and Mean'.center(30, '*'))
    print(iris.dataset.groupby('class').max(), end='\n-------\n')
    print(iris.dataset.groupby('class').min(), end='\n-------\n')
    print(iris.dataset.groupby('class').mean())

    # ----------------
    # --- Diagrams ---
    # ----------------

    iris.dataset.plot(kind='box', subplots=True, layout=(2, 2))
    pyplot.show()

    iris.dataset.hist()
    pyplot.show()

    scatter_matrix(iris.dataset)
    pyplot.show()

except Exception as e:
    print(f"An error occured: {e}")

import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset('iris')

# Create pairplot with hue='species' to color by species
sns.pairplot(iris, hue='species')

# Show the plot
plt.show()


# import sklearn.datasets

# data, target = sklearn.datasets.load_iris(return_X_y=True, as_frame=True)
# data["target"] = target
# print(data)