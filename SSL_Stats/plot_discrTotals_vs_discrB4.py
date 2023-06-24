import pandas as pd
import scipy.stats as stats
import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt


total_means_discr = pd.read_csv("C:/Users/apers/Downloads/GloblocData/SSL_Stats/discr_Train1_PerSubj_total.csv")
B4_discr = pd.read_csv('C:/Users/apers/Downloads/GloblocData/SSL_Stats/discr_Train1_PerSubj_B4.csv')



block1_totals_discr = []
block2_totals_discr = []
block3_totals_discr = []
block4_totals_discr = []
block5_totals_discr = []
block6_totals_discr = []
block7_totals_discr = []
block8_totals_discr = []



block1_B4_discr = []
block2_B4_discr = []
block3_B4_discr = []
block4_B4_discr = []
block5_B4_discr = []
block6_B4_discr = []
block7_B4_discr = []
block8_B4_discr = []


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


#add all availabe data for block 1 B4 discr into the appropriate lists
for i, row in B4_discr.iterrows():
    if row.block_data == 1:
        block1_B4_discr.append(row.means)
#add all availabe data for block 2 B4 discr into the appropriate lists
for i, row in B4_discr.iterrows():
    if row.block_data == 2:
        block2_B4_discr.append(row.means)
#add all availabe data for block 3 B4 discr into the appropriate lists
for i, row in B4_discr.iterrows():
    if row.block_data == 3:
        block3_B4_discr.append(row.means)
#add all availabe data for block 4 B4 discr into the appropriate lists
for i, row in B4_discr.iterrows():
    if row.block_data == 4:
        block4_B4_discr.append(row.means)
#add all availabe data for block 5 B4 discr into the appropriate lists
for i, row in B4_discr.iterrows():
    if row.block_data == 5:
        block5_B4_discr.append(row.means)
#add all availabe data for block 6 B4 discr into the appropriate lists
for i, row in B4_discr.iterrows():
    if row.block_data == 6:
        block6_B4_discr.append(row.means)
#add all availabe data for block 7 B4 discr into the appropriate lists
for i, row in B4_discr.iterrows():
    if row.block_data == 7:
        block7_B4_discr.append(row.means)
#add all availabe data for block 8 B4 discr into the appropriate lists
for i, row in B4_discr.iterrows():
    if row.block_data == 8:
        block8_B4_discr.append(row.means)



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


#fix lists for discr B4
#block 1 discr B4
countB1B4 = 0
for i in block1_B4_discr:
    countB1B4 += 1
num_missingB1B4 = n_discr - countB1B4
print('this is block 1 discr B4 original:')
print(countB1B4)
print(num_missingB1B4)
while num_missingB1B4 != 0:
    block1_B4_discr.append(0.92)
    num_missingB1B4 -= 1


countB1B4 = 0
for i in block1_B4_discr:
    countB1B4 += 1
print('this is block 1 B4 totals fixed:')
print(countB1B4)
print(num_missingB1B4)








#block 2 discr B4
countB2B4 = 0
for i in block2_B4_discr:
    countB2B4 += 1
num_missingB2B4 = n_discr - countB2B4
print('this is block 2 discr B4 original:')
print(countB2B4)
print(num_missingB2B4)
while num_missingB2B4 != 0:
    block2_B4_discr.append(0.92)
    num_missingB2B4 -= 1


countB2B4 = 0
for i in block2_B4_discr:
    countB2B4 += 1
print('this is block 2 B4 totals fixed:')
print(countB2B4)
print(num_missingB2B4)







#block 3 discr B4
countB3B4 = 0
for i in block3_B4_discr:
    countB3B4 += 1

num_missingB3B4 = n_discr - countB3B4
print('this is block 3 discr B4 original:')
print(countB3B4)
print(num_missingB3B4)

while num_missingB3B4 != 0:
    block3_B4_discr.append(0.92)
    num_missingB3B4 -= 1


countB3B4 = 0
for i in block3_B4_discr:
    countB3B4 += 1
print('this is block 3 discr B4 fixed:')
print(countB3B4)
print(num_missingB3B4)







#block 4 discr B4
countB4B4 = 0
for i in block4_B4_discr:
    countB4B4 += 1

num_missingB4B4 = n_discr - countB4B4
print('this is block 4 discr B4 original:')
print(countB4B4)
print(num_missingB4B4)

while num_missingB4B4 != 0:
    block4_B4_discr.append(0.92)
    num_missingB4B4 -= 1


countB4B4 = 0
for i in block4_B4_discr:
    countB4B4 += 1
print('this is block 4 discr B4 fixed:')
print(countB4B4)
print(num_missingB4B4)







#block 5 discr B4
countB5B4 = 0
for i in block5_B4_discr:
    countB5B4 += 1

num_missingB5B4 = n_discr - countB5B4
print('this is block 5 discr B4 original:')
print(countB5B4)
print(num_missingB5B4)

while num_missingB5B4 != 0:
    block5_B4_discr.append(0.92)
    num_missingB5B4 -= 1


countB5B4 = 0
for i in block5_B4_discr:
    countB5B4 += 1
print('this is block 5 discr B4 fixed:')
print(countB5B4)
print(num_missingB5B4)








#block 6 discr B4
countB6B4 = 0
for i in block6_B4_discr:
    countB6B4 += 1

num_missingB6B4 = n_discr - countB6B4
print('this is block 6 discr B4 original:')
print(countB6B4)
print(num_missingB6B4)

while num_missingB6B4 != 0:
    block6_B4_discr.append(0.92)
    num_missingB6B4 -= 1


countB6B4 = 0
for i in block6_B4_discr:
    countB6B4 += 1
print('this is block 6 discr B4 fixed:')
print(countB6B4)
print(num_missingB6B4)










#block 7 discr B4
countB7B4 = 0
for i in block7_B4_discr:
    countB7B4 += 1

num_missingB7B4 = n_discr - countB7B4
print('this is block 7 discr B4 original:')
print(countB7B4)
print(num_missingB7B4)

while num_missingB7B4 != 0:
    block7_B4_discr.append(0.92)
    num_missingB7B4 -= 1


countB7B4 = 0
for i in block7_B4_discr:
    countB7B4 += 1
print('this is block 7 discr B4 fixed:')
print(countB7B4)
print(num_missingB7B4)











#block 8 discr B4
countB8B4 = 0
for i in block8_B4_discr:
    countB8B4 += 1

num_missingB8B4 = n_discr - countB8B4
print('this is block 8 discr B4 original:')
print(countB8B4)
print(num_missingB8B4)

while num_missingB8B4 != 0:
    block8_B4_discr.append(0.92)
    num_missingB8B4 -= 1


countB8B4 = 0
for i in block8_B4_discr:
    countB8B4 += 1
print('this is block 8 discr B4 fixed:')
print(countB8B4)
print(num_missingB8B4)


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



M_block1_B4 = np.mean(block1_B4_discr)
err_block1_B4 = sem(block1_B4_discr)

M_block2_B4 = np.mean(block2_B4_discr)
err_block2_B4 = sem(block2_B4_discr)

M_block3_B4 = np.mean(block3_B4_discr)
err_block3_B4 = sem(block3_B4_discr)

M_block4_B4 = np.mean(block4_B4_discr)
err_block4_B4 = sem(block4_B4_discr)

M_block5_B4 = np.mean(block5_B4_discr)
err_block5_B4 = sem(block5_B4_discr)

M_block6_B4 = np.mean(block6_B4_discr)
err_block6_B4 = sem(block6_B4_discr)

M_block7_B4 = np.mean(block7_B4_discr)
err_block7_B4 = sem(block7_B4_discr)

M_block8_B4 = np.mean(block8_B4_discr)
err_block8_B4 = sem(block8_B4_discr)

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
plt.title("Training Phase 1: \n Overall Versus Beta 4 Performance (Discriminative)")
plt.savefig('C:/Users/apers/Downloads/GloblocData/SSL_Stats/discrTotals_vs_discrB4.png')







