import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas


def func(x, a, b):
    return a * np.exp(b * x)


class Exponential:
    @staticmethod
    def run(file_name):
        data = pandas.read_csv(f'./data/{file_name}')
        data = data.sort_values(by='ET/Etmax')
        y = np.array([item for item in data['Y/Ymax']])
        x = np.array([item for item in data['ET/Etmax']])
        popt, pcov = curve_fit(func, x, y)

        y_bar = np.sum(y) / len(y)
        sst = 0.0
        for i in range(len(y)):
            sst += pow(y[i] - y_bar, 2)
        ss_reg = 0.0
        y_hat = func(x, *popt)
        for i in range(len(y_hat)):
            ss_reg += pow(y_hat[i] - y_bar, 2)
        d = ss_reg / sst
        plt.title(f"Exponential of {file_name} , RS {'{0:.4f}'.format(d)}")
        new_x = np.linspace(0, max(x), 200)

        # xx = np.linspace(0, max(x), len(y))
        plt.plot(new_x, func(new_x, *popt), 'r-',
                 label=f'y = {"{0:.4f}".format(popt[0])}*e^{"{0:.4f}x".format(popt[1])}')
        plt.plot(x, y, 'x')
        plt.xlabel('ET/Etmax')
        plt.ylabel('Y/Ymax')
        plt.legend()
        plt.savefig(f'./output/{file_name}-{Exponential.__name__}.png')
        plt.show()
