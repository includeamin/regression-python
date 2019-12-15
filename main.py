from core.Expotential import Exponential as temp_EXP
from core.Power import Power as temp_Power
from core.Linear import Linear as temp_linear
from core.Polynomial import Polynomial as temp_polynomial

crop_list = [
    'grainmaize.csv',
    "Apple.csv",
    "citrus.csv",
    "rice.csv",
    "soybean.csv",
    'srgum.csv',
    'tomato.csv',
    'wheat.csv'
]

if __name__ == '__main__':
    # for item in crop_list:
    #     temp_polynomial.run(item)
    for item in crop_list:
        temp_EXP.run(item)
    # for item in crop_list:
    #     temp_linear.run(item)
    # for item in crop_list:
    #     temp_Power.run(item)
