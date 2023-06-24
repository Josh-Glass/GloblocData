import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt

df_discr = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Generalization/discr_TestPhase_means_PerSub.csv')

df_gener = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Generalization/gener_TestPhase_means_PerSub.csv')


#get separate dataframes for each category of stim

df_gener_Alphas = df_gener.drop(index = df_gener[df_gener['stim'] == 'materials/images/blueB1.png'].index)
df_gener_Alphas = df_gener_Alphas.drop(index = df_gener_Alphas[df_gener_Alphas['stim'] == 'materials/images/blueB2.png'].index)
df_gener_Alphas = df_gener_Alphas.drop(index = df_gener_Alphas[df_gener_Alphas['stim'] == 'materials/images/blueB3.png'].index)
df_gener_Alphas = df_gener_Alphas.drop(index = df_gener_Alphas[df_gener_Alphas['stim'] == 'materials/images/blueB4.png'].index)
df_gener_Alphas = df_gener_Alphas.drop(index = df_gener_Alphas[df_gener_Alphas['stim'] == 'materials/images/blueB5.png'].index)
df_gener_Alphas = df_gener_Alphas.drop(index = df_gener_Alphas[df_gener_Alphas['stim'] == 'materials/images/blueB6.png'].index)
df_gener_Alphas = df_gener_Alphas.drop(index = df_gener_Alphas[df_gener_Alphas['stim'] == 'materials/images/yGen1.png'].index)
df_gener_Alphas = df_gener_Alphas.drop(index = df_gener_Alphas[df_gener_Alphas['stim'] == 'materials/images/yGen2.png'].index)
df_gener_Alphas = df_gener_Alphas.drop(index = df_gener_Alphas[df_gener_Alphas['stim'] == 'materials/images/yGen3.png'].index)
df_gener_Alphas = df_gener_Alphas.drop(index = df_gener_Alphas[df_gener_Alphas['stim'] == 'materials/images/yGen4.png'].index)
df_gener_Alphas = df_gener_Alphas.drop(index = df_gener_Alphas[df_gener_Alphas['stim'] == 'materials/images/yGen5.png'].index)



# get ANOVA table as R like output

# Ordinary Least Squares (OLS) model
model_gener_Alphas = ols('means ~ C(stim)', data=df_gener_Alphas).fit()
anova_table_gener_Alphas = sm.stats.anova_lm(model_gener_Alphas, typ=1)
print(anova_table_gener_Alphas)


tukey = pairwise_tukeyhsd(endog=df_gener_Alphas['means'], groups=df_gener_Alphas['stim'], alpha=0.05)
print(tukey)





#get lists of subject response values for each stimulus
A1G = []
A2G = []
A3G = []
A4G =[]
A5G = []
A6G = []


B1D = []
B2D =[]
B3D = []
B4D = []
B5D = []
B6D = []


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB1.png':
        B1D.append(row.means)

for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB2.png':
        B2D.append(row.means)

for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB3.png':
        B3D.append(row.means)

for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB4.png':
        B4D.append(row.means)

for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB5.png':
        B5D.append(row.means)

for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB6.png':
        B6D.append(row.means)







for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA1.png':
        A1G.append(row.means)


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA2.png':
        A2G.append(row.means)


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA3.png':
        A3G.append(row.means)


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA4.png':
        A4G.append(row.means)


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA5.png':
        A5G.append(row.means)


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA6.png':
        A6G.append(row.means)


#another way to do an anova
#fvalue, pvalue = stats.f_oneway(B1D, B2D, B3D, B4D, B5D, B6D)
#print(fvalue, pvalue)


#Make a graph


A1G_mean = np.mean(A1G)
A1G_err = sem(A1G)


A2G_mean = np.mean(A2G)
A2G_err = sem(A2G)


A3G_mean = np.mean(A3G)
A3G_err = sem(A3G)

A4G_mean = np.mean(A4G)
A4G_err = sem(A4G)

A5G_mean = np.mean(A5G)
A5G_err = sem(A5G)

A6G_mean = np.mean(A6G)
A6G_err = sem(A6G)



conditions = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
x_pos = np.arange(len(conditions))
accuracy = [A1G_mean, A2G_mean, A3G_mean, A4G_mean, A5G_mean, A6G_mean]
error = [A1G_err, A2G_err, A3G_err, A4G_err, A5G_err, A6G_err]


# Build the plot
fig, ax = plt.subplots()
plt.ylim(0,1)
ax.bar(x_pos, accuracy, yerr=error, align='center', color =['r', 'b', 'g', 'gray', 'y', 'k'], alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Proportion of Subjects who Responded Alpha')
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions)
ax.set_title('No-feedback performance on familiar Alphas (Generative)')
ax.yaxis.grid(True)

# Save the figure
#plt.tight_layout()
plt.savefig('C:/Users/apers/Downloads/GloblocData/Generalization/gener_AlphaGen_barplot.png')