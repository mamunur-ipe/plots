"""
@Author: Mamunur Rahman
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

df = pd.read_excel(io = 'driving profile.xlsx', sheet_name= 'Sheet1', header=0)
df.head()

fig = plt.figure(constrained_layout=True, figsize=(8,5))

gs = GridSpec(3, 1, figure=fig)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[2, 0])

font_size=12 #font size
line_weight=1.25
# Peak hour traffic------------------------------------------------------------------------
color = 'orangered'
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Speed (m/s)', color=color)
ax1.plot(df['time_peak'], df['v_peak'], color='tab:orange', linewidth=line_weight)
ax1.tick_params(axis='y', labelcolor=color)
#ax1.set_xlim(0, 2300)
#ax1.set_ylim(0, 20)
ax1.set_yticks( np.arange(0,21,5))
ax1.set_title('(a) Peak hour traffic\n', color='k', fontsize=font_size, fontweight='bold')
ax1.text(600,22, ' (Total CO\N{SUBSCRIPT TWO} emission = 4405 grams)', color='k', size=11)

ax12 = ax1.twinx()
color = 'b'
ax12.set_ylabel('VSP (KW/ton)', color=color)  # we already handled the x-label with ax1
ax12.plot(df['time_peak'], df['vsp_peak'], color='cornflowerblue', linewidth=line_weight)
ax12.tick_params(axis='y', labelcolor=color)
ax12.set_ylim(-50, 50)

ax13 = ax1.twinx()
color = 'tab:green'
ax13.set_ylabel('CO2 rate (g/s)', color=color)  # we already handled the x-label with ax1
ax13.plot(df['time_peak'], df['co2_peak'], color='springgreen', linewidth=line_weight)
ax13.tick_params(axis='y', labelcolor=color)
# right, left, top, bottom
ax13.spines['right'].set_position(('outward', 50)) 
#ax13.set_ylim(0, 13)
ax13.set_yticks( np.arange(0,13,3))


# Moderate traffic------------------------------------------------------------------------
color = 'orangered'
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Speed (m/s)', color=color)
ax2.plot(df['time_moderate'], df['v_moderate'], color='tab:orange', linewidth=line_weight)
ax2.tick_params(axis='y', labelcolor=color)
#ax2.set_xlim(0, 2300)
#ax2.set_ylim(0, 20)
ax2.set_yticks( np.arange(0,21,5))
ax2.set_title('(b) Moderate traffic\n', color='k', fontsize=font_size, fontweight='bold')
ax2.text(450,22, ' (Total CO\N{SUBSCRIPT TWO} emission = 3673 grams)', color='k', size=11)

ax12 = ax2.twinx()
color = 'b'
ax12.set_ylabel('VSP (KW/ton)', color=color)  # we already handled the x-label with ax1
ax12.plot(df['time_moderate'], df['vsp_moderate'], color='cornflowerblue', linewidth=line_weight)
ax12.tick_params(axis='y', labelcolor=color)
ax12.set_ylim(-50, 50)

ax13 = ax2.twinx()
color = 'tab:green'
ax13.set_ylabel('CO2 rate (g/s)', color=color)  # we already handled the x-label with ax1
ax13.plot(df['time_moderate'], df['co2_moderate'], color='springgreen', linewidth=line_weight)
ax13.tick_params(axis='y', labelcolor=color)
# right, left, top, bottom
ax13.spines['right'].set_position(('outward', 50)) 
#ax13.set_ylim(0, 13)
ax13.set_yticks( np.arange(0,13,3))

# Low traffic------------------------------------------------------------------------
color = 'orangered'
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Speed (m/s)', color=color)
ax3.plot(df['time_low'], df['v_low'], color='tab:orange', linewidth=line_weight)
ax3.tick_params(axis='y', labelcolor=color)
#ax3.set_xlim(0, 2300)
#ax3.set_ylim(0, 20)
ax3.set_yticks( np.arange(0,21,5))
ax3.set_title('(c) Low traffic\n', color='k', fontsize=font_size, fontweight='bold')
ax3.text(450,22, ' (Total CO\N{SUBSCRIPT TWO} emission = 3458 grams)', color='k', size=11)

ax12 = ax3.twinx()
color = 'blue'
ax12.set_ylabel('VSP (KW/ton)', color=color)  # we already handled the x-label with ax1
ax12.plot(df['time_low'], df['vsp_low'], color='cornflowerblue', linewidth=line_weight)
ax12.tick_params(axis='y', labelcolor=color)
ax12.set_ylim(-50, 50)

ax13 = ax3.twinx()
color = 'tab:green'
ax13.set_ylabel('CO2 rate (g/s)', color=color)  # we already handled the x-label with ax1
ax13.plot(df['time_low'], df['co2_low'], color='springgreen', linewidth=line_weight)
ax13.tick_params(axis='y', labelcolor=color)
# right, left, top, bottom
ax13.spines['right'].set_position(('outward', 50)) 
#ax13.set_ylim(0, 13)
ax13.set_yticks( np.arange(0,13,3))


#save the figure
fig.savefig("Travel profile_city driving.png", dpi=300, bbox_inches='tight')
