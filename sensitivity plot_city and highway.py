
"""
@author: Mamunur Rahman
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

df1=pd.read_csv('Sensitivity_GV_city.csv', delimiter = ',')
df2=pd.read_csv('Sensitivity_EV_city.csv', delimiter = ',')
df3=pd.read_csv('Sensitivity_PHEV_city.csv', delimiter = ',')
df4=pd.read_csv('Sensitivity_GV_highway.csv', delimiter = ',')
df5=pd.read_csv('Sensitivity_EV_highway.csv', delimiter = ',')
df6=pd.read_csv('Sensitivity_PHEV_highway.csv', delimiter = ',')
df1.head()

fig = plt.figure(constrained_layout=True, figsize=(12,12))
gs = GridSpec(ncols=2, nrows=3, height_ratios=[1, .8, 1.3], figure=fig)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[2, 0])
ax4 = fig.add_subplot(gs[0, 1])
ax5 = fig.add_subplot(gs[1, 1])
ax6 = fig.add_subplot(gs[2, 1])

# font
font = {'fontname':'Calibri'}
# label font size
size = 14

############ CITY DRIVING  ###############################################################
# GV--------------------------------------
# name of the variables
variables = df1['variables']
# baseline values
base = 0
# low values in percentage
low = df1['low']*100
# high values in percentage
high = df1['high']*100

# position of the variables on y-axis
y_pos = np.arange(len(variables))

# create horizontal bar plot
ax1.barh(y_pos, high, align='center', left=base, height=0.9, color= 'orange', edgecolor='w', alpha =0.9, label='Increase parameter by 15%')
ax1.barh(y_pos, low, align='center', left=base, height=0.9, color= 'blue', edgecolor='w', alpha = 0.9, label='Decrease parameter by 15%')
ax1.set_yticks(y_pos)
ax1.set_yticklabels(variables, fontsize=size, **font)
# show the values of x tick labels in percentage
vals = ax1.get_xticks()
ax1.set_xticklabels(['{:,.0%}'.format(x/100) for x in vals], fontsize=size-4)
#ax1.set_xticks(np.linspace(-20, 20, 9))
ax1.set_xticks(np.arange(-20, 21, 5))
#ax1.grid(b=True, which='major', axis='x')
# set the x tick labels position
ax1.xaxis.set_ticks_position('bottom')

# Annotate the values
max_value = max([high.max(), low.max()])
min_value = min([high.min(), low.min()])
for i, v in enumerate(high):
    if v > 0:
        ax1.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax1.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)

for i, v in enumerate(low):
    if v > 0:
        ax1.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax1.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)


ax1.legend(fontsize=size-2, bbox_to_anchor=(0,1.15,1,0.22))
ax1.set_xlabel('Change of CO\N{SUBSCRIPT TWO} emission', fontsize=size, color='k', **font)
ax1.set_ylabel('Parameters', fontsize=size, color='k', **font)
ax1.set_title("(i) GV", color='b', fontsize=size+1, fontweight='bold')
ax1.text(-12, 9, '(a) City Driving', fontweight="bold", size=17)

# EV--------------------------------------
# name of the variables
variables = df2['variables']
# baseline values
base = 0
# low values in percentage
low = df2['low']*100
# high values in percentage
high = df2['high']*100

# position of the variables on y-axis
y_pos = np.arange(len(variables))

# create horizontal bar plot
ax2.barh(y_pos, high, align='center', left=base, height=0.9, color= 'orange', edgecolor='w', alpha =0.9, label='Increase parameter by 15%')
ax2.barh(y_pos, low, align='center', left=base, height=0.9, color= 'blue', edgecolor='w', alpha = 0.9, label='Decrease parameter by 15%')
ax2.set_yticks(y_pos)
ax2.set_yticklabels(variables, fontsize=size, **font)
# show the values of x tick labels in percentage
vals = ax2.get_xticks()
ax2.set_xticklabels(['{:,.0%}'.format(x/100) for x in vals], fontsize=size-4)
ax2.set_xticks(np.arange(-25, 21, 5))
#ax1.grid(b=True, which='major', axis='both')
# set the x tick labels position
ax2.xaxis.set_ticks_position('bottom')

# Annotate the values
max_value = max([high.max(), low.max()])
min_value = min([high.min(), low.min()])
for i, v in enumerate(high):
    if v > 0:
        ax2.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax2.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)

for i, v in enumerate(low):
    if v > 0:
        ax2.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax2.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)

#ax2.legend(fontsize=size-2, bbox_to_anchor=(0,1.06,1,0.22))
ax2.set_xlabel('Change of CO\N{SUBSCRIPT TWO} emission', fontsize=size, color='k', **font)
ax2.set_ylabel('Parameters', fontsize=size, color='k', **font)
ax2.set_title("(ii) EV", color='b', fontsize=size+1, fontweight='bold')

# PHEV--------------------------------------
# name of the variables
variables = df3['variables']
# baseline values
base = 0
# low values in percentage
low = df3['low']*100
# high values in percentage
high = df3['high']*100

# position of the variables on y-axis
y_pos = np.arange(len(variables))

# create horizontal bar plot
ax3.barh(y_pos, high, align='center', left=base, height=0.9, color= 'orange', edgecolor='w', alpha =.9, label='Increase parameter by 15%')
ax3.barh(y_pos, low, align='center', left=base, height=0.9, color= 'blue', edgecolor='w', alpha = .9, label='Decrease parameter by 15%')
ax3.set_yticks(y_pos)
ax3.set_yticklabels(variables, fontsize=size, **font)
# show the values of x tick labels in percentage
vals = ax3.get_xticks()
ax3.set_xticklabels(['{:,.0%}'.format(x/100) for x in vals], fontsize=size-2)
#ax3.set_xticks(np.linspace(-20, 20, 12))
#ax1.grid(b=True, which='major', axis='both')
# set the x tick labels position
ax3.xaxis.set_ticks_position('bottom')

# Annotate the values
max_value = max([high.max(), low.max()])
min_value = min([high.min(), low.min()])
for i, v in enumerate(high):
    if v > 0:
        ax3.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax3.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)

for i, v in enumerate(low):
    if v > 0:
        ax3.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax3.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)

#ax3.legend(fontsize=size-2, bbox_to_anchor=(0,1.06,1,0.22))
ax3.set_xlabel('Change of CO\N{SUBSCRIPT TWO} emission', fontsize=size, color='k', **font)
ax3.set_ylabel('Parameters', fontsize=size, color='k', **font)
ax3.set_title("(iii) PHEV", color='b', fontsize=size+1, fontweight='bold')

############ HIGHWAY DRIVING  ###############################################################
# GV--------------------------------------
# name of the variables
variables = df4['variables']
# baseline values
base = 0
# low values in percentage
low = df4['low']*100
# high values in percentage
high = df4['high']*100

# position of the variables on y-axis
y_pos = np.arange(len(variables))

# create horizontal bar plot
ax4.barh(y_pos, high, align='center', left=base, height=0.9, color= 'orange', edgecolor='w', alpha =0.9, label='Increase parameter by 15%')
ax4.barh(y_pos, low, align='center', left=base, height=0.9, color= 'blue', edgecolor='w', alpha = 0.9, label='Decrease parameter by 15%')
ax4.set_yticks(y_pos)
ax4.set_yticklabels(variables, fontsize=size, **font)
# show the values of x tick labels in percentage
vals = ax4.get_xticks()
ax4.set_xticklabels(['{:,.0%}'.format(x/100) for x in vals], fontsize=size-2)
#ax4.set_xticks(np.linspace(-20, 20, 9))
#ax1.grid(b=True, which='major', axis='x')
# set the x tick labels position
ax4.xaxis.set_ticks_position('bottom')

# Annotate the values
max_value = max([high.max(), low.max()])
min_value = min([high.min(), low.min()])
for i, v in enumerate(high):
    if v > 0:
        ax4.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax4.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)

for i, v in enumerate(low):
    if v > 0:
        ax4.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax4.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)


ax4.legend(fontsize=size-2, bbox_to_anchor=(0,1.15,1,0.22))
ax4.set_xlabel('Change of CO\N{SUBSCRIPT TWO} emission', fontsize=size, color='k', **font)
ax4.set_ylabel('Parameters', fontsize=size, color='k', **font)
ax4.set_title("(i) GV", color='b', fontsize=size+1, fontweight='bold')
ax4.text(-12, 9, '(b) Highway Driving', fontweight="bold", size=17)

# EV--------------------------------------
# name of the variables
variables = df5['variables']
# baseline values
base = 0
# low values in percentage
low = df5['low']*100
# high values in percentage
high = df5['high']*100

# position of the variables on y-axis
y_pos = np.arange(len(variables))

# create horizontal bar plot
ax5.barh(y_pos, high, align='center', left=base, height=0.9, color= 'orange', edgecolor='w', alpha =0.9, label='Increase parameter by 15%')
ax5.barh(y_pos, low, align='center', left=base, height=0.9, color= 'blue', edgecolor='w', alpha = 0.9, label='Decrease parameter by 15%')
ax5.set_yticks(y_pos)
ax5.set_yticklabels(variables, fontsize=size, **font)
# show the values of x tick labels in percentage
vals = ax5.get_xticks()
ax5.set_xticklabels(['{:,.0%}'.format(x/100) for x in vals], fontsize=size-2)
#ax5.set_xticks(np.linspace(-15, 15, 7))
#ax1.grid(b=True, which='major', axis='both')
# set the x tick labels position
ax5.xaxis.set_ticks_position('bottom')

# Annotate the values
max_value = max([high.max(), low.max()])
min_value = min([high.min(), low.min()])
for i, v in enumerate(high):
    if v > 0:
        ax5.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax5.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)

for i, v in enumerate(low):
    if v > 0:
        ax5.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax5.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)

#ax5.legend(fontsize=size-2, bbox_to_anchor=(0,1.06,1,0.22))
ax5.set_xlabel('Change of CO\N{SUBSCRIPT TWO} emission', fontsize=size, color='k', **font)
ax5.set_ylabel('Parameters', fontsize=size, color='k', **font)
ax5.set_title("(ii) EV", color='b', fontsize=size+1, fontweight='bold')

# PHEV--------------------------------------
# name of the variables
variables = df6['variables']
# baseline values
base = 0
# low values in percentage
low = df6['low']*100
# high values in percentage
high = df6['high']*100

# position of the variables on y-axis
y_pos = np.arange(len(variables))

# create horizontal bar plot
ax6.barh(y_pos, high, align='center', left=base, height=0.9, color= 'orange', edgecolor='w', alpha =.9, label='Increase parameter by 15%')
ax6.barh(y_pos, low, align='center', left=base, height=0.9, color= 'blue', edgecolor='w', alpha = .9, label='Decrease parameter by 15%')
ax6.set_yticks(y_pos)
ax6.set_yticklabels(variables, fontsize=size, **font)
# show the values of x tick labels in percentage
vals = ax6.get_xticks()
ax6.set_xticklabels(['{:,.0%}'.format(x/100) for x in vals], fontsize=size-4)
ax6.set_xticks(np.linspace(-20, 20, 9))
#ax1.grid(b=True, which='major', axis='both')
# set the x tick labels position
ax6.xaxis.set_ticks_position('bottom')

# Annotate the values
max_value = max([high.max(), low.max()])
min_value = min([high.min(), low.min()])
for i, v in enumerate(high):
    if v > 0:
        ax6.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax6.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)

for i, v in enumerate(low):
    if v > 0:
        ax6.text(max_value*0.8, i, '+' + str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)
    else:
        ax6.text(min_value*0.8, i, str(round(v,1)) + '%', color='k', va='center', ha='center', fontsize=size-2)

#ax6.legend(fontsize=size-2, bbox_to_anchor=(0,1.06,1,0.22))
ax6.set_xlabel('Change of CO\N{SUBSCRIPT TWO} emission', fontsize=size, color='k', **font)
ax6.set_ylabel('Parameters', fontsize=size, color='k', **font)
ax6.set_title("(iii) PHEV", color='b', fontsize=size+1, fontweight='bold')

fig.savefig("Sensitivity plot_city and highway driving.v2.png", dpi=300, bbox_inches='tight')