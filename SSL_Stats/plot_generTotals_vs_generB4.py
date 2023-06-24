import pandas as pd
import scipy.stats as stats
import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt


total_means_gener = pd.read_csv("C:/Users/apers/Downloads/GloblocData/SSL_Stats/gener_Train1_PerSubj_total.csv")
B4_gener = pd.read_csv('C:/Users/apers/Downloads/GloblocData/SSL_Stats/gener_Train1_PerSubj_B4.csv')



block1_totals_gener = []
block2_totals_gener = []
block3_totals_gener = []
block4_totals_gener = []
block5_totals_gener = []
block6_totals_gener = []
block7_totals_gener = []
block8_totals_gener = []



block1_B4_gener = []
block2_B4_gener = []
block3_B4_gener = []
block4_B4_gener = []
block5_B4_gener = []
block6_B4_gener = []
block7_B4_gener = []
block8_B4_gener = []


####################################################################################################################################
####################################################################################################################################

#add all availabe data for block 1 totals gener into the appropriate lists
for i, row in total_means_gener.iterrows():
    if row.block_data == 1:
        block1_totals_gener.append(row.means)
#add all availabe data for block 2 totals gener into the appropriate lists
for i, row in total_means_gener.iterrows():
    if row.block_data == 2:
        block2_totals_gener.append(row.means)

#add all availabe data for block 3 totals gener into the appropriate lists
for i, row in total_means_gener.iterrows():
    if row.block_data == 3:
        block3_totals_gener.append(row.means)

#add all availabe data for block 4 totals gener into the appropriate lists
for i, row in total_means_gener.iterrows():
    if row.block_data == 4:
        block4_totals_gener.append(row.means)

#add all availabe data for block 5 totals gener into the appropriate lists
for i, row in total_means_gener.iterrows():
    if row.block_data == 5:
        block5_totals_gener.append(row.means)

#add all availabe data for block 6 totals gener into the appropriate lists
for i, row in total_means_gener.iterrows():
    if row.block_data == 6:
        block6_totals_gener.append(row.means)

#add all availabe data for block 7 totals gener into the appropriate lists
for i, row in total_means_gener.iterrows():
    if row.block_data == 7:
        block7_totals_gener.append(row.means)

#add all availabe data for block 8 totals gener into the appropriate lists
for i, row in total_means_gener.iterrows():
    if row.block_data == 8:
        block8_totals_gener.append(row.means)


#############################################################################################################################################
#############################################################################################################################################


#add all availabe data for block 1 B4 gener into the appropriate lists
for i, row in B4_gener.iterrows():
    if row.block_data == 1:
        block1_B4_gener.append(row.means)
#add all availabe data for block 2 B4 gener into the appropriate lists
for i, row in B4_gener.iterrows():
    if row.block_data == 2:
        block2_B4_gener.append(row.means)
#add all availabe data for block 3 B4 gener into the appropriate lists
for i, row in B4_gener.iterrows():
    if row.block_data == 3:
        block3_B4_gener.append(row.means)
#add all availabe data for block 4 B4 gener into the appropriate lists
for i, row in B4_gener.iterrows():
    if row.block_data == 4:
        block4_B4_gener.append(row.means)
#add all availabe data for block 5 B4 gener into the appropriate lists
for i, row in B4_gener.iterrows():
    if row.block_data == 5:
        block5_B4_gener.append(row.means)
#add all availabe data for block 6 B4 gener into the appropriate lists
for i, row in B4_gener.iterrows():
    if row.block_data == 6:
        block6_B4_gener.append(row.means)
#add all availabe data for block 7 B4 gener into the appropriate lists
for i, row in B4_gener.iterrows():
    if row.block_data == 7:
        block7_B4_gener.append(row.means)
#add all availabe data for block 8 B4 gener into the appropriate lists
for i, row in B4_gener.iterrows():
    if row.block_data == 8:
        block8_B4_gener.append(row.means)



########################################################################################################################################################
########################################################################################################################################################

#n for generiminative is equal to 35 subjects
n_gener = 35

#n for generative is equal to 34 subjects
n_gener = 34

crit_num = 0.92





##################################################################################################################################################
#fix lists for gener totals
#block 1 gener totals
countB1T = 0
for i in block1_totals_gener:
    countB1T += 1
num_missingB1T = n_gener - countB1T
print('this is block 1 gener totals original:')
print(countB1T)
print(num_missingB1T)
while num_missingB1T != 0:
    block1_totals_gener.append(0.92)
    num_missingB1T -= 1


countB1T = 0
for i in block1_totals_gener:
    countB1T += 1
print('this is block 1 gener totals fixed:')
print(countB1T)
print(num_missingB1T)








#block 2 gener totals
countB2T = 0
for i in block2_totals_gener:
    countB2T += 1
num_missingB2T = n_gener - countB2T
print('this is block 2 gener totals original:')
print(countB2T)
print(num_missingB2T)
while num_missingB2T != 0:
    block2_totals_gener.append(0.92)
    num_missingB2T -= 1


countB2T = 0
for i in block2_totals_gener:
    countB2T += 1
print('this is block 2 gener totals fixed:')
print(countB2T)
print(num_missingB2T)







#block 3 gener totals
countB3T = 0
for i in block3_totals_gener:
    countB3T += 1

num_missingB3T = n_gener - countB3T
print('this is block 3 gener totals original:')
print(countB3T)
print(num_missingB3T)

while num_missingB3T != 0:
    block3_totals_gener.append(0.92)
    num_missingB3T -= 1


countB3T = 0
for i in block3_totals_gener:
    countB3T += 1
print('this is block 3 gener totals fixed:')
print(countB3T)
print(num_missingB3T)







#block 4 gener totals
countB4T = 0
for i in block4_totals_gener:
    countB4T += 1

num_missingB4T = n_gener - countB4T
print('this is block 4 gener totals original:')
print(countB4T)
print(num_missingB4T)

while num_missingB4T != 0:
    block4_totals_gener.append(0.92)
    num_missingB4T -= 1


countB4T = 0
for i in block4_totals_gener:
    countB4T += 1
print('this is block 4 gener totals fixed:')
print(countB4T)
print(num_missingB4T)







#block 5 gener totals
countB5T = 0
for i in block5_totals_gener:
    countB5T += 1

num_missingB5T = n_gener - countB5T
print('this is block 5 gener totals original:')
print(countB5T)
print(num_missingB5T)

while num_missingB5T != 0:
    block5_totals_gener.append(0.92)
    num_missingB5T -= 1


countB5T = 0
for i in block5_totals_gener:
    countB5T += 1
print('this is block 5 gener totals fixed:')
print(countB5T)
print(num_missingB5T)








#block 6 gener totals
countB6T = 0
for i in block6_totals_gener:
    countB6T += 1

num_missingB6T = n_gener - countB6T
print('this is block 6 gener totals original:')
print(countB6T)
print(num_missingB6T)

while num_missingB6T != 0:
    block6_totals_gener.append(0.92)
    num_missingB6T -= 1


countB6T = 0
for i in block6_totals_gener:
    countB6T += 1
print('this is block 6 gener totals fixed:')
print(countB6T)
print(num_missingB6T)








#block 7 gener totals
countB7T = 0
for i in block7_totals_gener:
    countB7T += 1

num_missingB7T = n_gener - countB7T
print('this is block 7 gener totals original:')
print(countB7T)
print(num_missingB7T)

while num_missingB7T != 0:
    block7_totals_gener.append(0.92)
    num_missingB7T -= 1


countB7T = 0
for i in block7_totals_gener:
    countB7T += 1
print('this is block 7 gener totals fixed:')
print(countB7T)
print(num_missingB7T)







#block 8 gener totals
countB8T = 0
for i in block8_totals_gener:
    countB8T += 1

num_missingB8T = n_gener - countB8T
print('this is block 8 gener totals original:')
print(countB8T)
print(num_missingB8T)

while num_missingB8T != 0:
    block8_totals_gener.append(0.92)
    num_missingB8T -= 1


countB8T = 0
for i in block8_totals_gener:
    countB8T += 1
print('this is block 8 gener totals fixed:')
print(countB8T)
print(num_missingB8T)

#####################################################################################################################################################


#fix lists for gener B4
#block 1 gener B4
countB1B4 = 0
for i in block1_B4_gener:
    countB1B4 += 1
num_missingB1B4 = n_gener - countB1B4
print('this is block 1 gener B4 original:')
print(countB1B4)
print(num_missingB1B4)
while num_missingB1B4 != 0:
    block1_B4_gener.append(0.92)
    num_missingB1B4 -= 1


countB1B4 = 0
for i in block1_B4_gener:
    countB1B4 += 1
print('this is block 1 B4 totals fixed:')
print(countB1B4)
print(num_missingB1B4)








#block 2 gener B4
countB2B4 = 0
for i in block2_B4_gener:
    countB2B4 += 1
num_missingB2B4 = n_gener - countB2B4
print('this is block 2 gener B4 original:')
print(countB2B4)
print(num_missingB2B4)
while num_missingB2B4 != 0:
    block2_B4_gener.append(0.92)
    num_missingB2B4 -= 1


countB2B4 = 0
for i in block2_B4_gener:
    countB2B4 += 1
print('this is block 2 B4 totals fixed:')
print(countB2B4)
print(num_missingB2B4)







#block 3 gener B4
countB3B4 = 0
for i in block3_B4_gener:
    countB3B4 += 1

num_missingB3B4 = n_gener - countB3B4
print('this is block 3 gener B4 original:')
print(countB3B4)
print(num_missingB3B4)

while num_missingB3B4 != 0:
    block3_B4_gener.append(0.92)
    num_missingB3B4 -= 1


countB3B4 = 0
for i in block3_B4_gener:
    countB3B4 += 1
print('this is block 3 gener B4 fixed:')
print(countB3B4)
print(num_missingB3B4)







#block 4 gener B4
countB4B4 = 0
for i in block4_B4_gener:
    countB4B4 += 1

num_missingB4B4 = n_gener - countB4B4
print('this is block 4 gener B4 original:')
print(countB4B4)
print(num_missingB4B4)

while num_missingB4B4 != 0:
    block4_B4_gener.append(0.92)
    num_missingB4B4 -= 1


countB4B4 = 0
for i in block4_B4_gener:
    countB4B4 += 1
print('this is block 4 gener B4 fixed:')
print(countB4B4)
print(num_missingB4B4)







#block 5 gener B4
countB5B4 = 0
for i in block5_B4_gener:
    countB5B4 += 1

num_missingB5B4 = n_gener - countB5B4
print('this is block 5 gener B4 original:')
print(countB5B4)
print(num_missingB5B4)

while num_missingB5B4 != 0:
    block5_B4_gener.append(0.92)
    num_missingB5B4 -= 1


countB5B4 = 0
for i in block5_B4_gener:
    countB5B4 += 1
print('this is block 5 gener B4 fixed:')
print(countB5B4)
print(num_missingB5B4)








#block 6 gener B4
countB6B4 = 0
for i in block6_B4_gener:
    countB6B4 += 1

num_missingB6B4 = n_gener - countB6B4
print('this is block 6 gener B4 original:')
print(countB6B4)
print(num_missingB6B4)

while num_missingB6B4 != 0:
    block6_B4_gener.append(0.92)
    num_missingB6B4 -= 1


countB6B4 = 0
for i in block6_B4_gener:
    countB6B4 += 1
print('this is block 6 gener B4 fixed:')
print(countB6B4)
print(num_missingB6B4)










#block 7 gener B4
countB7B4 = 0
for i in block7_B4_gener:
    countB7B4 += 1

num_missingB7B4 = n_gener - countB7B4
print('this is block 7 gener B4 original:')
print(countB7B4)
print(num_missingB7B4)

while num_missingB7B4 != 0:
    block7_B4_gener.append(0.92)
    num_missingB7B4 -= 1


countB7B4 = 0
for i in block7_B4_gener:
    countB7B4 += 1
print('this is block 7 gener B4 fixed:')
print(countB7B4)
print(num_missingB7B4)











#block 8 gener B4
countB8B4 = 0
for i in block8_B4_gener:
    countB8B4 += 1

num_missingB8B4 = n_gener - countB8B4
print('this is block 8 gener B4 original:')
print(countB8B4)
print(num_missingB8B4)

while num_missingB8B4 != 0:
    block8_B4_gener.append(0.92)
    num_missingB8B4 -= 1


countB8B4 = 0
for i in block8_B4_gener:
    countB8B4 += 1
print('this is block 8 gener B4 fixed:')
print(countB8B4)
print(num_missingB8B4)


#####################################################################################################################################################
#####################################################################################################################################################


M_block1_T = np.mean(block1_totals_gener)
err_block1_T = sem(block1_totals_gener)

M_block2_T = np.mean(block2_totals_gener)
err_block2_T = sem(block2_totals_gener)

M_block3_T = np.mean(block3_totals_gener)
err_block3_T = sem(block3_totals_gener)

M_block4_T = np.mean(block4_totals_gener)
err_block4_T = sem(block4_totals_gener)

M_block5_T = np.mean(block5_totals_gener)
err_block5_T = sem(block5_totals_gener)

M_block6_T = np.mean(block6_totals_gener)
err_block6_T = sem(block6_totals_gener)

M_block7_T = np.mean(block7_totals_gener)
err_block7_T = sem(block7_totals_gener)

M_block8_T = np.mean(block8_totals_gener)
err_block8_T = sem(block8_totals_gener)



#####################################################################################################################################################



M_block1_B4 = np.mean(block1_B4_gener)
err_block1_B4 = sem(block1_B4_gener)

M_block2_B4 = np.mean(block2_B4_gener)
err_block2_B4 = sem(block2_B4_gener)

M_block3_B4 = np.mean(block3_B4_gener)
err_block3_B4 = sem(block3_B4_gener)

M_block4_B4 = np.mean(block4_B4_gener)
err_block4_B4 = sem(block4_B4_gener)

M_block5_B4 = np.mean(block5_B4_gener)
err_block5_B4 = sem(block5_B4_gener)

M_block6_B4 = np.mean(block6_B4_gener)
err_block6_B4 = sem(block6_B4_gener)

M_block7_B4 = np.mean(block7_B4_gener)
err_block7_B4 = sem(block7_B4_gener)

M_block8_B4 = np.mean(block8_B4_gener)
err_block8_B4 = sem(block8_B4_gener)

#######################################################################################################################################################################
#######################################################################################################################################################################
##########################################                GRAPH  NOW                  #####################################################################################
#########################################################################################################################################################################
##############################################################################################################################################################################


block_data = [1,2,3,4,5,6,7,8]

totals_data = [M_block1_T, M_block2_T, M_block3_T, M_block4_T, M_block5_T, M_block6_T, M_block7_T, M_block8_T]
totals_err = [err_block1_T, err_block2_T, err_block3_T, err_block4_T, err_block5_T, err_block6_T, err_block7_T,err_block8_T]

B4_data = [M_block1_B4, M_block2_B4, M_block3_B4, M_block4_B4, M_block5_B4, M_block6_B4, M_block7_B4, M_block8_B4]
B4_err = [err_block1_B4, err_block2_B4, err_block3_B4, err_block4_B4, err_block5_B4, err_block6_B4, err_block7_B4, err_block8_B4]





plt.errorbar(block_data, totals_data, yerr= totals_err, color = 'k', label = 'Overall Performance', marker= 'o', markersize= 10)
plt.errorbar(block_data, B4_data, yerr= B4_err, color= 'r', label = 'B4', marker= 's', markersize= 10)



plt.ylim(0.2,1.05)
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.65, top=0.85)
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xlabel("Training Block")
plt.ylabel("Proportioin Correct")
plt.title("Training Phase 1: \n Overall Versus Beta 4 Performance (Generative)")
plt.savefig('C:/Users/apers/Downloads/GloblocData/SSL_Stats/generTotals_vs_generB4.png')







