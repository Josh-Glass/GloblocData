import matplotlib.pyplot as plt
import pandas as pd


df_Gens = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Generalization/discr_TestPhase_means.csv')
df_distances = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Generalization/distance_from_origin.csv')


gen_data = df_Gens['mean']
gen_err = df_Gens['stnd_err']

distances = df_distances['distance_O']

plt.scatter(distances[0:6], gen_data[0:6], color = 'k', marker = 's', edgecolors='k')
plt.errorbar(distances[0:6], gen_data[0:6], yerr= gen_err[0:6], fmt= 's', color = 'b',label = 'Beta' ,markersize= 10)

plt.scatter(distances[6:12], gen_data[6:12], color = 'k', marker = 'o')
plt.errorbar(distances[6:12], gen_data[6:12], yerr= gen_err[6:12], fmt= 'o', color = 'r',label = 'Alpha' ,markersize= 10)

plt.scatter(distances[12:17], gen_data[12:17], color = 'k', marker = '*')
plt.errorbar(distances[12:17], gen_data[12:17], yerr= gen_err[12:17], fmt= '*', color = 'y',label = 'Test' ,markersize= 10)

plt.ylim(0,1.01)
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.65, top=0.85)
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xlabel("City Block Distance from Origin")
plt.ylabel("Proportioin Enodrsed as Alpha")
plt.title("Generalization Behavior with Respect to Stimuli\nDistance from Origin (Discriminative)")
plt.savefig('C:/Users/apers/Downloads/GloblocData/Generalization/plot_GenPerf_vs_distance_discr.png')

