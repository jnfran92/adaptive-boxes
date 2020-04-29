
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import genfromtxt

data = genfromtxt('/Users/Juan/Desktop/Tesis Model/prepros/humboldt_binary_matrix.csv', delimiter=',')

# plt.scatter(data)

plt.subplot(111)
plt.imshow(data, cmap='Greys',  interpolation='nearest')

