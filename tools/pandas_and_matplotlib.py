# importing pandas, matplotlib
import pandas as pd
import matplotlib.pyplot as plt

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

# #####################
# FEW OTHER COMMANDS #
# ####################

#  Read the csv file and give the column names
df = pd.read_csv('QueryResults.csv',names=['DATE', 'TAG','POSTS'], header=0)

# Find the total sum of posts by category ('TAG' in this case)
total_by_tag = df.groupby('TAG').sum()

# Get an entry from a column. Date column, second cell(entry)
df['DATE'][1]

df.DATE[1] # another way of doing

# Check the data type of an entry
type(df['DATE'][1])

# Use pandas's to_datetime method to convert str to Timestamp
# Convert entire column
df['DATE'] = pd.to_datetime(df['DATE'])

# pivoting dataframe: tmaking a column of data as seperate column
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')

#  list all the columns
reshaped_df.columns

reshaped_df

# Count entries in each column
reshaped_df.count()

# Replace NaN values with 0 using .fillna
reshaped_df.fillna(0, inplace=True)

# Check if dataframe has any NaN
reshaped_df.isna().values.any()


# ##########    MATPLOTLIB     #####################

# Plot using matplotlib
plt.plot(reshaped_df.index,reshaped_df.java)

# Styling the chart
# Resize chart using .figure()
plt.figure(figsize=(16,10))

# Plot after resizing
plt.plot(reshaped_df.index, reshaped_df.java)

# Increase the font sizes
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Plot again to see the above changes applied
plt.plot(reshaped_df.index, reshaped_df.java)

# Add lables. NOTE: for all these changes to be applicable, the entire code should run in a single block in colab
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
# Add limits to y axis
plt.ylim(0, 35000)
# Plot after applying changes
plt.plot(reshaped_df.index, reshaped_df.java)
# plot another set of data in the same plot
plt.plot(reshaped_df.index,reshaped_df.python)

# Plot multiple data sets(columns). In this case multiple programming languages
for column in reshaped_df.columns:
  plt.plot(reshaped_df.index,reshaped_df[column], linewidth=2, label=reshaped_df[column].name)
# plt the legend (labeling what is what)
plt.legend(fontsize=10)

# Smoothing out the time series data
# window: the number of data we take as a chunk (6 or 12) to take an average
roll_df = reshaped_df.rolling(window=12).mean()

# plot again using roll_df dataframe
for column in roll_df.columns:
  plt.plot(roll_df.index, roll_df[column], label=roll_df[column].name)
plt.legend()
