import numpy as np
from numpy import linspace
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import pandas
from sklearn.metrics import r2_score
from scipy.stats import expon


class Exponential:
    @staticmethod
    def run(file_name):
        data = pandas.read_csv(f'./data/{file_name}')
        y = np.array([item for item in data['Y/Ymax']])
        x = np.array([item for item in data['ET/Etmax']])

        popt, pcov = curve_fit(lambda fx, a, b: a * fx ** -b, x, y)
        power_y = popt[0] * x ** -popt[1]

        plt.scatter(x, y, label='actual data')
        plt.plot(x, power_y, label='power-fit')
        plt.legend()
        plt.show()
