"""
@Author: Mamunur Rahman
"""

#show correlation in heatmap using Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

df=pd.read_csv('Breast cancer data.csv')
X=df.iloc[:,0:9]

fig = plt.figure(figsize=(7,4))
gs = GridSpec(1, 1, figure=fig)

#create colormap
ax = fig.add_subplot(gs[0, 0])
sns.heatmap(ax=ax, data=X.corr(), annot=True, fmt='.2f', linewidths=0.5, cmap="YlGnBu" )

#save figure
fig.savefig("Correlation heatmap_breast cancer.png", dpi=300, bbox_inches='tight')