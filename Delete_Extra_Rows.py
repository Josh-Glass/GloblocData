import pandas as pd
from IPython.display import display

#loading in the data
df = pd.read_csv('C:/Users/apers/Downloads/GloblocData/combined_csv.csv')
display(df.head(20))
#this makes a new data frame keeping everything that is not equal to pnum
newdf = df[df['pnum'] != 'pnum']

newdf.to_csv( "C:/Users/apers/Downloads/GloblocData/CombinedMinusRows_1.csv", index=False, encoding='utf-8-sig')
