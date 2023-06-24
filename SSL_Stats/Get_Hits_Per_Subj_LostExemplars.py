import pandas as pd
#get hit descriuptives per stim for trainining phase 1


df1 = pd.read_csv('discriminative_data.csv')
df2 = pd.read_csv('generative_data.csv')

#get discriminative training phase 1 means for A6
df1_A6 = df1.drop(index = df1[df1['phase_id'] == 'test_phase'].index)
df1_A6 = df1_A6.drop(index = df1_A6[df1_A6['phase_id']== 'training_phase_2'].index)
df1_A6 = df1_A6.drop(index = df1_A6[df1_A6['stim'] != 'materials/images/redA6.png'].index)

means_df1_A6 = df1_A6.groupby(['block_data', 'pnum'], as_index= True)['hit'].describe()

print(means_df1_A6)

means_df1_A6.to_csv( "C:/Users/apers/Downloads/GloblocData/SSL_Stats/discr_Train1_PerSubj_A6.csv", index=True, encoding='utf-8-sig')

#get discriminative training phase 1 means for B4
df1_B4 = df1.drop(index = df1[df1['phase_id'] == 'test_phase'].index)
df1_B4 = df1_B4.drop(index = df1_B4[df1_B4['phase_id']== 'training_phase_2'].index)
df1_B4 = df1_B4.drop(index = df1_B4[df1_B4['stim'] != 'materials/images/blueB4.png'].index)

means_df1_B4 = df1_B4.groupby(['block_data', 'pnum'], as_index= True)['hit'].describe()

print(means_df1_B4)

means_df1_B4.to_csv( "C:/Users/apers/Downloads/GloblocData/SSL_Stats/discr_Train1_PerSubj_B4.csv", index=True, encoding='utf-8-sig')




#get generative training phase 1 means for A6
df2_A6 = df2.drop(index = df2[df2['phase_id'] == 'test_phase'].index)
df2_A6 = df2_A6.drop(index = df2_A6[df2_A6['phase_id']== 'training_phase_2'].index)
df2_A6 = df2_A6.drop(index = df2_A6[df2_A6['stim'] != 'materials/images/redA6.png'].index)

means_df2_A6 = df2_A6.groupby(['block_data', 'pnum'], as_index= True)['hit'].describe()

print(means_df2_A6)
means_df2_A6.to_csv( "C:/Users/apers/Downloads/GloblocData/SSL_Stats/gener_Train1_PerSubj_A6.csv", index=True, encoding='utf-8-sig')


#get generative training phase 1 means for B4
df2_B4 = df2.drop(index = df2[df2['phase_id'] == 'test_phase'].index)
df2_B4 = df2_B4.drop(index = df2_B4[df2_B4['phase_id']== 'training_phase_2'].index)
df2_B4 = df2_B4.drop(index = df2_B4[df2_B4['stim'] != 'materials/images/blueB4.png'].index)

means_df2_B4 = df2_B4.groupby(['block_data', 'pnum'], as_index= True)['hit'].describe()

print(means_df2_B4)
means_df2_B4.to_csv( "C:/Users/apers/Downloads/GloblocData/SSL_Stats/gener_Train1_PerSubj_B4.csv", index=True, encoding='utf-8-sig')












