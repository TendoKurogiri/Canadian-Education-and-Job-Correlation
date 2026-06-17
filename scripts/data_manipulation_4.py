import pandas as pd

# Load your data
df = pd.read_csv('Education_and_Employment.csv')

# Replace "Valid skip" and "Not stated" everywhere with empty cells
df = df.replace('Valid skip', '')
df = df.replace('Not stated', '')

# Fix Region names for Tableau mapping
df['Region of Postsecondary Institution'] = df['Region of Postsecondary Institution'].replace({
    'Western provinces/territories': 'Western Canada',
    'Atlantic provinces': 'Atlantic Canada'
})

# Code Level of Study Grouping
df['Level of Study Grouping'] = df['Level of Study Grouping'].replace({
    "Master's/Doctorate": 3,
    "Bachelor's": 2,
    "College": 1
})
df['Level of Study Grouping'] = df['Level of Study Grouping'].where(df['Level of Study Grouping'].isin([1,2,3]), '')

# Code Total Personal Income in 2022
df['Total Personal Income in 2022'] = df['Total Personal Income in 2022'].replace({
    "Less than $30,000": 20000,
    "$30,000 to $49,999": 40000,
    "$50,000 to $69,999": 60000,
    "$70,000 to $89,999": 80000,
    "$90,000 or more": 100000
})
df['Total Personal Income in 2022'] = df['Total Personal Income in 2022'].where(
    df['Total Personal Income in 2022'].isin([20000,40000,60000,80000,100000]), ''
)

# Save the cleaned and coded data
df.to_csv('Education-and-Employment-Cleaned-2.csv', index=False)

print("Done! Your cleaned and coded data is saved.")