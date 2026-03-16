import pandas as pd
import numpy as np
df = pd.read_csv('data/spam.csv',index_col='Unnamed: 0')
df.rename(columns={'Unnamed: 0':'Respondent','spamORham':'Spam'}, inplace=True)
df['Spam'] = df['Spam'].replace({'ham': 0, 'spam': 1})
df.index.name = "Respondent"
#print(df.head(10))
#print(df['Spam'].value_counts())
#print(df['Message'].value_counts())
df2 = df.groupby(by = 'Message')
print(df2['Spam'].value_counts().sort_values(ascending=False))
df = df.drop_duplicates({'Spam','Message'})
print(df)
filt =((df['Message'] == np.nan) |(df['Message']=='NA') | (df['Message']==''))
print(df[filt])
df['length'] = df['Message'].apply(lambda x: len(x))
df['num words'] = df['Message'].apply(lambda x: len(x.split()))
df3 = df.groupby(by ='Spam')
print(df3.agg({'length':'median','num words':'median'}))
print(df)   
df.to_csv('data/modified.csv')  
print(df.shape) 
print(df['Spam'].value_counts())

