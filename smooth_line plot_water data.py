"""
@Author: Mamunur Rahman
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Data_water.csv', delimiter = ',')
df.head()

x = df['Month']
# convert month names from string to numeric type so that we can perform interpolation
x = np.arange(1, 13, 1)
ys = [df['Year 2016'], df['Year 2017'], df['Year 2018']]

colors = ['g', 'r', 'c']
labels = ['Year 2016', 'Year 2017', 'Year 2018']


for i, y in enumerate(ys):
    from scipy.interpolate import make_interp_spline
    # 100 represents number of points to make between x.min and x.max
    x_new = np.linspace(x.min(), x.max(), 100) 
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_new)
    plt.plot(x_new, y_smooth, color=colors[i], marker='o', linestyle='-', linewidth=1, markersize=4, markeredgecolor='k', label=labels[i])

label_texts = plt.xticks(np.arange(1, 13, 1), list(df['Month']), rotation = 45, horizontalalignment="center")
#horizontalalignment="center", "left", "right"
plt.xlabel('Month')
plt.ylabel('Cut off frequency')
plt.legend()
plt.tight_layout()
plt.savefig("Smooth line plot.png", dpi=300, bbox_inches='tight')

