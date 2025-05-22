import pandas as pd

s = pd.Series([1,2,3,4,5,6,]) #Series

#DataFrame
df = pd.DataFrame({
    'id': [1,2,3,4],
    'name': ['Alex','Hailey','Lilly','John'],
    'age': [23,45,34,23]
})

print(s)
print(df)