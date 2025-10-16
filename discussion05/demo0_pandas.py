"""
This is a quick demo on some pandas basics
"""

import numpy as np
import pandas as pd

# ==============================
# Creating series and dataframes
# ==============================
# see more info here:
# https://pandas.pydata.org/docs/user_guide/dsintro.html
#-------------------
# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

# with index
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)
print(s)

# Create a Series from a dictionary
data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
s = pd.Series(data)
print(s)

# Create a Series from a scalar value
s = pd.Series(5, index=['a', 'b', 'c', 'd', 'e'])
print(s)

# Create a DataFrame from lists


# Create a DataFrame from a dictionary
data = {'A': [1,2,3], 'B': [4,5,6]}
df = pd.DataFrame(data)
print(df)

# ==============================
# Indexing and selecting data
# ==============================
# see more info here:
# https://pandas.pydata.org/docs/user_guide/indexing.html
#-------------------
# indexing with .loc[]
data = {'col_0': [0, 10, 20], 'col_1': [1, 11, 21]}
df = pd.DataFrame(data, index=['row_A', 'row_B', 'row_C'])

# Select a single cell by label
value = df.loc['row_B', 'col_1']
print(f"Value at row_B, col_1: {value}")

# Select a row by label
row = df.loc['row_A']
print(f"\nRow 'row_A':\n{row}")

# Select multiple columns by label
subset = df.loc[:, ['col_0']]
print(f"\nSubset with 'col_0':\n{subset}")


#-----------------
# indexing with .iloc[]
data = {'col_0': [0, 10, 20], 'col_1': [1, 11, 21]}
df = pd.DataFrame(data, index=['row_A', 'row_B', 'row_C'])

# Select a single cell by integer position
value = df.iloc[1, 1]
print(f"Value at position 1, 1: {value}")

# Select a row by integer position
row = df.iloc[0]
print(f"\nRow at position 0:\n{row}")

# Select multiple columns by integer position
subset = df.iloc[:, [0]]
print(f"\nSubset with column at position 0:\n{subset}")

# ---------------
# quick scalar acess with df.at[] (label-based)
data = {'col_0': [0, 10, 20], 'col_1': [1, 11, 21]}
df = pd.DataFrame(data, index=['row_A', 'row_B', 'row_C'])

# Get a single value using .at
value = df.at['row_B', 'col_0']
print(f"Value at row_B, col_0 using .at: {value}")

# Set a single value using .at
df.at['row_A', 'col_1'] = 99
print(f"\nDataFrame after setting value with .at:\n{df}")


# ------------------
# scalar acess integer-loc based
value = df.iat[1,0]
print(f"Value at position 1, 0: {value}")

# Set a single value using .at
df.iat[1,0] = 99
print(f"\nDataFrame after setting value with .iat:\n{df}")


# ==============================
# Concatenate, merge and join
# ==============================
# see more info here:
# https://pandas.pydata.org/docs/user_guide/merging.html
# ------------------
# concat
exp1 = pd.DataFrame({'temp': [300, 310], 'count': [15, 20]})
exp2 = pd.DataFrame({'temp': [320, 330], 'count': [25, 18]})
all_data = pd.concat([exp1, exp2], ignore_index=True)
print('\nconcatenate dataFrames:')
print(all_data)


# merge
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Value': [10, 20, 30]})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Category': ['A', 'B', 'C']})

merged_df = pd.merge(df1, df2, on='ID', how='inner')
print('\nmerge dataFrames:')
print(merged_df)


# ==============================
# Exporting DataFrames
# ==============================
# see more info here:
# https://pandas.pydata.org/docs/user_guide/io.html
# ------------------
# write to csv file
all_data.to_csv('someData.csv',index=False)
