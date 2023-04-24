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

# Find the maximum value of a column
clean_df['Starting Median Salary'].max()

# Find the index / row where the maximum value occures
clean_df['Starting Median Salary'].idxmax()

# Access other properties(column name) for this row where max value occured, now that we know the row number.
clean_df['Undergraduate Major'].loc[43]

# or other way of accessing the same thing as above
clean_df['Undergraduate Major'][43]

# Print the entire row where max value ocuured
clean_df.loc[43]

# Find the differnce between two columns
spread = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

# Insert a column in position "1" in the the data. i.e the second column and 'name' it.
clean_df.insert(1, 'Spread', spread)

"""Sort the data by a column name"""

low_risk = clean_df.sort_values('Spread')

"""Display the sorted data based on desired column"""

low_risk[['Undergraduate Major', 'Spread']].head()

""""groupby" for knowing different types of catagories"""

clean_df.groupby('Group').count()

"""Find mean by a group (category)"""

clean_df.groupby('Group').mean()

# Tell panda to Formate number in a specific way
pd.options.display.float_format = '{:,.2f}'.format

# now the numbers will be printed in the specified format(, after 3 digits and 2 places after decimal)
clean_df.groupby('Group').mean()