import pandas as pd
import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#df = df.drop(index = df[df['phase_id'] == 'test_phase'].index)
#df = df.drop(index = df[df['phase_id'] == 'training_phase_2'].index)


def  individual_learn_curves(path, stim1, stim2):
    count= 1
    for file in os.listdir(path):
            if file.endswith('.csv'):
                input = pd.read_csv(str(path)+'/'+file)
                df = input[input['pnum'] != 'pnum']
                newdf = df.drop(index = df[df['phase_id'] != 'training_phase_1'].index)



                #print(np.array(df['pnum'].unique())[0],np.array(df['condition'].unique())[0],count)
                #count +=1
                condition = str(np.array(newdf['condition'].unique())[0])
                #print(condition)
                if condition == '1':
                    

                    met_crit = np.array(newdf['met_criterian'])
                    met_crit[met_crit=='False']= 0
                    met_crit[met_crit=='True']= 1
                    hit = np.array(newdf['hit'])
                    hit[hit=='False']= 0
                    hit[hit=='True']= 1

                    if np.sum(met_crit) >0:
                        
                        newdf['hit'] = newdf['hit'].astype(str)
                        newdf = newdf.replace('True', 1)
                        newdf = newdf.replace('False', 0)
                        stim1df = newdf.drop(index = newdf[newdf['stim'] != str(stim1)].index)
                        stim2df = newdf.drop(index = newdf[newdf['stim'] != str(stim2)].index)
                        stim3df = newdf.drop(index = newdf[newdf['stim'] != 'materials/images/blueB1.png'].index)
                        stim4df = newdf.drop(index = newdf[newdf['stim'] != 'materials/images/blueB2.png'].index)
                        stim5df = newdf.drop(index = newdf[newdf['stim'] != 'materials/images/blueB3.png'].index)
                        stim6df = newdf.drop(index = newdf[newdf['stim'] != 'materials/images/blueB5.png'].index)
                        stim7df = newdf.drop(index = newdf[newdf['stim'] != 'materials/images/blueB6.png'].index)
                        stim8df = newdf.drop(index = newdf[newdf['stim'] != 'materials/images/redA1.png'].index)
                        stim9df = newdf.drop(index = newdf[newdf['stim'] != 'materials/images/redA2.png'].index)
                        stim10df = newdf.drop(index = newdf[newdf['stim'] != 'materials/images/redA3.png'].index)
                        stim11df = newdf.drop(index = newdf[newdf['stim'] != 'materials/images/redA4.png'].index)
                        stim12df = newdf.drop(index = newdf[newdf['stim'] != 'materials/images/redA5.png'].index)













                        group1= stim1df.groupby(['block_data'], as_index= True)['hit'].describe()
                        group2= stim2df.groupby(['block_data'], as_index= True)['hit'].describe()
                        group3= stim3df.groupby(['block_data'], as_index= True)['hit'].describe()
                        group4= stim4df.groupby(['block_data'], as_index= True)['hit'].describe()
                        group5= stim5df.groupby(['block_data'], as_index= True)['hit'].describe()
                        group6= stim6df.groupby(['block_data'], as_index= True)['hit'].describe()
                        group7= stim7df.groupby(['block_data'], as_index= True)['hit'].describe()
                        group8= stim8df.groupby(['block_data'], as_index= True)['hit'].describe()
                        group9= stim9df.groupby(['block_data'], as_index= True)['hit'].describe()
                        group10= stim10df.groupby(['block_data'], as_index= True)['hit'].describe()
                        group11= stim11df.groupby(['block_data'], as_index= True)['hit'].describe()
                        group12= stim12df.groupby(['block_data'], as_index= True)['hit'].describe()



                        group1.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        group2.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        group3.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        group4.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        group5.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        group6.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        group7.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        group8.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        group9.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        group10.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        group11.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        group12.rename(columns = {'mean':'means', 'std':'stndDev'}, inplace = True)
                        
                        means1 = np.array(group1['means'])
                        means2 = np.array(group2['means'])
                        means3 = np.array(group3['means'])
                        means4 = np.array(group4['means'])
                        means5 = np.array(group5['means'])
                        means6 = np.array(group6['means'])
                        means7 = np.array(group7['means'])
                        means8 = np.array(group8['means'])
                        means9 = np.array(group9['means'])
                        means10 = np.array(group10['means'])
                        means11 = np.array(group11['means'])
                        means12 = np.array(group12['means'])
                        

                        blocks1 = np.array(group1['means'].index)
                        blocks2 = np.array(group2['means'].index)
                        blocks3 = np.array(group3['means'].index)
                        blocks4 = np.array(group4['means'].index)
                        blocks5 = np.array(group5['means'].index)
                        blocks6 = np.array(group6['means'].index)
                        blocks7 = np.array(group7['means'].index)
                        blocks8 = np.array(group8['means'].index)
                        blocks9 = np.array(group9['means'].index)
                        blocks10 = np.array(group10['means'].index)
                        blocks11 = np.array(group11['means'].index)
                        blocks12 = np.array(group12['means'].index)
                        

                        plt.errorbar(blocks1, means1, color = 'r', marker= 'o', markersize= 10, label='A6')
                        plt.errorbar(blocks2, means2, color = 'b', marker= '*', markersize= 10,label= 'B4')
                       # plt.errorbar(blocks3, means3, color = 'k',alpha=0.1, linestyle='dashed', linewidth=3, markersize= 10)
                       # plt.errorbar(blocks4, means4, color = 'k',alpha=0.1, linestyle='dashed', linewidth=3, markersize= 10)
                       # plt.errorbar(blocks5, means5, color = 'k',alpha=0.1, linestyle='dashed', linewidth=3, markersize= 10)
                        #plt.errorbar(blocks6, means6, color = 'k',alpha=0.1, linestyle='dashed', linewidth=3, markersize= 10)
                        #plt.errorbar(blocks7, means7, color = 'k',alpha=0.1, linestyle='dashed', linewidth=3, markersize= 10)
                        plt.errorbar(blocks8, means8, color = 'k',alpha=0.5, linestyle='dashed', linewidth=5, markersize= 10,label='A1')
                        #plt.errorbar(blocks9, means9, color = 'k',alpha=0.1, linestyle='dashed', linewidth=3, markersize= 10)
                       # plt.errorbar(blocks10, means10, color = 'k',alpha=0.1, linestyle='dashed', linewidth=3, markersize= 10)
                        #plt.errorbar(blocks11, means11, color = 'k',alpha=0.1, linestyle='dashed', linewidth=3, markersize= 10)
                        #plt.errorbar(blocks12, means12, color = 'k',alpha=0.1,linestyle='dashed', linewidth=3, markersize= 10)

                        xlabels = blocks1
                        ylabels= [0,1]
                        pnum = np.array(newdf['pnum'].unique())[0]
                        plt.legend()
                        plt.yticks(ylabels)
                        plt.xticks(xlabels)
                        plt.xlabel("Training Block")
                        plt.ylabel("correct or incorrect")
                        plt.title(str(pnum))
                        plt.savefig('C:/Users/apers/Downloads/GloblocData/perSubject/subject_learn_curves/'+str(pnum) + '.png')
                        plt.clf()

                        



                        
                    
                    
                     
                     



path = 'C:/Users/apers/Downloads/GloblocData/raw_data'
stim1= 'materials/images/redA6.png'
stim2= 'materials/images/blueB4.png'

#individual_learn_curves(path=path,stim1 = stim1, stim2=stim2)


def compare_last_block_and_test(path, stim, cond,title):
    
    trainhits= []
    testhits=[]
    count = 0
    for file in os.listdir(path):
        if file.endswith('.csv'):
            input = pd.read_csv(str(path)+'/'+file)
            df = input[input['pnum'] != 'pnum']
                

            df = df.replace('True', 1)
            df = df.replace('False', 0)
            traindf = df.drop(index = df[df['phase_id'] != 'training_phase_1'].index)
            testdf = df.drop(index = df[df['phase_id'] != 'test_phase'].index)

            if np.sum(traindf['met_criterian']) > 0 and traindf['condition'].unique()==cond:
                count+=1
                traindf.drop(index = traindf[traindf['stim'] != str(stim)].index, inplace=True)
                testdf.drop(index = testdf[testdf['stim'] != str(stim)].index, inplace=True)


                trainhits.append(np.array(traindf['hit'])[-1])
                
                
                for item in testdf['response']:
                    if item == testdf['correct_category'].unique():
                        testhits.append(1)
                    else:
                        testhits.append(0)

                




                
    #print(np.mean(trainhits))
    #print(np.mean(testhits))
    n=len(trainhits)
    righttrain = np.sum(trainhits)
    print(righttrain, 'right train')
    righttest=np.sum(testhits)
    print(righttest, 'right test')
    wrongtrain =(n-np.sum(trainhits))
    print(wrongtrain, 'wrong train')
    wrongtest =(n-np.sum(testhits))
    print(wrongtest, 'wrong test')
    table = np.array([[righttrain, wrongtrain], [righttest, wrongtest]])
    print(stats.fisher_exact(table, alternative='greater'))                
    print(count) 
    data = [np.mean(trainhits),np.mean(testhits)]
    sem = [stats.sem(trainhits), stats.sem(testhits)]
    xlabels= ['last block at train', 'test']
    xpos= np.arange(len(xlabels))
    plt.ylabel('proportion of subjects who answered correctly')
    plt.title(str(title))

    plt.bar(xlabels[0], height=data[0], yerr= sem[0], edgecolor='k', color='white', capsize=8, hatch= '//')
    plt.bar(xlabels[1], height=data[1], yerr= sem[1], edgecolor='k', color='white', capsize=8, hatch= 'oo')

    #plt.xticks(xlabels[xpos])
    plt.savefig('perSubject/graphs_compare_lastblock_test/'+ str(title) +'.png')
    plt.clf()
    print('...')
            #break



cond='2'

Aconds = {
    '1': 'item A6 (discriminative)',
    '2': 'item A6 (generative)'
}

Bconds = {
    '1': 'item B4 (discriminative)',
    '2': 'item B4 (generative)'
}

for key in Aconds:
    print(Aconds[key])
    compare_last_block_and_test(path=path,stim=stim1, cond=key, title=Aconds[key])

for key in Bconds:
    print(Bconds[key])
    compare_last_block_and_test(path=path,stim=stim2, cond=key, title=Bconds[key])