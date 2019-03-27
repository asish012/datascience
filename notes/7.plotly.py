
# coding: utf-8
import numpy as np
import pandas as pd

import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
get_ipython().magic('matplotlib inline')

# connect js to this notebook. because plotly connects pandas and python with interactive js lib.
init_notebook_mode(connected=True)
# cufflinks offline
cf.go_offline()

# data
df1 = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
df1.head()

df2 = pd.DataFrame({'Category': 'A B C '.split(), 'Values': [32, 43, 54]})
df2.head()

# simple line plot
df1.iplot()

# scatter plot
df1.iplot(kind='scatter', x='A', y='B', mode='markers')

# bar plot
df2.iplot(kind='bar', x='Category', y='Values')

# run some aggregate function on df and then plot. like a group by when the data is not in nice formate.
df1.sum().iplot(kind='bar')

# box plot
df1.iplot(kind='box')

# box plot for certain columns
df1[['A', 'B']].iplot(kind='box')

# 3D plot (surface plot)
df1[['A', 'B', 'C']].iplot(kind='surface', colorscale='rdylbu')

# histogram on particular column
df1['A'].iplot(kind='hist', bins=30)

# histogram on entire df. it overlaps one column over another
df1.iplot(kind='hist', bins=25)

# spread plot (stock chart like). it also shows line plot by default.
df1[['A', 'B']].iplot(kind='spread')

# bubble plot (similar to scattered plot)
df1.iplot(kind='bubble', x='A', y='B', size='C')

# scatter matrix plot (similar to seaborn's pairplot). all columns must be numerical.
df.scatter_matrix()

