import pandas as pd
import scipy.stats as stats
import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt

total_means_discr = pd.read_csv("C:/Users/apers/Downloads/GloblocData/SSL_Stats/discr_Train1_PerSubj_total.csv")
total_means_gener = pd.read_csv("C:/Users/apers/Downloads/GloblocData/SSL_Stats/gener_Train1_PerSubj_total.csv")


A6_discr = pd.read_csv('C:/Users/apers/Downloads/GloblocData/SSL_Stats/discr_Train1_PerSubj_A6.csv')
B4_discr = pd.read_csv('C:/Users/apers/Downloads/GloblocData/SSL_Stats/discr_Train1_PerSubj_B4.csv')

A6_gener = pd.read_csv('C:/Users/apers/Downloads/GloblocData/SSL_Stats/gener_Train1_PerSubj_A6.csv')
B4_gener = pd.read_csv('C:/Users/apers/Downloads/GloblocData/SSL_Stats/gener_Train1_PerSubj_B4.csv')


block1_totals_discr = []
block2_totals_discr = []
block3_totals_discr = []

block1_totals_gener = []
block2_totals_gener = []
block3_totals_gener = []

block1_A6_discr = []
block2_A6_discr = []
block3_A6_discr = []

block1_B4_discr = []
block2_B4_discr = []
block3_B4_discr = []

block1_A6_gener = []
block2_A6_gener = []
block3_A6_gener = []

block1_B4_gener = []
block2_B4_gener = []
block3_B4_gener = []








#add all availabe data for block 1 totals discr into the appropriate lists
for i, row in total_means_discr.iterrows():
    if row.block_data == 1:
        block1_totals_discr.append(row.means)

#add all availabe data for block 1 A6 discr into the appropriate lists
for i, row in A6_discr.iterrows():
    if row.block_data == 1:
        block1_A6_discr.append(row.means)

#add all availabe data for block 1 B4 discr into the appropriate lists
for i, row in B4_discr.iterrows():
    if row.block_data == 1:
        block1_B4_discr.append(row.means)





#add all availabe data for block 1 totals gener into the appropriate lists
for i, row in total_means_gener.iterrows():
    if row.block_data == 1:
        block1_totals_gener.append(row.means)

#add all availabe data for block 1 A6 gener into the appropriate lists
for i, row in A6_gener.iterrows():
    if row.block_data == 1:
        block1_A6_gener.append(row.means)

#add all availabe data for block 1 B4 gener into the appropriate lists
for i, row in B4_gener.iterrows():
    if row.block_data == 1:
        block1_B4_gener.append(row.means)





#add all availabe data for block 2 totals discr into the appropriate lists
for i, row in total_means_discr.iterrows():
    if row.block_data == 2:
        block2_totals_discr.append(row.means)

#add all availabe data for block 2 A6 discr into the appropriate lists
for i, row in A6_discr.iterrows():
    if row.block_data == 2:
        block2_A6_discr.append(row.means)

#add all availabe data for block 2 B4 discr into the appropriate lists
for i, row in B4_discr.iterrows():
    if row.block_data == 2:
        block2_B4_discr.append(row.means)




#add all availabe data for block 2  totals gener into the appropriate lists
for i, row in total_means_gener.iterrows():
    if row.block_data == 2:
        block2_totals_gener.append(row.means)

#add all availabe data for block 2  A6 gener into the appropriate lists
for i, row in A6_gener.iterrows():
    if row.block_data == 2:
        block2_A6_gener.append(row.means)

#add all availabe data for block 2 B4 gener into the appropriate lists
for i, row in B4_gener.iterrows():
    if row.block_data == 2:
        block2_B4_gener.append(row.means)







#add all availabe data for block 3 totals discr into the appropriate lists
for i, row in total_means_discr.iterrows():
    if row.block_data == 3:
        block3_totals_discr.append(row.means)
        
#add all availabe data for block 3 A6 discr into the appropriate lists
for i, row in A6_discr.iterrows():
    if row.block_data == 3:
        block3_A6_discr.append(row.means)

#add all availabe data for block 3 B4 discr into the appropriate lists
for i, row in B4_discr.iterrows():
    if row.block_data == 3:
        block3_B4_discr.append(row.means)







#add all availabe data for block 3 totals gener into the appropriate lists
for i, row in total_means_gener.iterrows():
    if row.block_data == 3:
        block3_totals_gener.append(row.means)

#add all availabe data for block 3 A6 gener into the appropriate lists
for i, row in A6_gener.iterrows():
    if row.block_data == 3:
        block3_A6_gener.append(row.means)

#add all availabe data for block 3 B4 gener into the appropriate lists
for i, row in B4_gener.iterrows():
    if row.block_data == 3:
        block3_B4_gener.append(row.means)






#n for discriminative is equal to 35 subjects
n_discr = 35

#n for generative is equal to 34 subjects
n_gener = 34

crit_num = 0.92
#########################################################################################################################################
#fix lists of the first three blocks for discr totals
#block 1 discr totals
countB1T = 0
for i in block1_totals_discr:
    countB1T += 1
num_missingB1T = n_discr - countB1T
print('this is block 1 discr totals original:')
print(countB1T)
print(num_missingB1T)
while num_missingB1T != 0:
    block1_totals_discr.append(0.92)
    num_missingB1T -= 1


countB1T = 0
for i in block1_totals_discr:
    countB1T += 1
print('this is block 1 discr totals fixed:')
print(countB1T)
print(num_missingB1T)


#block 2 discr totals
countB2T = 0
for i in block2_totals_discr:
    countB2T += 1
num_missingB2T = n_discr - countB2T
print('this is block 2 discr totals original:')
print(countB2T)
print(num_missingB2T)
while num_missingB2T != 0:
    block2_totals_discr.append(0.92)
    num_missingB2T -= 1


countB2T = 0
for i in block2_totals_discr:
    countB2T += 1
print('this is block 2 discr totals fixed:')
print(countB2T)
print(num_missingB2T)


#block 3 discr totals
countB3T = 0
for i in block3_totals_discr:
    countB3T += 1

num_missingB3T = n_discr - countB3T
print('this is block 3 discr totals original:')
print(countB3T)
print(num_missingB3T)

while num_missingB3T != 0:
    block3_totals_discr.append(0.92)
    num_missingB3T -= 1


countB3T = 0
for i in block3_totals_discr:
    countB3T += 1
print('this is block 3 discr totals fixed:')
print(countB3T)
print(num_missingB3T)
#combine lists
blocks_combined_discr_totals = block1_totals_discr + block2_totals_discr + block3_totals_discr

##################################################################################################################################################
#fix lists for first three blocks of gener totals
#block 1 gener totals
countB1TG = 0
for i in block1_totals_gener:
    countB1TG += 1
num_missingB1TG = n_gener - countB1TG
print('this is block 1 gener totals original:')
print(countB1TG)
print(num_missingB1TG)
while num_missingB1TG != 0:
    block1_totals_gener.append(0.92)
    num_missingB1TG -= 1


countB1TG = 0
for i in block1_totals_gener:
    countB1TG += 1
print('this is block 1 gener totals fixed:')
print(countB1TG)
print(num_missingB1TG)


#block 2 gener totals
countB2TG = 0

for i in block2_totals_gener:
    countB2TG += 1
num_missingB2TG = n_gener - countB2TG
print('this is block 2 gener totals original:')
print(countB2TG)
print(num_missingB2TG)
while num_missingB2TG != 0:
    block2_totals_gener.append(0.92)
    num_missingB2TG -= 1


countB2TG = 0
for i in block2_totals_gener:
    countB2TG += 1
print('this is block 2 gener totals fixed:')
print(countB2TG)
print(num_missingB2TG)


#block 3 gener totals
countB3TG = 0
for i in block3_totals_gener:
    countB3TG += 1

num_missingB3TG = n_gener - countB3TG
print('this is block 3 gener totals original:')
print(countB3TG)
print(num_missingB3TG)

while num_missingB3TG != 0:
    block3_totals_gener.append(0.92)
    num_missingB3TG -= 1


countB3TG = 0
for i in block3_totals_gener:
    countB3TG += 1
print('this is block 3 gener totals fixed:')
print(countB3TG)
print(num_missingB3TG)
#combine lists
blocks_combined_gener_totals = block1_totals_gener + block2_totals_gener + block3_totals_gener

##################################################################################################################################################
#fix lists for first three blocks of A6 discr
#block 1 A6 discr
countB1A6D = 0
for i in block1_A6_discr:
    countB1A6D += 1
num_missingB1A6D = n_discr - countB1A6D
print('this is block 1 A6 discr original:')
print(countB1A6D)
print(num_missingB1A6D)
while num_missingB1A6D != 0:
    block1_A6_discr.append(0.92)
    num_missingB1A6D -= 1


countB1A6D = 0
for i in block1_A6_discr:
    countB1A6D += 1
print('this is block 1 A6 discr fixed:')
print(countB1A6D)
print(num_missingB1A6D)


#block 2 A6 discr
countB2A6D = 0

for i in block2_A6_discr:
    countB2A6D += 1

num_missingB2A6D = n_discr - countB2A6D
print('this is block 2 A6 discr original:')
print(countB2A6D)
print(num_missingB2A6D)
while num_missingB2A6D != 0:
    block2_A6_discr.append(0.92)
    num_missingB2A6D -= 1


countB2A6D = 0
for i in block2_A6_discr:
    countB2A6D += 1
print('this is block 2 A6 discr fixed:')
print(countB2A6D)
print(num_missingB2A6D)


#block 3 A6 discr
countB3A6D = 0
for i in block3_A6_discr:
    countB3A6D += 1

num_missingB3A6D = n_discr - countB3A6D
print('this is block 3 A6 discr original:')
print(countB3A6D)
print(num_missingB3A6D)

while num_missingB3A6D != 0:
    block3_A6_discr.append(0.92)
    num_missingB3A6D -= 1


countB3A6D = 0
for i in block3_A6_discr:
    countB3A6D += 1
print('this is block 3 A6 discr fixed:')
print(countB3A6D)
print(num_missingB3A6D)
#combine lists
blocks_combined_discr_A6 = block1_A6_discr + block2_A6_discr + block3_A6_discr



##################################################################################################################################################
#fix lists for first three blocks of A6 gener 
#block 1 A6 gener
countB1A6G = 0
for i in block1_A6_gener:
    countB1A6G += 1
num_missingB1A6G = n_gener - countB1A6G
print('this is block 1 A6 gener original:')
print(countB1A6G)
print(num_missingB1A6G)
while num_missingB1A6G != 0:
    block1_A6_gener.append(0.92)
    num_missingB1A6G -= 1


countB1A6G = 0
for i in block1_A6_gener:
    countB1A6G += 1
print('this is block 1 A6 gener fixed:')
print(countB1A6G)
print(num_missingB1A6G)


#block 2 A6 gener
countB2A6G = 0

for i in block2_A6_gener:
    countB2A6G += 1

num_missingB2A6G = n_gener - countB2A6G
print('this is block 2 A6 gener original:')
print(countB2A6G)
print(num_missingB2A6G)
while num_missingB2A6G != 0:
    block2_A6_gener.append(0.92)
    num_missingB2A6G -= 1


countB2A6G = 0
for i in block2_A6_gener:
    countB2A6G += 1
print('this is block 2 A6 gener fixed:')
print(countB2A6G)
print(num_missingB2A6G)


#block 3 A6 gener
countB3A6G = 0
for i in block3_A6_gener:
    countB3A6G += 1

num_missingB3A6G = n_gener - countB3A6G
print('this is block 3 A6 gener original:')
print(countB3A6G)
print(num_missingB3A6G)

while num_missingB3A6G != 0:
    block3_A6_gener.append(0.92)
    num_missingB3A6G -= 1


countB3A6G = 0
for i in block3_A6_gener:
    countB3A6G += 1
print('this is block 3 A6 gener fixed:')
print(countB3A6G)
print(num_missingB3A6G)
#combine lists
blocks_combined_gener_A6 = block1_A6_gener + block2_A6_gener + block3_A6_gener


##################################################################################################################################################
#fix lists for first three blocks of B4 discr 
#block 1 B4 discr
countB1B4D = 0
for i in block1_B4_discr:
    countB1B4D += 1
num_missingB1B4D = n_discr - countB1B4D
print('this is block 1 B4 discr original:')
print(countB1B4D)
print(num_missingB1B4D)
while num_missingB1B4D != 0:
    block1_B4_discr.append(0.92)
    num_missingB1B4D -= 1


countB1B4D= 0
for i in block1_B4_discr:
    countB1B4D += 1
print('this is block 1 B4 discr fixed:')
print(countB1B4D)
print(num_missingB1B4D)


#block 2 B4 discr
countB2B4D = 0

for i in block2_B4_discr:
    countB2B4D += 1

num_missingB2B4D = n_discr - countB2B4D
print('this is block 2 B4 discr original:')
print(countB2B4D)
print(num_missingB2B4D)
while num_missingB2B4D != 0:
    block2_B4_discr.append(0.92)
    num_missingB2B4D -= 1


countB2B4D = 0
for i in block2_B4_discr:
    countB2B4D += 1
print('this is block 2 B4 discr fixed:')
print(countB2B4D)
print(num_missingB2B4D)


#block 3 B4 discr
countB3B4D = 0
for i in block3_B4_discr:
    countB3B4D += 1

num_missingB3B4D = n_discr - countB3B4D
print('this is block 3 B4 discr original:')
print(countB3B4D)
print(num_missingB3B4D)

while num_missingB3B4D != 0:
    block3_B4_discr.append(0.92)
    num_missingB3B4D -= 1


countB3B4D = 0
for i in block3_B4_discr:
    countB3B4D += 1
print('this is block 3 B4 discr fixed:')
print(countB3B4D)
print(num_missingB3B4D)
#combine lists
blocks_combined_discr_B4 = block1_B4_discr + block2_B4_discr + block3_B4_discr





##################################################################################################################################################
#fix lists for first three blocks of B4 gener 
#block 1 B4 gener
countB1B4G = 0
for i in block1_B4_gener:
    countB1B4G += 1
num_missingB1B4G = n_gener - countB1B4G
print('this is block 1 B4 gener original:')
print(countB1B4G)
print(num_missingB1B4G)
while num_missingB1B4G != 0:
    block1_B4_gener.append(0.92)
    num_missingB1B4G -= 1


countB1B4G= 0
for i in block1_B4_gener:
    countB1B4G += 1
print('this is block 1 B4 gener fixed:')
print(countB1B4G)
print(num_missingB1B4G)


#block 2 B4 discr
countB2B4G = 0

for i in block2_B4_gener:
    countB2B4G += 1

num_missingB2B4G = n_gener - countB2B4G
print('this is block 2 B4 gener original:')
print(countB2B4G)
print(num_missingB2B4G)
while num_missingB2B4G != 0:
    block2_B4_gener.append(0.92)
    num_missingB2B4G -= 1


countB2B4G = 0
for i in block2_B4_gener:
    countB2B4G += 1
print('this is block 2 B4 gener fixed:')
print(countB2B4G)
print(num_missingB2B4G)


#block 3 B4 gener
countB3B4G = 0
for i in block3_B4_gener:
    countB3B4G += 1

num_missingB3B4G = n_gener - countB3B4G
print('this is block 3 B4 gener original:')
print(countB3B4G)
print(num_missingB3B4G)

while num_missingB3B4G != 0:
    block3_B4_gener.append(0.92)
    num_missingB3B4G -= 1


countB3B4G = 0
for i in block3_B4_gener:
    countB3B4G += 1
print('this is block 3 B4 gener fixed:')
print(countB3B4G)
print(num_missingB3B4G)
#combine lists
blocks_combined_gener_B4 = block1_B4_gener + block2_B4_gener + block3_B4_gener
###########################################################################################################################################
###########################################################################################################################################
###################################                    TTESTS NOW                  #######################################################
###########################################################################################################################################
###########################################################################################################################################



print('t-test discr totals vs A6 discr')
print(stats.ttest_rel(blocks_combined_discr_totals, blocks_combined_discr_A6))

print('t-test discr totals vs B4 discr')
print(stats.ttest_rel(blocks_combined_discr_totals, blocks_combined_discr_B4))

print('t-test discr A6 vs B4 discr')
print(stats.ttest_rel(blocks_combined_discr_A6, blocks_combined_discr_B4))







print('t-test gener totals vs A6 gener')
print(stats.ttest_rel(blocks_combined_gener_totals, blocks_combined_gener_A6))


print('t-test gener totals vs B4 gener')
print(stats.ttest_rel(blocks_combined_gener_totals, blocks_combined_gener_B4))

print('t-test gener A6 vs B4 gener')
print(stats.ttest_rel(blocks_combined_gener_A6, blocks_combined_gener_B4))

###################################################################################################################################################
###################################################################################################################################################
###########################################              GRAPH   NOW                   #######################################################
###################################################################################################################################################
###################################################################################################################################################

#discriminative means and srtandard errors for the bar graph
discr_totals_mean = np.mean(blocks_combined_discr_totals)
err_discr_totals = sem(blocks_combined_discr_totals)

discr_A6_mean = np.mean(blocks_combined_discr_A6)
err_discr_A6 = sem(blocks_combined_discr_A6)

discr_B4_mean = np.mean(blocks_combined_discr_B4)
err_discr_B4 = sem(blocks_combined_discr_B4)


#generative means and srtandard errors for the bar graph
gener_totals_mean = np.mean(blocks_combined_gener_totals)
err_gener_totals = sem(blocks_combined_gener_totals)

gener_A6_mean = np.mean(blocks_combined_gener_A6)
err_gener_A6 = sem(blocks_combined_gener_A6)

gener_B4_mean = np.mean(blocks_combined_gener_B4)
err_gener_B4 = sem(blocks_combined_gener_B4)


conditions = ['Overall Performance', 'Performance on A6', 'Performance on B4']
x_pos = np.arange(len(conditions))
accuracy = [discr_totals_mean, discr_A6_mean, discr_B4_mean]
error = [err_discr_totals, err_discr_A6, err_discr_B4]

# Build the plot
fig, ax = plt.subplots()
plt.ylim(0,1)
ax.bar(x_pos, accuracy, yerr=error, align='center', color =['r', 'b', 'g'], alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Accuracy')
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions)
ax.set_title('Performance Across The First Three Training Blocks (Discriminative)')
ax.yaxis.grid(True)

# Save the figure
#plt.tight_layout()
plt.savefig('C:/Users/apers/Downloads/GloblocData/SSL_Stats/discr_acc_barplot.png')