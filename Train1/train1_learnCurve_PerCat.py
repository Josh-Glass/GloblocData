import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df1 = pd.read_csv('discr_phase1_ALPHA_means.csv')
df2 = pd.read_csv('discr_phase1_BETA_means.csv')

df3 = pd.read_csv('gener_phase1_ALPHA_means.csv')
df4 = pd.read_csv('gener_phase1_BETA_means.csv')


x_dAlpha = np.array(df1['block_data'])
y_dAlpha = np.array(df1['adj_mean'])

x_dBeta = np.array(df2['block_data'])
y_dBeta = np.array(df2['adj_mean'])

x_gAlpha = np.array(df3['block_data'])
y_gAlpha = np.array(df3['adj_mean'])

x_gBeta = np.array(df4['block_data'])
y_gBeta = np.array(df4['adj_mean'])

plt.plot(x_dAlpha, y_dAlpha, label = 'discriminative alpha', marker= 'o', markersize= 10)
plt.plot( x_dBeta, y_dBeta, label = 'discriminative beta', marker ='s', markersize = 10)

plt.plot(x_gAlpha, y_gAlpha, label = 'generative alpha', marker= '^', markersize= 10)
plt.plot( x_gBeta, y_gBeta, label = 'generative beta', marker = '*', markersize= 15)

plt.legend(loc="lower right")
plt.xlabel("Training Block")
plt.ylabel("Proportioin Correct")
plt.title("Training Phase 1: Learning Curves Per Category")
plt.savefig('train1_graph_PerCat.png')
