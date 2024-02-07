#!/usr/bin/python3
from pandas import read_csv


class Base:
    """ All methods in one place """

    def __init__(self, path, col):
        """ Initializing method """

        self.dataset = read_csv(path, names=col)

    def __str__(self):
        """ Total rows & columns """
        return f'{self.dataset.shape}'

    def __repr__(self):
        """ Data info """
        return f"{self.dataset.info()}"

    def describe(self, clscify=None):
        """ Data analysing """
        if clscify is None:
            return self.dataset.describe()
        else:
            try:
                return self.dataset.groupby(clscify).describe()
            except KeyError:
                raise KeyError(f"{clscify} not found")
            except Exception as e:
                raise f'{e}'

    def head(self, num=10):
        return self.dataset.head(num)

