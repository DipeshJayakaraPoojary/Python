import pandas as pd

df1 = pd.DataFrame({
        'id': [1,2,3,4],
        'name': ['Alex','Hailey','Lilly','John'],
        'age': [23,45,34,23]
})

df2 = pd.DataFrame({
        'id': [1,2,3,4],
        'name': ['Alex','Hailey','Lilly','John'],
        'marks': [23,45,34,23]        
})

print(df1.sort_values(by='age', ascending=False))
print(df2.sort_values(by='marks', ascending=False))


print(pd.merge(df1,df2, on='id'))