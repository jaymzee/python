import pandas as pd

age = [
    ['Aman', 95.5, "Male"],
    ['Sunny', 65.7, "Female"],
    ['Monty', 85.1, "Male"],
    ['toni', 75.4, "Male"]
]

df = pd.DataFrame(age, columns=['Name', 'Marks', 'Gender'])

print(df)
