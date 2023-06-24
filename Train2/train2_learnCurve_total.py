from black import err
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df1 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/Train2/discr_phase2_means.csv")
df2 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/Train2/gener_phase2_means.csv")


x1 = np.array(df1['block_data'])
y1 = np.array(df1['mean'])
err1 = np.array(df1['err'])
x2 = np.array(df2['block_data'])
y2 = np.array(df2['mean'])
err2 = np.array(df2['err'])

plt.errorbar(x1, y1, yerr= err1, label = 'discriminative (n=35)', marker= 'o', markersize= 10)
plt.errorbar( x2, y2, yerr= err2, label = 'generative (n=34)', marker ='s', markersize = 10)
plt.ylim(0.2,1.0)
plt.xlim(right =2.05)
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.65, top=0.85)
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xticks(range(1,3))
#plt.legend(loc="lower right")
plt.xlabel("Training Block")
plt.ylabel("Proportioin Correct")
plt.title("Training Phase 2:\nGenerative vs. Discriminative Learning Curves")
plt.savefig('C:/Users/apers/Downloads/GloblocData/Train2/train2_graph_total.png')
