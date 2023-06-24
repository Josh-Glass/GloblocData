import pandas as pd
import scipy.stats as stats
import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt


total_means_discr = pd.read_csv("C:/Users/apers/Downloads/GloblocData/SSL_Stats/discr_Train1_PerSubj_total.csv")
A6_discr = pd.read_csv('C:/Users/apers/Downloads/GloblocData/SSL_Stats/discr_Train1_PerSubj_A6.csv')



block1_totals_discr = []
block2_totals_discr = []
block3_totals_discr = []
block4_totals_discr = []
block5_totals_discr = []
block6_totals_discr = []
block7_totals_discr = []
block8_totals_discr = []



block1_A6_discr = []
block2_A6_discr = []
block3_A6_discr = []
block4_A6_discr = []
block5_A6_discr = []
block6_A6_discr = []
block7_A6_discr = []
block8_A6_discr = []


####################################################################################################################################
####################################################################################################################################

#add all availabe data for block 1 totals discr into the appropriate lists
for i, row in total_means_discr.iterrows():
    if row.block_data == 1:
        block1_totals_discr.append(row.means)
#add all availabe data for block 2 totals discr into the appropriate lists
for i, row in total_means_discr.iterrows():
    if row.block_data == 2:
        block2_totals_discr.append(row.means)

#add all availabe data for block 3 totals discr into the appropriate lists
for i, row in total_means_discr.iterrows():
    if row.block_data == 3:
        block3_totals_discr.append(row.means)

#add all availabe data for block 4 totals discr into the appropriate lists
for i, row in total_means_discr.iterrows():
    if row.block_data == 4:
        block4_totals_discr.append(row.means)

#add all availabe data for block 5 totals discr into the appropriate lists
for i, row in total_means_discr.iterrows():
    if row.block_data == 5:
        block5_totals_discr.append(row.means)

#add all availabe data for block 6 totals discr into the appropriate lists
for i, row in total_means_discr.iterrows():
    if row.block_data == 6:
        block6_totals_discr.append(row.means)

#add all availabe data for block 7 totals discr into the appropriate lists
for i, row in total_means_discr.iterrows():
    if row.block_data == 7:
        block7_totals_discr.append(row.means)

#add all availabe data for block 8 totals discr into the appropriate lists
for i, row in total_means_discr.iterrows():
    if row.block_data == 8:
        block8_totals_discr.append(row.means)


#############################################################################################################################################
#############################################################################################################################################


#add all availabe data for block 1 A6 discr into the appropriate lists
for i, row in A6_discr.iterrows():
    if row.block_data == 1:
        block1_A6_discr.append(row.means)
#add all availabe data for block 2 A6 discr into the appropriate lists
for i, row in A6_discr.iterrows():
    if row.block_data == 2:
        block2_A6_discr.append(row.means)
#add all availabe data for block 3 A6 discr into the appropriate lists
for i, row in A6_discr.iterrows():
    if row.block_data == 3:
        block3_A6_discr.append(row.means)
#add all availabe data for block 4 A6 discr into the appropriate lists
for i, row in A6_discr.iterrows():
    if row.block_data == 4:
        block4_A6_discr.append(row.means)
#add all availabe data for block 5 A6 discr into the appropriate lists
for i, row in A6_discr.iterrows():
    if row.block_data == 5:
        block5_A6_discr.append(row.means)
#add all availabe data for block 6 A6 discr into the appropriate lists
for i, row in A6_discr.iterrows():
    if row.block_data == 6:
        block6_A6_discr.append(row.means)
#add all availabe data for block 7 A6 discr into the appropriate lists
for i, row in A6_discr.iterrows():
    if row.block_data == 7:
        block7_A6_discr.append(row.means)
#add all availabe data for block 8 A6 discr into the appropriate lists
for i, row in A6_discr.iterrows():
    if row.block_data == 8:
        block8_A6_discr.append(row.means)



########################################################################################################################################################
########################################################################################################################################################

#n for discriminative is equal to 35 subjects
n_discr = 35

#n for generative is equal to 34 subjects
n_gener = 34

crit_num = 0.92





##################################################################################################################################################
#fix lists for discr totals
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







#block 4 discr totals
countB4T = 0
for i in block4_totals_discr:
    countB4T += 1

num_missingB4T = n_discr - countB4T
print('this is block 4 discr totals original:')
print(countB4T)
print(num_missingB4T)

while num_missingB4T != 0:
    block4_totals_discr.append(0.92)
    num_missingB4T -= 1


countB4T = 0
for i in block4_totals_discr:
    countB4T += 1
print('this is block 4 discr totals fixed:')
print(countB4T)
print(num_missingB4T)







#block 5 discr totals
countB5T = 0
for i in block5_totals_discr:
    countB5T += 1

num_missingB5T = n_discr - countB5T
print('this is block 5 discr totals original:')
print(countB5T)
print(num_missingB5T)

while num_missingB5T != 0:
    block5_totals_discr.append(0.92)
    num_missingB5T -= 1


countB5T = 0
for i in block5_totals_discr:
    countB5T += 1
print('this is block 5 discr totals fixed:')
print(countB5T)
print(num_missingB5T)








#block 6 discr totals
countB6T = 0
for i in block6_totals_discr:
    countB6T += 1

num_missingB6T = n_discr - countB6T
print('this is block 6 discr totals original:')
print(countB6T)
print(num_missingB6T)

while num_missingB6T != 0:
    block6_totals_discr.append(0.92)
    num_missingB6T -= 1


countB6T = 0
for i in block6_totals_discr:
    countB6T += 1
print('this is block 6 discr totals fixed:')
print(countB6T)
print(num_missingB6T)








#block 7 discr totals
countB7T = 0
for i in block7_totals_discr:
    countB7T += 1

num_missingB7T = n_discr - countB7T
print('this is block 7 discr totals original:')
print(countB7T)
print(num_missingB7T)

while num_missingB7T != 0:
    block7_totals_discr.append(0.92)
    num_missingB7T -= 1


countB7T = 0
for i in block7_totals_discr:
    countB7T += 1
print('this is block 7 discr totals fixed:')
print(countB7T)
print(num_missingB7T)







#block 8 discr totals
countB8T = 0
for i in block8_totals_discr:
    countB8T += 1

num_missingB8T = n_discr - countB8T
print('this is block 8 discr totals original:')
print(countB8T)
print(num_missingB8T)

while num_missingB8T != 0:
    block8_totals_discr.append(0.92)
    num_missingB8T -= 1


countB8T = 0
for i in block8_totals_discr:
    countB8T += 1
print('this is block 8 discr totals fixed:')
print(countB8T)
print(num_missingB8T)

#####################################################################################################################################################


#fix lists for discr A6
#block 1 discr A6
countB1A6 = 0
for i in block1_A6_discr:
    countB1A6 += 1
num_missingB1A6 = n_discr - countB1A6
print('this is block 1 discr A6 original:')
print(countB1A6)
print(num_missingB1A6)
while num_missingB1A6 != 0:
    block1_A6_discr.append(0.92)
    num_missingB1A6 -= 1


countB1A6 = 0
for i in block1_A6_discr:
    countB1A6 += 1
print('this is block 1 A6 totals fixed:')
print(countB1A6)
print(num_missingB1A6)








#block 2 discr A6
countB2A6 = 0
for i in block2_A6_discr:
    countB2A6 += 1
num_missingB2A6 = n_discr - countB2A6
print('this is block 2 discr A6 original:')
print(countB2A6)
print(num_missingB2A6)
while num_missingB2A6 != 0:
    block2_A6_discr.append(0.92)
    num_missingB2A6 -= 1


countB2A6 = 0
for i in block2_A6_discr:
    countB2A6 += 1
print('this is block 2 A6 totals fixed:')
print(countB2A6)
print(num_missingB2A6)







#block 3 discr A6
countB3A6 = 0
for i in block3_A6_discr:
    countB3A6 += 1

num_missingB3A6 = n_discr - countB3A6
print('this is block 3 discr A6 original:')
print(countB3A6)
print(num_missingB3A6)

while num_missingB3A6 != 0:
    block3_A6_discr.append(0.92)
    num_missingB3A6 -= 1


countB3A6 = 0
for i in block3_A6_discr:
    countB3A6 += 1
print('this is block 3 discr A6 fixed:')
print(countB3A6)
print(num_missingB3A6)







#block 4 discr A6
countB4A6 = 0
for i in block4_A6_discr:
    countB4A6 += 1

num_missingB4A6 = n_discr - countB4A6
print('this is block 4 discr A6 original:')
print(countB4A6)
print(num_missingB4A6)

while num_missingB4A6 != 0:
    block4_A6_discr.append(0.92)
    num_missingB4A6 -= 1


countB4A6 = 0
for i in block4_A6_discr:
    countB4A6 += 1
print('this is block 4 discr A6 fixed:')
print(countB4A6)
print(num_missingB4A6)







#block 5 discr A6
countB5A6 = 0
for i in block5_A6_discr:
    countB5A6 += 1

num_missingB5A6 = n_discr - countB5A6
print('this is block 5 discr A6 original:')
print(countB5A6)
print(num_missingB5A6)

while num_missingB5A6 != 0:
    block5_A6_discr.append(0.92)
    num_missingB5A6 -= 1


countB5A6 = 0
for i in block5_A6_discr:
    countB5A6 += 1
print('this is block 5 discr A6 fixed:')
print(countB5A6)
print(num_missingB5A6)








#block 6 discr A6
countB6A6 = 0
for i in block6_A6_discr:
    countB6A6 += 1

num_missingB6A6 = n_discr - countB6A6
print('this is block 6 discr A6 original:')
print(countB6A6)
print(num_missingB6A6)

while num_missingB6A6 != 0:
    block6_A6_discr.append(0.92)
    num_missingB6A6 -= 1


countB6A6 = 0
for i in block6_A6_discr:
    countB6A6 += 1
print('this is block 6 discr A6 fixed:')
print(countB6A6)
print(num_missingB6A6)










#block 7 discr A6
countB7A6 = 0
for i in block7_A6_discr:
    countB7A6 += 1

num_missingB7A6 = n_discr - countB7A6
print('this is block 7 discr A6 original:')
print(countB7A6)
print(num_missingB7A6)

while num_missingB7A6 != 0:
    block7_A6_discr.append(0.92)
    num_missingB7A6 -= 1


countB7A6 = 0
for i in block7_A6_discr:
    countB7A6 += 1
print('this is block 7 discr A6 fixed:')
print(countB7A6)
print(num_missingB7A6)











#block 8 discr A6
countB8A6 = 0
for i in block8_A6_discr:
    countB8A6 += 1

num_missingB8A6 = n_discr - countB8A6
print('this is block 8 discr A6 original:')
print(countB8A6)
print(num_missingB8A6)

while num_missingB8A6 != 0:
    block8_A6_discr.append(0.92)
    num_missingB8A6 -= 1


countB8A6 = 0
for i in block8_A6_discr:
    countB8A6 += 1
print('this is block 8 discr A6 fixed:')
print(countB8A6)
print(num_missingB8A6)


#####################################################################################################################################################
#####################################################################################################################################################


M_block1_T = np.mean(block1_totals_discr)
err_block1_T = sem(block1_totals_discr)

M_block2_T = np.mean(block2_totals_discr)
err_block2_T = sem(block2_totals_discr)

M_block3_T = np.mean(block3_totals_discr)
err_block3_T = sem(block3_totals_discr)

M_block4_T = np.mean(block4_totals_discr)
err_block4_T = sem(block4_totals_discr)

M_block5_T = np.mean(block5_totals_discr)
err_block5_T = sem(block5_totals_discr)

M_block6_T = np.mean(block6_totals_discr)
err_block6_T = sem(block6_totals_discr)

M_block7_T = np.mean(block7_totals_discr)
err_block7_T = sem(block7_totals_discr)

M_block8_T = np.mean(block8_totals_discr)
err_block8_T = sem(block8_totals_discr)



#####################################################################################################################################################



M_block1_A6 = np.mean(block1_A6_discr)
err_block1_A6 = sem(block1_A6_discr)

M_block2_A6 = np.mean(block2_A6_discr)
err_block2_A6 = sem(block2_A6_discr)

M_block3_A6 = np.mean(block3_A6_discr)
err_block3_A6 = sem(block3_A6_discr)

M_block4_A6 = np.mean(block4_A6_discr)
err_block4_A6 = sem(block4_A6_discr)

M_block5_A6 = np.mean(block5_A6_discr)
err_block5_A6 = sem(block5_A6_discr)

M_block6_A6 = np.mean(block6_A6_discr)
err_block6_A6 = sem(block6_A6_discr)

M_block7_A6 = np.mean(block7_A6_discr)
err_block7_A6 = sem(block7_A6_discr)

M_block8_A6 = np.mean(block8_A6_discr)
err_block8_A6 = sem(block8_A6_discr)

#######################################################################################################################################################################
#######################################################################################################################################################################
##########################################                GRAPH  NOW                  #####################################################################################
#########################################################################################################################################################################
##############################################################################################################################################################################


block_data = [1,2,3,4,5,6,7,8]

totals_data = [M_block1_T, M_block2_T, M_block3_T, M_block4_T, M_block5_T, M_block6_T, M_block7_T, M_block8_T]
totals_err = [err_block1_T, err_block2_T, err_block3_T, err_block4_T, err_block5_T, err_block6_T, err_block7_T,err_block8_T]

A6_data = [M_block1_A6, M_block2_A6, M_block3_A6, M_block4_A6, M_block5_A6, M_block6_A6, M_block7_A6, M_block8_A6]
A6_err = [err_block1_A6, err_block2_A6, err_block3_A6, err_block4_A6, err_block5_A6, err_block6_A6, err_block7_A6, err_block8_A6]





plt.errorbar(block_data, totals_data, yerr= totals_err, color = 'k', label = 'Overall Performance', marker= 'o', markersize= 10)
plt.errorbar(block_data, A6_data, yerr= A6_err, color= 'r', label = 'A6', marker= 's', markersize= 10)



plt.ylim(0.2,1.05)
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.65, top=0.85)
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xlabel("Training Block")
plt.ylabel("Proportioin Correct")
plt.title("Training Phase 1: \n Overall Versus Alpha 6 Performance (Discriminative)")
plt.savefig('C:/Users/apers/Downloads/GloblocData/SSL_Stats/discrTotals_vs_discrA6.png')







