import pandas as pd
import pingouin as pg
import scipy.stats as stats
import seaborn as sb

df = pd.read_csv('output.csv')

cond_1 = []
cond_2 = []
for i, row in df.iterrows():
    if row.condition == 1:
        cond_1.append(row.num2crit)
    else:
        cond_2.append(row.num2crit)

print(cond_1)
print(cond_2)

print(stats.ttest_ind(cond_1, cond_2))
