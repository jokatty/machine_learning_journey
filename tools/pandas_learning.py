# importing pandas
import pandas as pd

# Reading a file
df = pd.read_csv('filename.csv')

# Printing first five data lines
df.head()

# Printing last five data rows
df.tail()

# Getting number of rows and columns
df.shape


# Get the columns name
df.columns


#  Check for is NaN value
df.isna()

# Drop the rows with NaN values
# MAKE SURE TO STORE THE CLEAN DATA IN A VARIABLE
clean_df = df.dropna()

# Typing just the variable name in colab will print all the data
clean_df

# Print a column
clean_df['Starting Median salary']