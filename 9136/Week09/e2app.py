# *Exercise 2:  Working with Pandas<a class="anchor" id="exercise-2"
# Firstly, let's load the data about of the height, weight,
# and gender of the person (i.e. the `height_weight.csv` file),
# assign to a variable named `df`, and show the data frame
# contains the information using print:

import pandas as pd

df = pd.read_csv('height_weight.csv',index_col=0)


# Slicing with .loc and .iloc
# Selecting particular rows and columns from a DataFrame
# is referred to as "slicing".
# We can use .loc[index_label, column_label] to slice by label:

# Row 2, "height" column
text_height = df.loc[2,"height"]
# print(text_height)
# >>187

# All rows from 1 to 3, and the "height" column
text_height_all = df.loc[1:]
# print(text_height_all)

# Select only the initial rows up to the 3rd row,
# and the "name" and "weight" columns
text_initial = df.loc[:2,["name","weight"]]
# print(text_initial)



# Modifying the index
# Recall that we can select rows corresponding to a given person using:
condition = df['name'] == 'Dinesh'
condition = df[condition]
# print(condition)

# However, we can change the index to one of the columns in the DataFrame:
df.set_index('name', inplace=True)
df.loc["Julia"]
# print(df.loc["Julia"])

# However, if we want to slice by position,
# we now have to use .iloc[position] to do so:

# # 0th row, all columns
df.iloc[0]
# print(df.iloc[0])

# Initial rows up to 1st row, and the "height" column
# (which is now the 0th column)
df.iloc[:2,0]
# print(df.iloc[:2,0])


# Adding and altering columns
# We can add a column to a DataFrame like so:
df['age']=[39,43,22,44,27]
# print(df)


# Now use the cell below to create a new column called last_name
# which contains each person's last name (just make up some last names).
df['last_name'] = [139,243,322,444,527]
# print(df)

# Note that we can change column names using the .rename() , method:
df = df.rename(columns={'name': 'first_name',
                   'height': 'height (cm)',
                   'weight': 'weight (kg)'})
# print(df.columns)

# We can also combine data from different columns into a new column.
# For example, let's create a new column for the full name of each person
# in the table:
df_income = pd.read_csv('income.csv')
# print(df_income)


# Note that the new full_name column does not contain any whitespace between
# the two names, because we simply concatenated the two columns using the + operator.
# See if you can re-create the full_name column in the code cell below,
# but this time include a single whitespace character between the two names:
df['full_name'] = df.last_name
#  + ' ' + df.last_name
# print(df)

# You can also use the .apply() method to apply a function to
# all entries in a column.
# Create new column containing number of characters in each person's full_name

# df['full_name_len'] = df.full_name.apply(len)
# print(df)


