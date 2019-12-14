import warnings

import numpy as np
from numpy import linspace
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import pandas
import numpy.polynomial.polynomial as poly
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score


class Polynomial:
    @staticmethod
    def run(file_name):
        data = pandas.read_csv(f'./data/{file_name}')
        y = np.array([item for item in data['Y/Ymax']])
        x = np.array([item for item in data['ET/Etmax']])
        import numpy
        z = np.polyfit(x, y, 2)
        p = np.poly1d(z)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', np.RankWarning)
            p30 = np.poly1d(np.polyfit(x, y, 2))
        yhat = p(x)  # or [p(z) for z in x]
        ybar = numpy.sum(y) / len(y)  # or sum(y)/len(y)
        ssreg = numpy.sum((yhat - ybar) ** 2)  # or sum([ (yihat - ybar)**2 for yihat in yhat])
        sstot = numpy.sum((y - ybar) ** 2)
        xp = np.linspace(0, 1, len(y))
        _ = plt.plot(x, y, '.', xp, p(xp), '-', xp, p30(xp), '--')
        r2 = ssreg / sstot
        plt.text(.001, .7, f"{file_name} {'%.4f' % r2}", fontsize=12)
        plt.show()
