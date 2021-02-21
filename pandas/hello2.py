import pandas as pd

df = pd.read_csv('foo', sep=':')

print(df)
print(df['Feb'])
print(df[['Jan']])
