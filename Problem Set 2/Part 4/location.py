allpairs = list((x,y) for x in range(99) for y in range(99))

# or with Py2.6 or later:
from itertools import product
allpairs = list(product(range(99),range(99)))

# or even taking DRY to the extreme
allpairs = list(product(*[range(99)]*2))

from random import shuffle
shuffle(allpairs)

n = 100
import numpy as np
trainingset = allpairs[:n]

print(trainingset)

