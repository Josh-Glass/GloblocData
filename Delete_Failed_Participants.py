import pandas as pd
from IPython.display import display
from csv import writer

df = pd.read_csv('CombinedMinusRows_1.csv')
#display(df.head(5))
failed_pnums = []
for item in df.groupby(['pnum','phase_id']):
    if item[0][1] == 'training_phase_1':
       
        if item[1].sum()['met_criterian'] == 0 and item[0][0] not in failed_pnums:
            failed_pnums.append(item[0][0])


            #df = df[df['pnum'] != item[1]['pnum']]
            
print(failed_pnums)


for item in failed_pnums:
    #if df[item]['pnum'] in failed_pnums:
    df = df.drop(index = df[df['pnum'] == item].index)
    #print(df[df['pnum'] == item].index)

print(df)


df.to_csv( "C:/Users/apers/Downloads/GloblocData/metCritpnums.csv", index=False, encoding='utf-8-sig')
        





