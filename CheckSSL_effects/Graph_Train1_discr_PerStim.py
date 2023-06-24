import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df1 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB1_Descriptives.csv")
x_blueB1 = np.array(df1['block_data'])
y_blueB1 = np.array(df1['adj_mean'])
yerr_blueB1 = np.array(df1['stnd_error'], df1['stnd_error'])

df2 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB2_Descriptives.csv")
x_blueB2 = np.array(df2['block_data'])
y_blueB2 = np.array(df2['adj_mean'])
yerr_blueB2 = np.array(df2['stnd_error'], df2['stnd_error'])

df3 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB3_Descriptives.csv")
x_blueB3 = np.array(df3['block_data'])
y_blueB3 = np.array(df3['adj_mean'])
yerr_blueB3 = np.array(df3['stnd_error'], df3['stnd_error'])

df4 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB4_Descriptives.csv")
x_blueB4 = np.array(df4['block_data'])
y_blueB4 = np.array(df4['adj_mean'])
yerr_blueB4 = np.array(df4['stnd_error'], df4['stnd_error'])

df5 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB5_Descriptives.csv")
x_blueB5 = np.array(df5['block_data'])
y_blueB5 = np.array(df5['adj_mean'])
yerr_blueB5 = np.array(df5['stnd_error'], df5['stnd_error'])

df6 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB6_Descriptives.csv")
x_blueB6 = np.array(df6['block_data'])
y_blueB6 = np.array(df6['adj_mean'])
yerr_blueB6 = np.array(df6['stnd_error'], df6['stnd_error'])

df7 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA1_Descriptives.csv")
x_redA1 = np.array(df7['block_data'])
y_redA1 = np.array(df7['adj_mean'])
yerr_redA1 = np.array(df7['stnd_error'], df7['stnd_error'])

df8 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA2_Descriptives.csv")
x_redA2 = np.array(df8['block_data'])
y_redA2 = np.array(df8['adj_mean'])
yerr_redA2 = np.array(df8['stnd_error'], df8['stnd_error'])

df9 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA3_Descriptives.csv")
x_redA3 = np.array(df9['block_data'])
y_redA3 = np.array(df9['adj_mean'])
yerr_redA3 = np.array(df9['stnd_error'], df9['stnd_error'])

df10 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA4_Descriptives.csv")
x_redA4 = np.array(df10['block_data'])
y_redA4 = np.array(df10['adj_mean'])
yerr_redA4 = np.array(df10['stnd_error'], df10['stnd_error'])

df11 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA5_Descriptives.csv")
x_redA5 = np.array(df11['block_data'])
y_redA5 = np.array(df11['adj_mean'])
yerr_redA5 = np.array(df11['stnd_error'], df11['stnd_error'])

df12 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA6_Descriptives.csv")
x_redA6 = np.array(df12['block_data'])
y_redA6 = np.array(df12['adj_mean'])
yerr_redA6 = np.array(df12['stnd_error'], df12['stnd_error'])

plt.errorbar(x_blueB1, y_blueB1, yerr= yerr_blueB1, color = 'b', label = 'B1', marker= 'o', markersize= 8)
plt.errorbar(x_blueB2, y_blueB2, yerr= yerr_blueB2, color= 'b', label = 'B2', marker= 's', markersize= 8)
plt.errorbar(x_blueB3, y_blueB3, yerr= yerr_blueB3, color= 'b', label = 'B3', marker= 'P', markersize= 8)
plt.errorbar(x_blueB4, y_blueB4, yerr= yerr_blueB4, color= 'k', label = 'B4', marker= '*', markersize= 8)
plt.errorbar(x_blueB5, y_blueB5, yerr= yerr_blueB5, color= 'b', label = 'B5', marker= '^', markersize= 8)
plt.errorbar(x_blueB6, y_blueB6, yerr= yerr_blueB6,color = 'b', label = 'B6', marker= 'x', markersize= 8)

plt.errorbar(x_redA1, y_redA1, yerr= yerr_redA1, color= 'r', label = 'A1', marker= 'o', markersize= 8)
plt.errorbar(x_redA2, y_redA2, yerr= yerr_redA2, color = 'r', label = 'A2', marker= 's', markersize= 8)
plt.errorbar(x_redA3, y_redA3, yerr= yerr_redA3,color = 'r', label = 'A3', marker= 'P', markersize= 8)
plt.errorbar(x_redA4, y_redA4, yerr= yerr_redA4,color= 'r', label = 'A4', marker= '*', markersize= 8)
plt.errorbar(x_redA5, y_redA5, yerr= yerr_redA5, color = 'r', label = 'A5', marker= '^', markersize= 8)
plt.errorbar(x_redA6, y_redA6, yerr= yerr_redA6, color = 'k',label = 'A6', marker= 'x', markersize= 8)


plt.ylim(0.2,1.05)
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75, top=0.9)
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xlabel("Training Block")
plt.ylabel("Proportioin Correct")
plt.title("Training Phase 1: Discriminative Learning Per Stimulus")
plt.savefig('C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/train1_Discr_graph_PerStim.png')
