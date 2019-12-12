
from core.Exponential import Exponential
from core.Linear import Linear
from core.Ploynomial import Polynomial
from core.Power import Power
crop_list = [
    'grainmaize.csv',
    "Apple.csv",
    "grainmaize.csv",
    "rice.csv",
    "soybean.csv",
    'srgum.csv',
    'tomato.csv',
    'wheat.csv'
]

if __name__ == '__main__':
    for item in crop_list:
        Linear.run(item)
