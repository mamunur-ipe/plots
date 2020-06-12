import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

## Confidence Interval plot assuming not equal variance
fig = plt.figure(figsize=(7,4))

gs = GridSpec(1, 1, figure=fig)
ax = fig.add_subplot(gs[0, 0])

size=11 #font size
# Female
ax.plot([45.8, 65.0, 84.2], [1,1,1],'bo-',linewidth=4, markeredgecolor='k',
         markersize=6, markeredgewidth=2, markerfacecolor='w')

ax.plot([24.0,35.6,47.22], [3,3,3],'bo-',linewidth=4, markeredgecolor='k',
         markersize=6, markeredgewidth=2, markerfacecolor='w')

ax.plot([40.2,50.7,61.2], [5,5,5],'bo-',linewidth=4, markeredgecolor='k',
         markersize=6, markeredgewidth=2, markerfacecolor='w')

ax.plot([31.7,46.4,61.1], [7,7,7],'bo-',linewidth=4, markeredgecolor='k',
         markersize=6, markeredgewidth=2, markerfacecolor='w')


ax.plot([38.0,50.4,62.8], [9,9,9],'bo-',linewidth=4, markeredgecolor='k',
         markersize=6, markeredgewidth=2, markerfacecolor='w')

# Male
ax.plot([79.3,97.6,115.9], [1.5,1.5,1.5], color='lime', marker='o',
         linestyle='-', linewidth=4, markeredgecolor='k', markersize=6, markeredgewidth=2, markerfacecolor='w')

ax.plot([24.4,41.8,59.2], [3.5,3.5,3.5], color='lime', marker='o',
         linestyle='-', linewidth=4, markeredgecolor='k', markersize=6, markeredgewidth=2, markerfacecolor='w')


ax.plot([64.6,71.8,79.0], [5.5,5.5,5.5], color='lime', marker='o',
         linestyle='-', linewidth=4, markeredgecolor='k', markersize=6, markeredgewidth=2, markerfacecolor='w')

ax.plot([60.6,70.6,80.6], [7.5,7.5,7.5], color='lime', marker='o',
         linestyle='-', linewidth=4, markeredgecolor='k', markersize=6, markeredgewidth=2, markerfacecolor='w')

ax.plot([55.2,63.6,72.0], [9.5,9.5,9.5], color='lime', marker='o',
         linestyle='-', linewidth=4, markeredgecolor='k', markersize=6, markeredgewidth=2, markerfacecolor='w')

#Set x-label
ax.set_xlabel('Force (lbs)', fontsize=12, color='b')
#Set y-label
ax.set_ylabel('Wrist positions', fontsize=12, color='b')

# Set y-tick labels
ax.set_yticks( [0.5,1,1.5,3,3.5,5,5.5,7,7.5,9,9.5,10] )
ax.set_yticklabels(['','Neutral-female','Neutral-male','Flexed-female','Flexed-male','Extended-female',
                     'Extended-male','Ulnar-female','Ulnar-male','Radial-female','Radial-male',''], fontsize=11)
ax.set_title('CI of forces for different wrist positions\n', fontsize=12, fontweight='bold', color='r')
#ax.grid()
plt.show()
fig.savefig("Confidence Interval plot.png", dpi=300, bbox_inches='tight')
