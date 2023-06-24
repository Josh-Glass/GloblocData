import numpy as np 
import matplotlib.pyplot as plt


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

    [.12, .28], # generalzation test items
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






preds = ['r', 'b', 'r', 'r', 'b']


plt.scatter(data_a[:,0],data_a[:,1], c= 'r', s= 150, edgecolor= 'r', marker= (r'$\alpha$'))
plt.scatter(data_b[:,0],data_b[:,1], c= 'b', s= 150,edgecolor= 'b', marker = (r'$\beta$'))
plt.scatter(data_t[:,0],data_t[:,1], c= preds, s= 150, edgecolor= preds, marker = ('$T$'))
plt.xlabel("Shading")
plt.ylabel("Size")
plt.title("Predicted Generalizations: Global Coherence")
plt.savefig('Global_Preds.png')