from core.Exponential import Exponential
from core.Linear import Linear
from core.Ploynomial import Polynomial
from core.Power import Power
from core_temp.Expotential import Exponential as temp_EXP
from core_temp.Power import Power as temp_Power
from core_temp.Linear import Linear as temp_linear
from core_temp.Polynomial import Polynomial as temp_polynomial
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
    for item in crop_list:
       temp_EXP.run(item)
    # for item in crop_list:
    #     Linear.run(item)
    #
    # for item in crop_list:
    #     Polynomial.run(item)
    #
    # for item in crop_list:
    #     Power.run(item)
    #
    # for item in crop_list:
    #     Exponential.run(item)
