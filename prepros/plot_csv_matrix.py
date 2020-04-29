
import matplotlib.pyplot as plt
from numpy import genfromtxt

data = genfromtxt('/Users/Juan/Desktop/Tesis Model/prepros/humboldt_binary_matrix.csv', delimiter=',')

plt.subplot(111)
plt.imshow(data, cmap='Greys',  interpolation='nearest')

