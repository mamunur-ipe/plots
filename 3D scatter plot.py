"""
@Author: Mamunur Rahman
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from mpl_toolkits import mplot3d


#old data
df=pd.read_csv('Breast cancer data.csv')
X=df.iloc[:,0:9]
y=df.iloc[:,9]

data_1_old = df[df["Classification"] == 1] #data with class '1'
data_0_old = df[df["Classification"] == 0] #data with class '0'

#new data
X_new=pd.read_csv('Breast cancer_weighted data.csv')
df_new = X_new
df_new["Classification"] = df["Classification"]

data_1 = df_new[df["Classification"] == 1] #data with class '1'
data_0 = df_new[df["Classification"] == 0] #data with class '0'

#figure
fig = plt.figure(constrained_layout=True, figsize=(12,4.5))

gs = GridSpec(1, 2, figure=fig)
ax1 = fig.add_subplot(gs[0, 0], projection='3d')
ax2 = fig.add_subplot(gs[0, 1], projection='3d')

size = 11.5  #label font size

## scatter plot before oversampling
scatter1=ax1.scatter(data_1_old.iloc[:, [2]], data_1_old.iloc[:, [0]], data_1_old.iloc[:, [8]], c='cyan', marker='o', s=30, edgecolors='k', depthshade= 0)
scatter2=ax1.scatter(data_0_old.iloc[:, [2]], data_0_old.iloc[:, [0]], data_0_old.iloc[:, [8]], c='coral', marker='o', s=30, edgecolors='k', depthshade= 0)

ax1.set_xlabel('Glucose', fontsize=size)
ax1.set_ylabel('Age', fontsize=size, rotation=30)
ax1.set_zlabel('MCP-1', fontsize=size)
# ax1.set_xticks(range(20,91,10))

ax1.set_title('(a) Before preprocessing\n\n', fontsize=14, fontweight='bold')

# set legend
legend=ax1.legend([scatter1, scatter2], ['Cancer patient', 'Healthy subject'], numpoints = 1, loc='upper right', fontsize=size)
legend.get_frame().set_edgecolor('k')



## scatter plot after oversampling
scatter1=ax2.scatter(data_1.iloc[:, [2]], data_1.iloc[:, [0]], data_1.iloc[:, [8]], c='cyan', marker='o', s=30, edgecolors='k', depthshade= 0)
scatter2=ax2.scatter(data_0.iloc[:, [2]], data_0.iloc[:, [0]], data_0.iloc[:, [8]], c='coral', marker='o', s=30, edgecolors='k', depthshade= 0)

ax2.set_xlabel('Glucose', fontsize=size)
ax2.set_ylabel('Age', fontsize=size, rotation=30)
ax2.set_zlabel('MCP-1', fontsize=size)
# ax2.set_yticks(range(0,20,2))
ax2.set_title('(b) After scaling and feature weighting\n\n', fontsize=14, fontweight='bold')

# set legend
legend=ax2.legend([scatter1, scatter2], ['Cancer patient', 'Healthy subject'], numpoints = 1, loc='upper right', fontsize=size)
legend.get_frame().set_edgecolor('k')

#save figure
fig.savefig("3D plot_breast cancer.png", dpi=300, bbox_inches='tight')

