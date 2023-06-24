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

df_gener_Betas = df_gener.drop(index = df_gener[df_gener['stim'] == 'materials/images/redA1.png'].index)
df_gener_Betas = df_gener_Betas.drop(index = df_gener_Betas[df_gener_Betas['stim'] == 'materials/images/redA2.png'].index)
df_gener_Betas = df_gener_Betas.drop(index = df_gener_Betas[df_gener_Betas['stim'] == 'materials/images/redA3.png'].index)
df_gener_Betas = df_gener_Betas.drop(index = df_gener_Betas[df_gener_Betas['stim'] == 'materials/images/redA4.png'].index)
df_gener_Betas = df_gener_Betas.drop(index = df_gener_Betas[df_gener_Betas['stim'] == 'materials/images/redA5.png'].index)
df_gener_Betas = df_gener_Betas.drop(index = df_gener_Betas[df_gener_Betas['stim'] == 'materials/images/redA6.png'].index)
df_gener_Betas = df_gener_Betas.drop(index = df_gener_Betas[df_gener_Betas['stim'] == 'materials/images/yGen1.png'].index)
df_gener_Betas = df_gener_Betas.drop(index = df_gener_Betas[df_gener_Betas['stim'] == 'materials/images/yGen2.png'].index)
df_gener_Betas = df_gener_Betas.drop(index = df_gener_Betas[df_gener_Betas['stim'] == 'materials/images/yGen3.png'].index)
df_gener_Betas = df_gener_Betas.drop(index = df_gener_Betas[df_gener_Betas['stim'] == 'materials/images/yGen4.png'].index)
df_gener_Betas = df_gener_Betas.drop(index = df_gener_Betas[df_gener_Betas['stim'] == 'materials/images/yGen5.png'].index)



# get ANOVA table as R like output

# Ordinary Least Squares (OLS) model
model_gener_Betas = ols('means ~ C(stim)', data=df_gener_Betas).fit()
anova_table_gener_Betas = sm.stats.anova_lm(model_gener_Betas, typ=1)
print(anova_table_gener_Betas)


tukey = pairwise_tukeyhsd(endog=df_gener_Betas['means'], groups=df_gener_Betas['stim'], alpha=0.05)
print(tukey)







#get all the data for discriminative codnition first
#get lists of subject response values for each stimulus
A1D = []
A2D = []
A3D = []
A4D =[]
A5D = []
A6D = []


B1G = []
B2G =[]
B3G = []
B4G = []
B5G = []
B6G = []


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB1.png':
        B1G.append(row.means)

for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB2.png':
        B2G.append(row.means)

for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB3.png':
        B3G.append(row.means)

for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB4.png':
        B4G.append(row.means)

for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB5.png':
        B5G.append(row.means)

for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/blueB6.png':
        B6G.append(row.means)







for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA1.png':
        A1D.append(row.means)


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA2.png':
        A2D.append(row.means)


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA3.png':
        A3D.append(row.means)


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA4.png':
        A4D.append(row.means)


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA5.png':
        A5D.append(row.means)


for i, row in df_gener.iterrows():
    if row.stim == 'materials/images/redA6.png':
        A6D.append(row.means)


#another way to do an anova
#fvalue, pvalue = stats.f_oneway(B1G, B2G, B3G, B4G, B5G, B6G)
#print(fvalue, pvalue)


#Make a graph

#change the data so it represent proportion of beta responses
newB1G = []
for i in B1G:
    e = 1 -i
    newB1G.append(e)

newB2G = []
for i in B2G:
    e = 1 -i
    newB2G.append(e)

newB3G = []
for i in B3G:
    e = 1 -i
    newB3G.append(e)


newB4G = []
for i in B4G:
    e = 1 -i
    newB4G.append(e)


newB5G = []
for i in B5G:
    e = 1 -i
    newB5G.append(e)

newB6G = []
for i in B6G:
    e = 1 -i
    newB6G.append(e)



B1G_mean = np.mean(newB1G)
B1G_err = sem(newB1G)


B2G_mean = np.mean(newB2G)
B2G_err = sem(newB2G)


B3G_mean = np.mean(newB3G)
B3G_err = sem(newB3G)

B4G_mean = np.mean(newB4G)
B4G_err = sem(newB4G)

B5G_mean = np.mean(newB5G)
B5G_err = sem(newB5G)

B6G_mean = np.mean(newB6G)
B6G_err = sem(newB6G)



conditions = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']
x_pos = np.arange(len(conditions))
accuracy = [B1G_mean, B2G_mean, B3G_mean, B4G_mean, B5G_mean, B6G_mean]
error = [B1G_err, B2G_err, B3G_err, B4G_err, B5G_err, B6G_err]


# Build the plot
fig, ax = plt.subplots()
plt.ylim(0,1)
ax.bar(x_pos, accuracy, yerr=error, align='center', color =['r', 'b', 'g', 'gray', 'y', 'k'], alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Proportion of Subjects who Responded Beta')
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions)
ax.set_title('No-feedback performance on familiar Betas (Generative)')
ax.yaxis.grid(True)

# Save the figure
#plt.tight_layout()
plt.savefig('C:/Users/apers/Downloads/GloblocData/Generalization/gener_BetaGen_barplot.png')