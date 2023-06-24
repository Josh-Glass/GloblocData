import pandas as pd
#get hit descriuptives per stim for trainining phase 1


df1 = pd.read_csv('discriminative_data.csv')
df2 = pd.read_csv('generative_data.csv')

#get discriminative training phase 1 means
df1 = df1.drop(index = df1[df1['phase_id'] == 'test_phase'].index)
df1 = df1.drop(index = df1[df1['phase_id']== 'training_phase_2'].index)

means_df1 = df1.groupby(['block_data', 'stim'], as_index= True)['hit'].describe()

print(means_df1)

means_df1.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_PerStim_Descriptives.csv", index=True, encoding='utf-8-sig')

#get generative training phase 1 means
df2 = df2.drop(index = df2[df2['phase_id'] == 'test_phase'].index)
df2 = df2.drop(index = df2[df2['phase_id']== 'training_phase_2'].index)

means_df2 = df2.groupby(['block_data', 'stim'], as_index= True)['hit'].describe()

print(means_df2)
means_df2.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_PerStim_Descriptives.csv", index=True, encoding='utf-8-sig')













