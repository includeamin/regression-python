import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas


def func(x, a, b):
    return a * x + b


class Linear:
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
        print(ss_reg / sst)
        print('---')
        plt.title(f"Linear of {file_name}")
        new_x = np.linspace(0, max(x), 200)

        plt.plot(new_x, func(new_x, *popt), 'r--',
                 label=f'y = {"{0:.4f}".format(popt[0])}x + {"{0:.4f}".format(popt[1])} , RS {"{0:.4f}".format(ss_reg / sst)}')
        plt.plot(x, y, 'x')
        plt.xlabel('ET/Etmax')
        plt.ylabel('Y/Ymax')
        plt.legend()
        plt.savefig(f'./output/{file_name}-{Linear.__name__}.png')

        plt.show()
