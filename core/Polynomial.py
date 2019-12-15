import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas


def func(x, a, b, c):
    return a * x ** 2 + b * x + c


def getEquidistantPoints(p1, p2, parts):
    return zip(np.linspace(p1[0], p2[0], parts + 1), np.linspace(p1[1], p2[1], parts + 1))


class Polynomial:
    @staticmethod
    def run(file_name):
        data = pandas.read_csv(f'./data/{file_name}')
        data = data.sort_values(by='ET/Etmax')

        y = np.array([item for item in data['Y/Ymax']])
        x = np.array([item for item in data['ET/Etmax']])
        new_x = np.linspace(0, max(x), 200)
        popt, pcov = curve_fit(func, x, y)
        y_bar = np.sum(y) / len(y)
        sst = 0.0
        for i in range(len(y)):
            sst += pow(y[i] - y_bar, 2)
        ss_reg = 0.0
        y_hat = func(x, *popt)
        for i in range(len(y_hat)):
            ss_reg += pow(y_hat[i] - y_bar, 2)
        print('---')
        plt.title(f"Polynomial of {file_name}")
        plt.plot(new_x, func(new_x, *popt), 'r-',
                 label=f'y = {"{0:.4f}".format(popt[0])}x^2 + {"{0:.4f}".format(popt[1])}x + {"{0:.4f}".format(popt[2])}\n'
                       f' RS {"{0:.4f}".format(ss_reg / sst)}')
        plt.plot(x, y, 'x')
        plt.xlabel('ET/Etmax')
        plt.ylabel('Y/Ymax')
        plt.legend()
        plt.savefig(f'./output/{file_name}-{Polynomial.__name__}.png')
        plt.show()

# top = len(x) * (np.sum(x * y) - np.sum(x) * np.sum(y))
# under = len(x) * np.sum(np.power(x, 2)) - np.power(np.sum(x), 2) - \
#         len(x) * np.sum(np.power(y, 2)) - np.power(np.sum(y), 2)
#
# r = top / under ** 1 / 2
# print(r**2)
