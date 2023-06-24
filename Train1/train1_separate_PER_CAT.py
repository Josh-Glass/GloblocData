import pandas as pd


means_df1 = pd.read_csv('discr_phase1_means_PER_CAT.csv')
means_df2 = pd.read_csv('gener_phase1_means_PER_CAT.csv')


#get just ALPHAS for discriminative data
means_alphas = means_df1.drop(index = means_df1[means_df1['correct_category'] == 'Beta'].index)
means_alphas.to_csv( "C:/Users/apers/Downloads/GloblocData/discr_phase1_ALPHA_means.csv", index=False, encoding='utf-8-sig')
#get just BETAS for discriminative data
means_betas = means_df1.drop(index = means_df1[means_df1['correct_category'] == 'Alpha'].index)
means_betas.to_csv( "C:/Users/apers/Downloads/GloblocData/discr_phase1_BETA_means.csv", index=False, encoding='utf-8-sig')


#get just ALPHAS for generative data
means_alphas2 = means_df2.drop(index = means_df2[means_df2['correct_category'] == 'Beta'].index)
means_alphas2.to_csv( "C:/Users/apers/Downloads/GloblocData/gener_phase1_ALPHA_means.csv", index=False, encoding='utf-8-sig')
#get just BETAS for discriminative data
means_betas2 = means_df2.drop(index = means_df2[means_df2['correct_category'] == 'Alpha'].index)
means_betas2.to_csv( "C:/Users/apers/Downloads/GloblocData/gener_phase1_BETA_means.csv", index=False, encoding='utf-8-sig')

