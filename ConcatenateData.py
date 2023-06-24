import os
import pandas as pd 
import glob

os.chdir('C:/Users/apers/Downloads/GloblocData/raw_data')

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "C:/Users/apers/Downloads/GloblocData/combined_csv.csv", index=False, encoding='utf-8-sig')


#data = pd.concat([
#    os.path.join('C:/Users/apers/Downloads/GloblocData_11006to11075', file)
#    for file in os.listdir('C:/Users/apers/Downloads/GloblocData_11006to11075') if file.endswith('.csv')
#])



#sumvalues = data.groupby('subject id').sum()['column you want'] # <-- assuming you have some column called "subject id", which you should
