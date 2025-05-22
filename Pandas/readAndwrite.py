import pandas as pd

df = pd.read_excel('output.xlsx', sheet_name='Sheet1')

'''# Display the first few rows of the DataFrame
print(df.head())
# Display the all column names
print(df.columns)
# Display the last few rows of the DataFrame
print(df.tail())
# Display the shape of the DataFrame
print(df.info())
# Display the description of the DataFrame
print(df.describe())'''

'''
#Accessing columns
print(df['product'])

#Accessing multiple columns
print(df[['product','unitsofvolume','lotsize']])

#First row by index
print(df.iloc[10])

#For first 5 rows in index
print(df.loc[0:5])  '''

print(df['tradedvolume']>500)