"""
for data visualizations
"""

import numpy

def path_2d_numpy(x, y):
    m1, m2 = numpy.meshgrid(x, y)
    m1[1::2] = m1[1::2,::-1]
    r = numpy.append(m1, m2)
    r.shape = 2,-1
    return r.T

from matplotlib import lines
from matplotlib import pyplot

def plot_path_2d(path):
    x, y = path.T
    pyplot.plot(x, y, '-ro', lw=3)
    pyplot.show()

x = numpy.linspace(4, 1, 4)
y = numpy.linspace(1, 5, 5)
path = path_2d_numpy(x, y)
plot_path_2d(path)
