"""
@Author: Mamunur Rahman
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec

df=pd.read_csv('Breast cancer_optimum number features.csv', delimiter = ',')
df.head()

labels = ['BLR', 'LDA', 'QDA', 'CART', 'SVM', 'RF', 'Bagging', 'AdaBoost']

BLR = df['BLR']
LDA = df['LDA']
QDA = df['QDA']
CART = df['CART']
SVM = df['SVM']
RF = df['RF']
Bagging = df['Bagging']
AdaBoost = df['AdaBoost']

x = np.arange(len(labels))  # the label locations
width = 0.1  # the width of the bars

#figure
fig = plt.figure(constrained_layout=True, figsize=(10,4))

gs = GridSpec(1, 1, figure=fig)
ax = fig.add_subplot(gs[0, 0])

b1 = ax.bar(x - 4*width+width/2, BLR-74, width, label='BLR', bottom=74, edgecolor='w', linewidth=1)
b2 = ax.bar(x - 3*width+width/2, LDA-74, width, label='LDA', bottom=74, edgecolor='w', linewidth=1)
b3 = ax.bar(x - 2*width+width/2, QDA-74, width, label='QDA', bottom=74, edgecolor='w', linewidth=1)
b4 = ax.bar(x - 1*width+width/2, CART-74, width, label='CART', bottom=74, edgecolor='w', linewidth=1)
b5 = ax.bar(x + 0*width+width/2, SVM-74, width, label='SVM', bottom=74, edgecolor='w', linewidth=1)
b6 = ax.bar(x + 1*width+width/2, RF-74, width, label='RF', bottom=74, edgecolor='w', linewidth=1)
b7 = ax.bar(x + 2*width+width/2, Bagging-74, width, label='Bagging', bottom=74, edgecolor='w', linewidth=1)
b8 = ax.bar(x + 3*width+width/2, AdaBoost-74, width, label='AdaBoost', bottom=74, edgecolor='w', linewidth=1)

ax.set_yticks(np.arange(74, 99, 2))
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Classification accuracy (%)')
ax.set_xlabel('Number of top features')
ax.set_xticks(x)
ax.set_xticklabels(df['Dimension'])
ax.legend()

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/1.5, 1.05*height+74,
                f'{"{:.1f}".format(height+74)}%', ha='center', va='bottom', rotation=90, fontsize=9, color='b')


autolabel(b1)
autolabel(b2)
autolabel(b3)
autolabel(b4)
autolabel(b5)
autolabel(b6)
autolabel(b7)
autolabel(b8)

# ax.grid(which='major', axis='y', ls = '-', lw = .3)

plt.show()
fig.savefig("Grouped bar chart_breast cancer.png", dpi=300, bbox_inches='tight')
