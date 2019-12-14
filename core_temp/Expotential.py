import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas
import math


def func(x, a, b):
    # return a * math.e ** b * x
    return a * np.exp(b * x)


class Exponential:
    @staticmethod
    def run(file_name):
        data = pandas.read_csv(f'./data/{file_name}')
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
        print('---')
        d= ss_reg / sst
        plt.title(f"Polymonial of {file_name} , RS {'{0:.4f}'.format(d)}")
        power_y = popt[0] * np.exp(x * popt[1])
        print(len(y))
        print(len(power_y))
        print(power_y)
        plt.plot(x, power_y, 'r-', label=f'y = {popt[0]}^{popt[1]}*X')
        plt.plot(x, y, 'x')
        plt.xlabel('ET/Etmax')
        plt.ylabel('Y/Ymax')
        plt.legend()
        plt.show()
    # @staticmethod
    # def run(file_name):
    #
#         # import matplotlib.pyplot as plt
#         # import numpy as np
#         #
#         # T = np.array([6, 7, 8, 9, 10, 11, 12])
#         # power = np.array([1.53E+03, 5.92E+02, 2.04E+02, 7.24E+01, 2.72E+01, 1.10E+01, 4.70E+00])
#         # xnew = np.linspace(T.min(), T.max(), 300)  # 300 represents number of points to make between T.min and T.max
#         #
#         # power_smooth = spline(T, power, xnew)
#         #
#         # plt.plot(xnew, power_smooth)
#         # plt.show()
#         data = pandas.read_csv(f'./data/{file_name}')
#         y = np.array([item for item in data['Y/Ymax']])
#         x = np.array([item for item in data['ET/Etmax']])
#         popt, pcov = curve_fit(func, x, y)
#
#         y_bar = np.mean(y)
#         sst = 0.0
#         for i in range(len(y)):
#             sst += pow(y[i] - y_bar, 2)
#         ss_reg = 0.0
#         y_hat = func(x, *popt)
#         for i in range(len(y_hat)):
#             ss_reg += pow(y_hat[i] - y_bar, 2)
#         print(ss_reg / sst)
#         print('---')
#         xx = np.linspace(x.min(), x.max(), num=len(y))
#         plt.title(f"Exponential of {file_name}")
#         plt.plot(xx, func(x, *popt), 'r--', label=f'y = {popt[0]}E^{popt[1]}*X \n, RS {ss_reg / sst}')
#         plt.plot(x, y, 'x')
#         plt.xlabel('ET/Etmax')
#         plt.ylabel('Y/Ymax')
#         plt.legend()
#         plt.show()
#
# # top = len(x) * (np.sum(x * y) - np.sum(x) * np.sum(y))
# # under = len(x) * np.sum(np.power(x, 2)) - np.power(np.sum(x), 2) - \
# #         len(x) * np.sum(np.power(y, 2)) - np.power(np.sum(y), 2)
# #
# # r = top / under ** 1 / 2
# # print(r**2)
