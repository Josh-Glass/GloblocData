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

df_discr_Betas = df_discr.drop(index = df_discr[df_discr['stim'] == 'materials/images/redA1.png'].index)
df_discr_Betas = df_discr_Betas.drop(index = df_discr_Betas[df_discr_Betas['stim'] == 'materials/images/redA2.png'].index)
df_discr_Betas = df_discr_Betas.drop(index = df_discr_Betas[df_discr_Betas['stim'] == 'materials/images/redA3.png'].index)
df_discr_Betas = df_discr_Betas.drop(index = df_discr_Betas[df_discr_Betas['stim'] == 'materials/images/redA4.png'].index)
df_discr_Betas = df_discr_Betas.drop(index = df_discr_Betas[df_discr_Betas['stim'] == 'materials/images/redA5.png'].index)
df_discr_Betas = df_discr_Betas.drop(index = df_discr_Betas[df_discr_Betas['stim'] == 'materials/images/redA6.png'].index)
df_discr_Betas = df_discr_Betas.drop(index = df_discr_Betas[df_discr_Betas['stim'] == 'materials/images/yGen1.png'].index)
df_discr_Betas = df_discr_Betas.drop(index = df_discr_Betas[df_discr_Betas['stim'] == 'materials/images/yGen2.png'].index)
df_discr_Betas = df_discr_Betas.drop(index = df_discr_Betas[df_discr_Betas['stim'] == 'materials/images/yGen3.png'].index)
df_discr_Betas = df_discr_Betas.drop(index = df_discr_Betas[df_discr_Betas['stim'] == 'materials/images/yGen4.png'].index)
df_discr_Betas = df_discr_Betas.drop(index = df_discr_Betas[df_discr_Betas['stim'] == 'materials/images/yGen5.png'].index)



# get ANOVA table as R like output

# Ordinary Least Squares (OLS) model
model_discr_Betas = ols('means ~ C(stim)', data=df_discr_Betas).fit()
anova_table_discr_Betas = sm.stats.anova_lm(model_discr_Betas, typ=1)
print(anova_table_discr_Betas)


tukey = pairwise_tukeyhsd(endog=df_discr_Betas['means'], groups=df_discr_Betas['stim'], alpha=0.05)
print(tukey)








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

#change the data so it represent proportion of beta responses
newB1D = []
for i in B1D:
    e = 1 -i
    newB1D.append(e)

newB2D = []
for i in B2D:
    e = 1 -i
    newB2D.append(e)

newB3D = []
for i in B3D:
    e = 1 -i
    newB3D.append(e)


newB4D = []
for i in B4D:
    e = 1 -i
    newB4D.append(e)


newB5D = []
for i in B5D:
    e = 1 -i
    newB5D.append(e)

newB6D = []
for i in B6D:
    e = 1 -i
    newB6D.append(e)



B1D_mean = np.mean(newB1D)
B1D_err = sem(newB1D)


B2D_mean = np.mean(newB2D)
B2D_err = sem(newB2D)


B3D_mean = np.mean(newB3D)
B3D_err = sem(newB3D)

B4D_mean = np.mean(newB4D)
B4D_err = sem(newB4D)

B5D_mean = np.mean(newB5D)
B5D_err = sem(newB5D)

B6D_mean = np.mean(newB6D)
B6D_err = sem(newB6D)



conditions = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']
x_pos = np.arange(len(conditions))
accuracy = [B1D_mean, B2D_mean, B3D_mean, B4D_mean, B5D_mean, B6D_mean]
error = [B1D_err, B2D_err, B3D_err, B4D_err, B5D_err, B6D_err]


# Build the plot
fig, ax = plt.subplots()
plt.ylim(0,1)
ax.bar(x_pos, accuracy, yerr=error, align='center', color =['r', 'b', 'g', 'gray', 'y', 'k'], alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Proportion of Subjects who Responded Beta')
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions)
ax.set_title('No-feedback performance on familiar Betas (Discriminative)')
ax.yaxis.grid(True)

# Save the figure
#plt.tight_layout()
plt.savefig('C:/Users/apers/Downloads/GloblocData/Generalization/discr_BetaGen_barplot.png')