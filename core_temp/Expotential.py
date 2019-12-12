import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas


def func(x, a, b):
    return a * np.exp(b * x)


def r2():
    pass


class Exponential:
    @staticmethod
    def run(file_name):
        data = pandas.read_csv(f'./data/{file_name}')
        y = np.array([item for item in data['Y/Ymax']])
        x = np.array([item for item in data['ET/Etmax']])
        popt, pcov = curve_fit(func, x, y)
        plt.title(f"Exponential of {file_name}")
        plt.plot(x, func(x, *popt), 'r--', label=f'y = {popt[0]}E^{popt[1]}*X')
        plt.plot(x, y, 'x')
        plt.xlabel('ET/Etmax')
        plt.ylabel('Y/Ymax')
        plt.legend()
        plt.show()
