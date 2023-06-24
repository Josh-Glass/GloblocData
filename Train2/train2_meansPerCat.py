import pandas as pd



df1 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/discriminative_data.csv')
df2 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/generative_data.csv')

#get discriminative training phase 2 means
df1 = df1.drop(index = df1[df1['phase_id'] == 'test_phase'].index)
df1 = df1.drop(index = df1[df1['phase_id']== 'training_phase_1'].index)

means_df1 = df1.groupby(['block_data', 'correct_category'], as_index= True)['hit'].describe()

print(means_df1)

means_df1.to_csv( "C:/Users/apers/Downloads/GloblocData/Train2/discr_phase2_means_PER_CAT.csv", index=True, encoding='utf-8-sig')

#get generative training phase 2 means
df2 = df2.drop(index = df2[df2['phase_id'] == 'test_phase'].index)
df2 = df2.drop(index = df2[df2['phase_id']== 'training_phase_1'].index)

means_df2 = df2.groupby(['block_data', 'correct_category'], as_index= True)['hit'].describe()

print(means_df2)
means_df2.to_csv( "C:/Users/apers/Downloads/GloblocData/Train2/gener_phase2_means_PER_CAT.csv", index=True, encoding='utf-8-sig')













