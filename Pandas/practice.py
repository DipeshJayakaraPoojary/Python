import pandas as pd

df1 = pd.DataFrame({
    'id': [1,2,3],
    'name': ['Priya','Alex','Rob'],
    'age': [16,16,17]
})

df2 = pd.DataFrame({
    'id': [1,2,3],
    'name': ['Priya','Alex','Rob'],
    'marks': [29,30,38]
})

sort = df1.sort_values(by='age', ascending=True)
print(sort)

print("Merge")
merge = pd.merge(df1,df2, on='id')
print(merge)

print("Concatination")
cont = pd.concat([df1,df2], axis=0)
print(cont)