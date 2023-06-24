import pandas as pd


means_df1 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Train2/discr_phase2_means_PER_CAT.csv')
means_df2 = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Train2/gener_phase2_means_PER_CAT.csv')


#get just ALPHAS for discriminative data
means_alphas = means_df1.drop(index = means_df1[means_df1['correct_category'] == 'Beta'].index)
means_alphas = means_alphas.drop(index = means_alphas[means_alphas['correct_category'] == 'Gamma'].index)
means_alphas = means_alphas.drop(index = means_alphas[means_alphas['correct_category'] == 'Delta'].index)
means_alphas.to_csv( "C:/Users/apers/Downloads/GloblocData/Train2/discr_phase2_ALPHA_means.csv", index=False, encoding='utf-8-sig')
#get just BETAS for discriminative data
means_betas = means_df1.drop(index = means_df1[means_df1['correct_category'] == 'Alpha'].index)
means_betas = means_betas.drop(index = means_betas[means_betas['correct_category'] == 'Gamma'].index)
means_betas = means_betas.drop(index = means_betas[means_betas['correct_category'] == 'Delta'].index)
means_betas.to_csv( "C:/Users/apers/Downloads/GloblocData/Train2/discr_phase2_BETA_means.csv", index=False, encoding='utf-8-sig')
#get just GAMMAS for discriminative data
means_gammas = means_df1.drop(index = means_df1[means_df1['correct_category'] == 'Alpha'].index)
means_gammas = means_gammas.drop(index = means_gammas[means_gammas['correct_category'] == 'Beta'].index)
means_gammas = means_gammas.drop(index = means_gammas[means_gammas['correct_category'] == 'Delta'].index)
means_gammas.to_csv( "C:/Users/apers/Downloads/GloblocData/Train2/discr_phase2_GAMMA_means.csv", index=False, encoding='utf-8-sig')
#get just DELTAS for discriminative data
means_deltas = means_df1.drop(index = means_df1[means_df1['correct_category'] == 'Alpha'].index)
means_deltas = means_deltas.drop(index = means_deltas[means_deltas['correct_category'] == 'Beta'].index)
means_deltas = means_deltas.drop(index = means_deltas[means_deltas['correct_category'] == 'Gamma'].index)
means_deltas.to_csv( "C:/Users/apers/Downloads/GloblocData/Train2/discr_phase2_DELTA_means.csv", index=False, encoding='utf-8-sig')

#get just ALPHAS for generative data
means_alphas2 = means_df2.drop(index = means_df2[means_df2['correct_category'] == 'Beta'].index)
means_alphas2 = means_alphas2.drop(index = means_alphas2[means_alphas2['correct_category'] == 'Gamma'].index)
means_alphas2 = means_alphas2.drop(index = means_alphas2[means_alphas2['correct_category'] == 'Delta'].index)
means_alphas2.to_csv( "C:/Users/apers/Downloads/GloblocData/Train2/gener_phase2_ALPHA_means.csv", index=False, encoding='utf-8-sig')
#get just BETAS for discriminative data
means_betas2 = means_df2.drop(index = means_df2[means_df2['correct_category'] == 'Alpha'].index)
means_betas2 = means_betas2.drop(index = means_betas2[means_betas2['correct_category'] == 'Gamma'].index)
means_betas2 = means_betas2.drop(index = means_betas2[means_betas2['correct_category'] == 'Delta'].index)
means_betas2.to_csv( "C:/Users/apers/Downloads/GloblocData/Train2/gener_phase2_BETA_means.csv", index=False, encoding='utf-8-sig')
#get just GAMMAS for discriminative data
means_gammas2 = means_df2.drop(index = means_df2[means_df2['correct_category'] == 'Alpha'].index)
means_gammas2 = means_gammas2.drop(index = means_gammas2[means_gammas2['correct_category'] == 'Beta'].index)
means_gammas2 = means_gammas2.drop(index = means_gammas2[means_gammas2['correct_category'] == 'Delta'].index)
means_gammas2.to_csv( "C:/Users/apers/Downloads/GloblocData/Train2/gener_phase2_GAMMA_means.csv", index=False, encoding='utf-8-sig')
#get just DELTAS for discriminative data
means_deltas2 = means_df2.drop(index = means_df2[means_df2['correct_category'] == 'Alpha'].index)
means_deltas2 = means_deltas2.drop(index = means_deltas2[means_deltas2['correct_category'] == 'Beta'].index)
means_deltas2 = means_deltas2.drop(index = means_deltas2[means_deltas2['correct_category'] == 'Gamma'].index)
means_deltas2.to_csv( "C:/Users/apers/Downloads/GloblocData/Train2/gener_phase2_DELTA_means.csv", index=False, encoding='utf-8-sig')