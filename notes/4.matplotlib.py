# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# see plots inline within notebook. outside notebooks you'd have to write > plt.show()
get_ipython().magic('matplotlib inline')

x = np.linspace(0, 5, 11)
y = x ** 2

# there are two ways to plot.
    # 1: Functional method
    # 2: Object oriented method

# Functional method:
plt.plot(x, y)

# adding labels
plt.xlabel('x')
plt.ylabel('y')
plt.title('simple x y plot')
plt.plot(x, y, 'r')

# multiple plots (as a grid) at once using subplot(nrows, ncols, plot_number)
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')

plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')


# Object oriented method using a figure object. # A figure object can be imagined as a blank canvas.
fig = plt.figure()
axes = fig.add_axes([0, 0, 1, 1])
axes.set_title('simple object oriented plot')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.plot(x, y)

# Nested plots using object oriented method
fig = plt.figure()
axes1 = fig.add_axes([0, 0, 1, 1])
axes2 = fig.add_axes([.1, .5, .4, .4])

axes1.set_title('large plot')
axes1.plot(x, y)

axes2.set_title('inner plot')
axes2.plot(y, x)

# Multi plot using subplots(nrows, ncols)
fig, new_axes = plt.subplots(nrows=1, ncols=2)
new_axes[0].set_title('plot 1')
new_axes[0].set_xlabel('x')
new_axes[0].set_ylabel('y')
new_axes[0].plot(x, y)
plt.tight_layout()

# for a in new_axes:
#     a.plot(x, y)
