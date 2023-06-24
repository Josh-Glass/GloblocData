import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


df1 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/discriminative_data.csv')

#drop training phase 1 and 2 so only left with test phase
df1 = df1.drop(index = df1[df1['phase_id'] == 'training_phase_1'].index)
df1 = df1.drop(index = df1[df1['phase_id']== 'training_phase_2'].index)

discr_list = [11016,
             11022,
             11024,
             11030,
             11034,
             11052,
             11080,
             11092,
             11094,
             ]

gener_list = [11023,
              11039,
              11071,
              11083,
              11098,
              11103,
             ]

newdf1 = df1[df1['pnum'].isin(list(discr_list))]


yGen4 = newdf1.drop(index = newdf1[newdf1['stim'] != 'materials/images/yGen4.png'].index)
yGen5 = newdf1.drop(index = newdf1[newdf1['stim'] != 'materials/images/yGen5.png'].index)

print(yGen4['rt'].mean())
print(yGen5['rt'].mean())
print(stats.ttest_ind(yGen4['rt'], yGen5['rt'], alternative='two-sided'))


print(yGen4['response'].mean())
print(yGen5['response'].mean())

print(stats.ttest_ind(yGen4['response'], yGen5['response'], alternative='two-sided'))

exit()


means_df1 = newdf1.groupby(['stim'], as_index= True)['response'].describe()

print(means_df1)

i=0

means_list = []
while i < 17:
 means_list.append(means_df1['mean'][i])
 i+=1



#print(means_list)


data_all = np.array([
     
     [.04,.98], # B
    [.12,.74], # B
    [.24,.88], # B

    [.36,.04], # B
    [.56,.1], # B
    [.7,.52], # B




    [.02,.02], # A
    [.08,.08], # A
    [.14,.14], # A

    [.2,.2], # A
    [.26,.26], # A
    [.32,.32], # A



    [.12, .28],  # generalization test item
    [.28, .12],  # generalzation test items
    [.48, .48],  # generalization test item
    [.6, .6],  # generalzation test items

    [.8, .6],  # generalzation test items

])

data_a = np.array([
  

    [.02,.02], # A
    [.08,.08], # A
    [.14,.14], # A

    [.2,.2], # A
    [.26,.26], # A
    [.32,.32], # A


])


data_b = np.array([

    [.04,.98], # B
    [.12,.74], # B
    [.24,.88], # B

    [.36,.04], # B
    [.56,.1], # B
    [.7,.52], # B

])

data_t = np.array([

    [.12, .28],  # generalization test item
    [.28, .12],  # generalzation test items
    [.48, .48],  # generalization test item
    [.6, .6],  # generalzation test items

    [.8, .6],  # generalzation test items

])




plt.scatter(data_a[:,0],data_a[:,1], c= 'w', s= 300, edgecolor= 'red', linewidths=3, marker= 'o', label= (r'$\alpha$'))
plt.scatter(data_b[:,0],data_b[:,1],c = 'w', s= 300, edgecolor= 'blue', linewidths=3, marker = 'o', label= (r'$\beta$'))
plt.scatter(data_t[:,0],data_t[:,1], c = 'w', s= 300, edgecolor= 'y', linewidths=3, marker = 'o', label = ('test'))
plt.scatter(data_all[:,0],data_all[:,1],cmap= 'bwr', c= means_list, s= 100, edgecolor= 'k', marker= 'o')


plt.legend(loc="upper right")
plt.colorbar(shrink=0.5, aspect=8, label='Proportion ' + (r'$\alpha$') + ' Response')
plt.xlabel("Shading")
plt.ylabel("Size")
plt.title("Subgroup Generalization Response (n=6)")

plt.savefig('C:/Users/apers/Downloads/GloblocData/perSubject/gen_subject_genplots/gener_subGroupG.png')