"""
@Author: Mamunur Rahman
"""

## Violin plot of the features
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

#read data
df=pd.read_csv('Breast cancer data.csv')
X=df.iloc[:,0:9]
y=df.iloc[:,9]

fig = plt.figure(constrained_layout=True, figsize=(10,5))

gs = GridSpec(3, 3, figure=fig)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])

ax4 = fig.add_subplot(gs[1, 0])
ax5 = fig.add_subplot(gs[1, 1])
ax6 = fig.add_subplot(gs[1, 2])

ax7 = fig.add_subplot(gs[2, 0])
ax8 = fig.add_subplot(gs[2, 1])
ax9 = fig.add_subplot(gs[2, 2])

size=11 #font size

ax1.violinplot(df['Age'][y==0], [1], points=20, widths=0.8, vert=False, showmeans=True)
ax1.violinplot(df['Age'][y==1],[2], points=20, widths=0.8, vert=False, showmeans=True)
ax1.set_yticks([1, 2])
ax1.set_yticklabels(['Healthy\n' + 'subject', 'Cancer\n' + 'patient'])
ax1.set_xticks(range(20,91,10))
ax1.set_xlabel('Age (years)', fontsize=size, color='b')

ax2.violinplot(df['BMI'][y==0], [1], points=20, widths=0.8, vert=False, showmeans=True)
ax2.violinplot(df['BMI'][y==1],[2], points=20, widths=0.8, vert=False, showmeans=True)
ax2.set_yticks([1, 2])
ax2.set_yticklabels(['Healthy\n' + 'subject', 'Cancer\n' + 'patient'])
ax2.set_xticks(range(15,41,5))
ax2.set_xlabel('BMI (kg/m2) ', fontsize=size, color='b')

ax3.violinplot(df['Glucose'][y==0], [1], points=20, widths=0.8, vert=False, showmeans=True)
ax3.violinplot(df['Glucose'][y==1],[2], points=20, widths=0.8, vert=False, showmeans=True)
ax3.set_yticks([1, 2])
ax3.set_yticklabels(['Healthy\n' + 'subject', 'Cancer\n' + 'patient'])
ax3.set_xticks(range(60,221,30))
ax3.set_xlabel('Glucose (mg/dL)', fontsize=size, color='b')

ax4.violinplot(df['Insulin'][y==0], [1], points=20, widths=0.8, vert=False, showmeans=True)
ax4.violinplot(df['Insulin'][y==1],[2], points=20, widths=0.8, vert=False, showmeans=True)
ax4.set_yticks([1, 2])
ax4.set_yticklabels(['Healthy\n' + 'subject', 'Cancer\n' + 'patient'])
ax4.set_xticks(range(0,61,10))
ax4.set_xlabel('Insulin (μU/mL)', fontsize=size, color='b')

ax5.violinplot(df['HOMA'][y==0], [1], points=20, widths=0.8, vert=False, showmeans=True)
ax5.violinplot(df['HOMA'][y==1],[2], points=20, widths=0.8, vert=False, showmeans=True)
ax5.set_yticks([1, 2])
ax5.set_yticklabels(['Healthy\n' + 'subject', 'Cancer\n' + 'patient'])
ax5.set_xticks(range(0,26,5))
ax5.set_xlabel('HOMA', fontsize=size, color='b')

ax6.violinplot(df['Leptin'][y==0], [1], points=20, widths=0.8, vert=False, showmeans=True)
ax6.violinplot(df['Leptin'][y==1],[2], points=20, widths=0.8, vert=False, showmeans=True)
ax6.set_yticks([1, 2])
ax6.set_yticklabels(['Healthy\n' + 'subject', 'Cancer\n' + 'patient'])
ax6.set_xticks(range(0,91,10))
ax6.set_xlabel('Leptin (ng/mL)', fontsize=size, color='b')

ax7.violinplot(df['Adiponectin'][y==0], [1], points=20, widths=0.8, vert=False, showmeans=True)
ax7.violinplot(df['Adiponectin'][y==1],[2], points=20, widths=0.8, vert=False, showmeans=True)
ax7.set_yticks([1, 2])
ax7.set_yticklabels(['Healthy\n' + 'subject', 'Cancer\n' + 'patient'])
ax7.set_xticks(range(0,41,10))
ax7.set_xlabel('Adiponectin (μg/mL)', fontsize=size, color='b')

ax8.violinplot(df['Resistin'][y==0], [1], points=20, widths=0.8, vert=False, showmeans=True)
ax8.violinplot(df['Resistin'][y==1],[2], points=20, widths=0.8, vert=False, showmeans=True)
ax8.set_yticks([1, 2])
ax8.set_yticklabels(['Healthy\n' + 'subject', 'Cancer\n' + 'patient'])
ax8.set_xticks(range(0,91,10))
ax8.set_xlabel('Resistin (ng/mL)', fontsize=size, color='b')

ax9.violinplot(df['MCP-1'][y==0], [1], points=20, widths=0.8, vert=False, showmeans=True)
ax9.violinplot(df['MCP-1'][y==1],[2], points=20, widths=0.8, vert=False, showmeans=True)
ax9.set_yticks([1, 2])
ax9.set_yticklabels(['Healthy\n' + 'subject', 'Cancer\n' + 'patient'])
ax9.set_xticks(range(0,2001,500))
ax9.set_xlabel('MCP-1 (pg/dL)', fontsize=size, color='b')

plt.show()
#save figure
fig.savefig("Violin plot_breast cancer.png", dpi=300, bbox_inches='tight')