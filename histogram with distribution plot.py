"""
@Author: Mamunur Rahman
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.stats import norm

df1=pd.read_csv('Baseline_city.csv', delimiter = ',')
df2=pd.read_csv('Moderate_city.csv', delimiter = ',')
df3=pd.read_csv('Low_city.csv', delimiter = ',')
df1.head()

fig = plt.figure(constrained_layout=True, figsize=(9,5))
gs = GridSpec(2, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, 0:2])
ax2 = fig.add_subplot(gs[0, 2:])
ax3 = fig.add_subplot(gs[1, 1:3])

size=11 #font size



## peak hour volume
# create data for GV, EV, and PHEV
xs = [df1.GV, df1.EV, df1.PHEV]
n_bins = [20, 8, 20]
colors = ['b', 'g', 'orange']
labels = ['GV ($\overline {X}$=337.8)', 'EV ($\overline {X}$=149.7)', 'PHEV ($\overline {X}$=199.1)']

for i, x in enumerate(xs):
    n, bins, patches = ax1.hist(x, bins=n_bins[i], color=colors[i],
                                edgecolor='w', density=True, alpha=0.8,
                                label=labels[i])
    # add a 'best fit' line
    mu = x.mean()
    sigma = x.std(ddof=1)
    y = norm.pdf(bins, mu, sigma)
    ax1.plot(bins, y, linestyle='--', color='r')

# put legend
ax1.legend(fontsize=9, loc='upper center')
#put axis labels
ax1.set_xlabel('CO\N{SUBSCRIPT TWO} emission (g/km)', fontsize=size)
ax1.set_ylabel('Probability density', fontsize=size)
ax1.set_title('Peak hour traffic', fontsize=size, color='b')


## moderate volume
# create data for GV, EV, and PHEV
xs = [df2.GV, df2.EV, df2.PHEV]
#n_bins = [7, 5, 5]
n_bins = [13, 12, 6]
colors = ['b', 'g', 'orange']
labels = ['GV ($\overline {X}$=291.1)', 'EV ($\overline {X}$=143.3)', 'PHEV ($\overline {X}$=172.3)']

for i, x in enumerate(xs):
    n, bins, patches = ax2.hist(x, bins=n_bins[i], color=colors[i],
                                edgecolor='w', density=True, alpha=0.8,
                                label=labels[i])
    # add a 'best fit' line
    mu = x.mean()
    sigma = x.std(ddof=1)
    y = norm.pdf(bins, mu, sigma)
    ax2.plot(bins, y, linestyle='--', color='r')

# put legend
ax2.legend(fontsize=9, loc='upper center')
#put axis labels
ax2.set_xlabel('CO\N{SUBSCRIPT TWO} emission (g/km)', fontsize=size)
ax2.set_ylabel('Probability density', fontsize=size)
ax2.set_title('Moderate traffic', fontsize=size, color='b')



## low volume
# create data for GV, EV, and PHEV
xs = [df3.GV, df3.EV, df3.PHEV]
#n_bins = [6, 8, 5]
n_bins = [10, 10, 5]
colors = ['b', 'g', 'orange']
labels = ['GV ($\overline {X}$=271.5)', 'EV ($\overline {X}$=140.6)', 'PHEV ($\overline {X}$=160.2)']

for i, x in enumerate(xs):
    n, bins, patches = ax3.hist(x, bins=n_bins[i], color=colors[i],
                                edgecolor='w', density=True, alpha=0.8,
                                label=labels[i])
    # add a 'best fit' line
    mu = x.mean()
    sigma = x.std(ddof=1)
    y = norm.pdf(bins, mu, sigma)
    ax3.plot(bins, y, linestyle='--', color='r')

# put legend
ax3.legend(fontsize=9, loc='upper center')
#put axis labels
ax3.set_xlabel('CO\N{SUBSCRIPT TWO} emission (g/km)', fontsize=size)
ax3.set_ylabel('Probability density', fontsize=size)
ax3.set_title('Low traffic', fontsize=size, color='b')


#super title of the subplots
fig.suptitle("(a)  City driving", fontweight="bold", size=12)

fig.savefig("CO2 emission histogram_city.png", dpi=300, bbox_inches='tight')

