import numpy as np
from numpy import linspace
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import pandas
from sklearn.metrics import r2_score


class Power:
    @staticmethod
    def run(file_name):
        data = pandas.read_csv(f'./data/{file_name}')
        y = np.array([item for item in data['Y/Ymax']])
        x = np.array([item for item in data['ET/Etmax']])
        x = np.array(x)
        y = np.array(y)

        def func(x, a, b):
            return a * (b ** x)

        popt, pcov = curve_fit(lambda fx, a, b: a * fx ** -b, x, y)
        print(popt, pcov)
        x_linspace = np.linspace(0, max(x), len(y))
        power_y = popt[0] * x ** -popt[1]
        plt.scatter(x, y, label='actual data')
        plt.plot(x_linspace, power_y, label='power-fit')
        r = r2_score(y, power_y)
        plt.text(.001, .8, f" R2 = {r}", fontsize=12)
        plt.title("POWER Regression")
        plt.xlabel('ET/Etmax', fontsize=11)
        plt.ylabel('Y/Ymax', fontsize=11)
        plt.text(.001, .7, f"R Square {'%.4f' % r}", fontsize=12)
        # plt.tight_layout()
        plt.legend()
        plt.show()
