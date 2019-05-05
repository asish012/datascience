
# coding: utf-8

import seaborn as sns
import numpy as np
get_ipython().magic('matplotlib inline')


# Distribution Plots
# 1. distplot()    [single variable]
# 2. jointplot()   [two variable]
# 3. pairplot()    [all numarical column agains each other]
# .. rugplot()
# .. kdeplot()

tips = sns.load_dataset('tips')

tips.head()

# Single column (single variable) plot. also known as histogram
sns.distplot(tips['total_bill'], kde=False, bins=25).grid(True)

sns.rugplot(tips['total_bill'])

# Two column (two variable) plot
sns.jointplot(x='total_bill', y='tip', data=tips)

# Jointplot with Hexagon
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')

# Jointplot with Linear Regression
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')

sns.pairplot(data=tips, hue='sex', palette='coolwarm')

# Kernel Density Estimation of a column
sns.kdeplot(tips['total_bill'])


# Categorical Plots (a categorical column agains either a categorical or a numerical column)
# 1. barplot      [categorycal column vs categorical/numerical column]
# 2. countplot    [counts number of occurances for each category]
# 3. boxplot      [categorical axis (x) can be sub devided by another category using hue]
# 4. violinplot   [similar to box plot]
# 5. stripplot    [a scatterplot where x axis is categorical data. you can also split primary category with another category using hue]
# 6. swarmplot    [violinplot like stripplot]
# +. factorplot   [magic function to create any plot using the parameter 'kind']

tips.head()

# A categorical column agains a numerical column
sns.barplot(x='sex', y='total_bill', data=tips)

# barplot with standard deviation estimator
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

sns.countplot(x='sex', data=tips)

# categorical vs numeric. and the primary category is split into other categorical column
sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')

sns.violinplot(x='day', y='total_bill', data=tips, hue='smoker', split=True)

sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', split=True)

sns.swarmplot(x='day', y='total_bill', data=tips, hue='sex')

sns.violinplot(x='day', y='total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data=tips, color='black')


# Matrix Plots (data should be in matrix form)
# 1. heatmap    [requires a matrix like data, similar to excel-spreadsheet with row and columns]
# 2. clustermap [shows matrix data as hierarchical data where similar data are closed to each other]

flights = sns.load_dataset('flights')

flights.head()

# For heatmap we must have one of the column value as row names which will form matrix with an existing column.
# and another column would be the actual value. Similar to excel-sheet: cell-value = C12 = column-row.
# Here we'll transform years as row names, and use passengers as the value for each matrix cell.

# pivot_table() helps us to transform flights data into a spreadsheet-style pivot table as a DataFrame.
fp = flights.pivot_table(index='year', columns='month', values='passengers')

sns.heatmap(fp)

sns.heatmap(fp, cmap='magma', linewidth=1, linecolor='white')

sns.clustermap(fp)

sns.clustermap(fp, standard_scale=1)


# Regration plots (machinelearning topic)
# 1. lmplot    [linier model plot]

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex')

sns.lmplot(x='total_bill', y='tip', data=tips, col='sex')

sns.lmplot(x='total_bill', y='tip', data=tips, col='day', row='time', hue='sex')

# Grids

