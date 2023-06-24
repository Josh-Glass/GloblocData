import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df1 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Train2/discr_phase2_ALPHA_means.csv')
df2 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Train2/discr_phase2_BETA_means.csv')
df3 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Train2/discr_phase2_GAMMA_means.csv')
df4 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Train2/discr_phase2_DELTA_means.csv')

df5= pd.read_csv('C:/Users/apers/Downloads/GloblocData/Train2/gener_phase2_ALPHA_means.csv')
df6= pd.read_csv('C:/Users/apers/Downloads/GloblocData/Train2/gener_phase2_BETA_means.csv')
df7 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Train2/gener_phase2_GAMMA_means.csv')
df8 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Train2/gener_phase2_DELTA_means.csv')


x_dAlpha = np.array(df1['block_data'])
y_dAlpha = np.array(df1['mean'])

x_dBeta = np.array(df2['block_data'])
y_dBeta = np.array(df2['mean'])

x_dGamma = np.array(df3['block_data'])
y_dGamma = np.array(df3['mean'])

x_dDelta = np.array(df4['block_data'])
y_dDelta = np.array(df4['mean'])


x_gAlpha = np.array(df5['block_data'])
y_gAlpha = np.array(df5['mean'])

x_gBeta = np.array(df6['block_data'])
y_gBeta = np.array(df6['mean'])

x_gGamma = np.array(df7['block_data'])
y_gGamma = np.array(df7['mean'])

x_gDelta = np.array(df8['block_data'])
y_gDelta = np.array(df8['mean'])


plt.plot(x_gAlpha, y_gAlpha, label = 'generative alpha', marker= 'o', markersize= 10)
plt.plot( x_gBeta, y_gBeta, label = 'generative beta', marker = 's', markersize= 10)
plt.plot( x_gGamma, y_gGamma, label = 'generative gamma', marker ='^', markersize = 10)
plt.plot( x_gDelta, y_gDelta, label = 'generative delta', marker ='P', markersize = 10)

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.65, top=0.8)
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xlabel("Training Block")
plt.ylabel("Proportioin Correct")
plt.title("Training Phase 2: Generative Learning Per Category")
plt.savefig('C:/Users/apers/Downloads/GloblocData/Train2/train2_Gener_graph_PerCat.png')
