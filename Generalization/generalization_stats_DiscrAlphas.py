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

df_discr_Alphas = df_discr.drop(index = df_discr[df_discr['stim'] == 'materials/images/blueB1.png'].index)
df_discr_Alphas = df_discr_Alphas.drop(index = df_discr_Alphas[df_discr_Alphas['stim'] == 'materials/images/blueB2.png'].index)
df_discr_Alphas = df_discr_Alphas.drop(index = df_discr_Alphas[df_discr_Alphas['stim'] == 'materials/images/blueB3.png'].index)
df_discr_Alphas = df_discr_Alphas.drop(index = df_discr_Alphas[df_discr_Alphas['stim'] == 'materials/images/blueB4.png'].index)
df_discr_Alphas = df_discr_Alphas.drop(index = df_discr_Alphas[df_discr_Alphas['stim'] == 'materials/images/blueB5.png'].index)
df_discr_Alphas = df_discr_Alphas.drop(index = df_discr_Alphas[df_discr_Alphas['stim'] == 'materials/images/blueB6.png'].index)
df_discr_Alphas = df_discr_Alphas.drop(index = df_discr_Alphas[df_discr_Alphas['stim'] == 'materials/images/yGen1.png'].index)
df_discr_Alphas = df_discr_Alphas.drop(index = df_discr_Alphas[df_discr_Alphas['stim'] == 'materials/images/yGen2.png'].index)
df_discr_Alphas = df_discr_Alphas.drop(index = df_discr_Alphas[df_discr_Alphas['stim'] == 'materials/images/yGen3.png'].index)
df_discr_Alphas = df_discr_Alphas.drop(index = df_discr_Alphas[df_discr_Alphas['stim'] == 'materials/images/yGen4.png'].index)
df_discr_Alphas = df_discr_Alphas.drop(index = df_discr_Alphas[df_discr_Alphas['stim'] == 'materials/images/yGen5.png'].index)



# get ANOVA table as R like output

# Ordinary Least Squares (OLS) model
model_discr_Alphas = ols('means ~ C(stim)', data=df_discr_Alphas).fit()
anova_table_discr_Alphas = sm.stats.anova_lm(model_discr_Alphas, typ=1)
print(anova_table_discr_Alphas)


tukey = pairwise_tukeyhsd(endog=df_discr_Alphas['means'], groups=df_discr_Alphas['stim'], alpha=0.05)
print(tukey)


exit()

#get all the data for discriminative codnition first
#get lists of subject response values for each stimulus
A1D = []
A2D = []
A3D = []
A4D =[]
A5D = []
A6D = []


B1D = []
B2D =[]
B3D = []
B4D = []
B5D = []
B6D = []


for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/blueB1.png':
        B1D.append(row.means)

for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/blueB2.png':
        B2D.append(row.means)

for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/blueB3.png':
        B3D.append(row.means)

for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/blueB4.png':
        B4D.append(row.means)

for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/blueB5.png':
        B5D.append(row.means)

for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/blueB6.png':
        B6D.append(row.means)







for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/redA1.png':
        A1D.append(row.means)


for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/redA2.png':
        A2D.append(row.means)


for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/redA3.png':
        A3D.append(row.means)


for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/redA4.png':
        A4D.append(row.means)


for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/redA5.png':
        A5D.append(row.means)


for i, row in df_discr.iterrows():
    if row.stim == 'materials/images/redA6.png':
        A6D.append(row.means)


#another way to do an anova
#fvalue, pvalue = stats.f_oneway(B1D, B2D, B3D, B4D, B5D, B6D)
#print(fvalue, pvalue)


#Make a graph


A1D_mean = np.mean(A1D)
A1D_err = sem(A1D)


A2D_mean = np.mean(A2D)
A2D_err = sem(A2D)


A3D_mean = np.mean(A3D)
A3D_err = sem(A3D)

A4D_mean = np.mean(A4D)
A4D_err = sem(A4D)

A5D_mean = np.mean(A5D)
A5D_err = sem(A5D)

A6D_mean = np.mean(A6D)
A6D_err = sem(A6D)



conditions = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
x_pos = np.arange(len(conditions))
accuracy = [A1D_mean, A2D_mean, A3D_mean, A4D_mean, A5D_mean, A6D_mean]
error = [A1D_err, A2D_err, A3D_err, A4D_err, A5D_err, A6D_err]


# Build the plot
fig, ax = plt.subplots()
plt.ylim(0,1)
ax.bar(x_pos, accuracy, yerr=error, align='center', color =['r', 'b', 'g', 'gray', 'y', 'k'], alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Proportion of Subjects who Responded Alpha')
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions)
ax.set_title('No-feedback performance on familiar Alphas (Discriminative)')
ax.yaxis.grid(True)

# Save the figure
#plt.tight_layout()
plt.savefig('C:/Users/apers/Downloads/GloblocData/Generalization/discr_AlphaGen_barplot.png')