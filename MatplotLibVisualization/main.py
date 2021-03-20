import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from numpy import random as rand

x = np.linspace(0, 5, 11)
y = x ** 2

# Functional Method
plt.plot(x, y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')

# Multi Plots SUBPLOT
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')

plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')
# plt.show()

# Object Oriented Method
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y)
axes.set_xlabel('X label')
axes.set_ylabel('Y l Label')
axes.set_title('Title')

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.4])

axes1.plot(x, y)
axes1.set_title('Larger Plot')

axes2.plot(y, x)
axes2.set_title('Smaller Plot')

fig.show()

# Create subplot with OOP
fig, axes = plt.subplot(nrows=1, ncols=2)
axes.plot(x, y)

plt.tight_layout()  # Fixes Overlapping

for current_axe in axes:
    current_axe.plot(x, y)  # Iterating through axes

axes[0].plot(x, y)
axes.set_title('First Plot')

axes[1].plot(y, x)
axes.set_title('Second Plot')  # Indexing the axes

# Aspect Ratio and DPI
fig, axes = plt.size.figure(figsize=(8, 2))
ax = fig.add_axes([0, 0, 1, 1])

# saving a figure to a file
fig.save('my_picture.png')  # Choose between jpeg, png, vector and so on

fig = plt.figure()
fig.add_axes([0, 0, 1, 1])
ax.plot(x, x**2, label="X Squared")
ax.plot(y, x**3, label='X Cubed')

ax.legend(loc=0) # Sets the location of your legend

# setting Colors, Line Widths and Line Types
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y, color='Orange', linewidth=2, linestyle='--', marker='+', markersize='4',
        markerfacecolor='red', markeredgewidth=3, markeredgecolor='green')  # RGB Hex Code for Colors

# Control over axis appearance and plot range
ax.plot(x, y, color='purple', lw=2, ls='--')
ax.set_xlim([0, 1])
ax.set_ylim([0, 2])

# PANDAS VISUALIZATION

df1 = pd.read_csv('df1', index_col=0)
df1.head()

df1['A'].hist(bins=30)

df1['A'].plot(kind='hist', bins=30)

df1['A'].plot.hist()

df1.plot.area()

df1.plot.area(alpha=0.4)

df1.plot.bar(stacked=True)

df1['A'].plot.hist(bins=50)

df1.plot.line(x=df1.index, y='B', figsize=(12, 3), lw=1)

df1.plot.scatter(x='A', y='B', s=df1['C']*100)

df1.plot.box()

df = pd.DataFrame(np.random.randn(1000, 2, columns=['A', 'B']))

df.plot.hexbin(x='A', y='B', gridsize=25, cmap='coolwarm')

df1.plot.density()

# PANDAS WITH TIME SERIES

see = pd.read_csv(r'C:\Users\wwstudent\Downloads\Python-for-Finance-Repo-master.zip\Python-for-Finance-Repo-master\05'
                  r'-Pandas-with-Time-Series\time_data')
see.to_csv('mcdon')
print(pd.read_csv('mcdon'))

