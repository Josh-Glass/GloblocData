import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df1 = pd.read_csv('discr_phase1_means.csv')
df2 = pd.read_csv('gener_phase1_means.csv')


x1 = np.array(df1['block_data'])
y1 = np.array(df1['adj_mean'])
x2 = np.array(df2['block_data'])
y2 = np.array(df2['adj_mean'])

plt.plot(x1, y1, label = 'discriminative (n=35)', marker= 'o', markersize= 10)
plt.plot( x2, y2, label = 'generative (n=34)', marker ='s', markersize = 10)
plt.legend(loc="lower right")
plt.xlabel("Training Block")
plt.ylabel("Proportioin Correct")
plt.title("Training Phase 1: Generative vs. Discriminative Learning Curves")
plt.savefig('train1_graph_total.png')
