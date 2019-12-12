import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


class Exponential:
    @staticmethod
    def run(file_name):
        data = pandas.read_csv(f'./data/{file_name}')
        y = np.array([item for item in data['Y/Ymax']])
        x = np.array([item for item in data['ET/Etmax']])
        popt, pcov = curve_fit(func, x, y)
        print(popt)
        plt.plot(x, func(x, *popt), 'r-',
                 label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
        plt.plot(x, y, 'x')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()
