import pandas as pd


df1 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/discriminative_data.csv')
df2 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/generative_data.csv')

#get discriminative training phase 1 means
df1 = df1.drop(index = df1[df1['phase_id'] == 'training_phase_1'].index)
df1 = df1.drop(index = df1[df1['phase_id']== 'training_phase_2'].index)

means_df1 = df1.groupby(['stim', 'pnum'], as_index= True)['response'].describe()

print(means_df1)

means_df1.to_csv( "C:/Users/apers/Downloads/GloblocData/Generalization/discr_TestPhase_means_PerSub.csv", index=True, encoding='utf-8-sig')


df2 = df2.drop(index = df2[df2['phase_id'] == 'training_phase_1'].index)
df2 = df2.drop(index = df2[df2['phase_id']== 'training_phase_2'].index)

means_df2 = df2.groupby(['stim', 'pnum'], as_index= True)['response'].describe()

print(means_df2)
means_df2.to_csv( "C:/Users/apers/Downloads/GloblocData/Generalization/gener_TestPhase_means_PerSub.csv", index=True, encoding='utf-8-sig')


