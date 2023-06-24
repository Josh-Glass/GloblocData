import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

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


data_g = np.array([

   [.78,.14], # C
   [.9,.06], # C
   [.94,.18], # C

   [.04,.44], # C
   [.06,.62], # C
   [.18,.58], # C


])


data_d = np.array([

   [.26, 1], # D
   [.34, 1], # D
   [.42, 1], # D

   [.5, 1], # D
   [.58, 1], # D
   [.66, 1], # D
])


df = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Generalization/gener_TestPhase_means.csv')


average_Ax = np.mean(data_a[:,0])
average_Ay = np.mean(data_a[:,1])

average_Bx = np.mean(data_b[:,0])
average_By = np.mean(data_b[:,1])



plt.scatter(data_a[:,0],data_a[:,1], c= 'w', s= 300, edgecolor= 'red', linewidths=3, marker= 'o', label= (r'$\alpha$'))
plt.scatter(data_b[:,0],data_b[:,1],c = 'w', s= 300, edgecolor= 'blue', linewidths=3, marker = 'o', label= (r'$\beta$'))
plt.scatter(data_t[:,0],data_t[:,1], c = 'w', s= 300, edgecolor= 'y', linewidths=3, marker = 'o', label = ('test'))
plt.scatter(data_all[:,0],data_all[:,1],cmap= 'bwr', c= df['mean'], s= 100, edgecolor= 'k', marker= 'o')
#plt.scatter(average_Ax,average_Ay, c= 'darkred', s= 300, edgecolor= 'k', marker= '*', label= "Alpha prototype")
#plt.scatter(average_Bx,average_By, c= 'darkblue', s= 300, edgecolor= 'k', marker= '*', label= "Beta prototype")


plt.legend(loc="upper right")
plt.colorbar(shrink=0.5, aspect=8, label='Proportion ' + (r'$\alpha$') + ' Response')

plt.xlabel("Shading")
plt.ylabel("Size")
plt.title("Generative: Average Generalization Response")
plt.savefig('C:/Users/apers/Downloads/GloblocData/Generalization/Gen_Plot_generative.png')