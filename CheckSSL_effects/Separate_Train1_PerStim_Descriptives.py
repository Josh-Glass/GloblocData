import pandas as pd


means_df1 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_PerStim_Descriptives.csv")
means_df2 = pd.read_csv("C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_PerStim_Descriptives.csv")


#get just blueB1 for discriminative data
means_blueB1 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/blueB1.png'].index)
means_blueB1.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB1_Descriptives.csv", index=False, encoding='utf-8-sig')


#get just blueB2 for discriminative data
means_blueB2 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/blueB2.png'].index)
means_blueB2.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB2_Descriptives.csv", index=False, encoding='utf-8-sig')


#get just  blueB3 for discriminative data
means_blueB3 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/blueB3.png'].index)
means_blueB3.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB3_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just blueB4 for discriminative data
means_blueB4 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/blueB4.png'].index)
means_blueB4.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB4_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just blueB5 for discriminative data
means_blueB5 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/blueB5.png'].index)
means_blueB5.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB5_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just blueB6 for discriminative data
means_blueB6 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/blueB6.png'].index)
means_blueB6.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_blueB6_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA1 for discriminative data
means_redA1 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/redA1.png'].index)
means_redA1.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA1_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA2 for discriminative data
means_redA2 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/redA2.png'].index)
means_redA2.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA2_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA3 for discriminative data
means_redA3 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/redA3.png'].index)
means_redA3.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA3_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA4 for discriminative data
means_redA4 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/redA4.png'].index)
means_redA4.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA4_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA5 for discriminative data
means_redA5 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/redA5.png'].index)
means_redA5.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA5_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA6 for discriminative data
means_redA6 = means_df1.drop(index = means_df1[means_df1['stim'] != 'materials/images/redA6.png'].index)
means_redA6.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/discr_Train1_redA6_Descriptives.csv", index=False, encoding='utf-8-sig')

#- - - - -  -- - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#--- - - - - - - - - - - - - - - - --  - - - - - - - - - -- - - - - - - - - - - - -  - - -- - - - - - - - - - - - -  - - -- - - - -- - - - -  -- - -- - - - - -- - - - - -- - --
##################################################################################################################################################################################
##################################################################################################################################################################################
#- - - - -  -- - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#--- - - - - - - - - - - - - - - - --  - - - - - - - - - -- - - - - - - - - - - - -  - - -- - - - - - - - - - - - -  - - -- - - - -- - - - -  -- - -- - - - - -- - - - - -- - --
#FOR GENERATIVE DATA NOW

#get just blueB1 for discriminative data
Gmeans_blueB1 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/blueB1.png'].index)
Gmeans_blueB1.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_blueB1_Descriptives.csv", index=False, encoding='utf-8-sig')


#get just blueB2 for discriminative data
Gmeans_blueB2 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/blueB2.png'].index)
Gmeans_blueB2.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_blueB2_Descriptives.csv", index=False, encoding='utf-8-sig')


#get just  blueB3 for discriminative data
Gmeans_blueB3 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/blueB3.png'].index)
Gmeans_blueB3.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_blueB3_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just blueB4 for discriminative data
Gmeans_blueB4 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/blueB4.png'].index)
Gmeans_blueB4.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_blueB4_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just blueB5 for discriminative data
Gmeans_blueB5 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/blueB5.png'].index)
Gmeans_blueB5.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_blueB5_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just blueB6 for discriminative data
Gmeans_blueB6 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/blueB6.png'].index)
Gmeans_blueB6.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_blueB6_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA1 for discriminative data
Gmeans_redA1 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/redA1.png'].index)
Gmeans_redA1.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_redA1_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA2 for discriminative data
Gmeans_redA2 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/redA2.png'].index)
Gmeans_redA2.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_redA2_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA3 for discriminative data
Gmeans_redA3 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/redA3.png'].index)
Gmeans_redA3.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_redA3_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA4 for discriminative data
Gmeans_redA4 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/redA4.png'].index)
Gmeans_redA4.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_redA4_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA5 for discriminative data
Gmeans_redA5 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/redA5.png'].index)
Gmeans_redA5.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_redA5_Descriptives.csv", index=False, encoding='utf-8-sig')

#get just redA6 for discriminative data
Gmeans_redA6 = means_df2.drop(index = means_df2[means_df2['stim'] != 'materials/images/redA6.png'].index)
Gmeans_redA6.to_csv( "C:/Users/apers/Downloads/GloblocData/CheckSSL_effects/gener_Train1_redA6_Descriptives.csv", index=False, encoding='utf-8-sig')

