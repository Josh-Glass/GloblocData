import pandas as pd
 
df = pd.read_csv('metCritpnums.csv')

stim_ygen = {
    'materials/images/yGen1.png': 'test_1',
    'materials/images/yGen2.png': 'test_2',
    'materials/images/yGen3.png': 'test_3',
    'materials/images/yGen4.png': 'test_4',
    'materials/images/yGen5.png': 'test_5',
}

newdf = pd.DataFrame({
    'pnum':[],
    'num2crit':[],
    'condition':[],
    'test_1':[],
    'test_2':[],
    'test_3':[],
    'test_4':[],
    'test_5':[],
    'alpha_p2b1': [],
    'beta_p2b1':[],
    'gamma_p2b1':[],
    'delta_p2b1':[],
    'alpha_p2b2':[],
    'beta_p2b2':[],
    'gamma_p2b2':[],
    'delta_p2b2':[],
})

for i, row in df.iterrows():
    if row.phase_id == 'training_phase_1':
        # Check if pnum exists in new dataframe
        if(row.pnum in newdf.pnum.values):
            index = newdf[newdf.pnum == row.pnum].index[0]
            newdf.at[index, 'num2crit'] = row.block_data
        else:
            new_index = len(newdf.index)+1
            newdf.loc[new_index] = [row.pnum, row.block_data, row.condition, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    elif row.phase_id == 'test_phase':
        if row.stim in stim_ygen:
            index = newdf[newdf.pnum == row.pnum].index[0]
            if row.response == 'Alpha':
                newdf.at[index, stim_ygen[row.stim]] = 0
            else:
                newdf.at[index, stim_ygen[row.stim]] = 1
            

    elif row.phase_id == 'training_phase_2':
        response = row.response
        block = row.block_data
        
        col = str(response).lower()+'_p2b'+str(block)
        index = newdf[newdf.pnum == row.pnum].index[0]
        if row.correct_category == row.response:
            newdf.at[index, col] += 1

    

newdf.to_csv('output.csv', index=False, encoding='utf-8-sig')