import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import pandas
from sklearn.metrics import r2_score


class Linear:
    @staticmethod
    def run(file_name):
        data = pandas.read_csv(f'./data/{file_name}')
        y = np.array([item for item in data['Y/Ymax']])
        x = np.array([item for item in data['ET/Etmax']])
        x = np.array(x).reshape((-1, 1))
        y = np.array(y)
        model = LinearRegression().fit(x, y)
        # r_sq = model.score(x, y)
        plt.scatter(x, y, color='g')
        temp = model.predict(x)
        r_sq = model.score(x, y)
        # r_sq = r =r2_score(temp,y)

        plt.plot(x, temp, color='k')
        plt.title("Linear Regression")
        plt.xlabel('ET/Etmax', fontsize=11)
        plt.ylabel('Y/Ymax', fontsize=11)
        plt.tight_layout()
        plt.text(.001, .7, f"R Square {'%.4f' % r_sq}", fontsize=12)
        plt.show()
