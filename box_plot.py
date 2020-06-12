"""
@Author: Mamunur Rahman
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib as mpl

df1=pd.read_csv('Results_baseline_scenario_replications.csv', delimiter = ',')

fig = plt.figure(constrained_layout=True, figsize=(10,4))
gs = GridSpec(1, 7, figure=fig)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])
ax4 = fig.add_subplot(gs[0, 3])
ax5 = fig.add_subplot(gs[0, 4])
ax6 = fig.add_subplot(gs[0, 5])
ax7 = fig.add_subplot(gs[0, 6])



size=11 #font size


# search time----------------------------------------------------------------------------
ax1.boxplot([df1.Search_time, df2.Search_time], vert=True, widths = 0.7)
ax1.set_ylabel('Search time (seconds)', fontsize=size, color='b')
ax1.set_xticks( [1,2])
ax1.set_xticklabels(['Baseline', 'Crowdinforming'], fontsize=size, rotation='vertical')
ax1.yaxis.set_tick_params(labelsize=size)

# distance driven----------------------------------------------------------------------------
ax2.boxplot([df1.Distance_driven, df2.Distance_driven], vert=True, widths = 0.7)
ax2.set_ylabel('Distance driven (miles)', fontsize=size, color='b')
ax2.set_xticks( [1,2])
ax2.set_xticklabels(['Baseline', 'Crowdinforming'], fontsize=size, rotation='vertical')
ax2.yaxis.set_tick_params(labelsize=size)

# Fuel burnt----------------------------------------------------------------------------
ax3.boxplot([df1.Fuel, df2.Fuel], vert=True, widths = 0.7)
ax3.set_ylabel('Fuel burnt (ml)', fontsize=size, color='b')
ax3.set_xticks( [1,2])
ax3.set_xticklabels(['Baseline', 'Crowdinforming'], fontsize=size, rotation='vertical')
ax3.yaxis.set_tick_params(labelsize=size)

# CO2----------------------------------------------------------------------------
ax4.boxplot([df1.CO2, df2.CO2], vert=True, widths = 0.7)
ax4.set_ylabel('CO\N{SUBSCRIPT TWO} (grams)', fontsize=size, color='b')
ax4.set_xticks( [1,2])
ax4.set_xticklabels(['Baseline', 'Crowdinforming'], fontsize=size, rotation='vertical')
ax4.yaxis.set_tick_params(labelsize=size)

# CO----------------------------------------------------------------------------
ax5.boxplot([df1.CO, df2.CO], vert=True, widths = 0.7)
ax5.set_ylabel('CO (grams)', fontsize=size, color='b')
ax5.set_xticks( [1,2])
ax5.set_xticklabels(['Baseline', 'Crowdinforming'], fontsize=size, rotation='vertical')
ax5.yaxis.set_tick_params(labelsize=size)

# NOx----------------------------------------------------------------------------
ax6.boxplot([df1.NOX, df2.NOX], vert=True, widths = 0.7)
ax6.set_ylabel('NOx (grams)', fontsize=size, color='b')
ax6.set_xticks( [1,2])
ax6.set_xticklabels(['Baseline', 'Crowdinforming'], fontsize=size, rotation='vertical')
ax6.yaxis.set_tick_params(labelsize=size)

# HC----------------------------------------------------------------------------
ax7.boxplot([df1.HC, df2.HC], vert=True, widths = 0.7)
ax7.set_ylabel('HC (grams)', fontsize=size, color='b')
ax7.set_xticks( [1,2])
ax7.set_xticklabels(['Baseline', 'Crowdinforming'], fontsize=size, rotation='vertical')
ax7.yaxis.set_tick_params(labelsize=size)


# change the boxplot and outlier style----------------------------------------------------
mpl.rcParams['boxplot.whiskerprops.linestyle'] = '--'
mpl.rcParams['boxplot.boxprops.color'] = 'r'
mpl.rcParams['boxplot.whiskerprops.color'] = 'r'
mpl.rcParams['boxplot.flierprops.markeredgecolor'] = 'r'
mpl.rcParams['boxplot.flierprops.marker'] = 'o'

fig.savefig("Box plot_parking project", dpi=300, bbox_inches='tight')

