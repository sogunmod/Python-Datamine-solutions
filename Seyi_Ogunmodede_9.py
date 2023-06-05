# It is helpful to use a Parquet file when we need efficient storage
# If we tried to read in all the .csv files in the disney folder the kernel would crash
# In short a Parquet file allows for high performance data compression and encoding 
# schemes to deal with large amounts of complex data. 
# The format is a column-oriented file format while .csv’s tend to be row-oriented

# Since there is a lot of new ride data, let’s print the name of each ride.

# to know the files that are in the Disney directory
# using ls/anvil/projects/tdm/data/disney
# there are seperate files for each ride
# There is a ride called total.parquet
# it has information of all of the rides in it.
# to import the file which is not a csv, 
# you have to use read_parquet function

ls/anvil/projects/tdm/data/disney

import pandas as pd
disney = pd.read_parquet('/anvil/projects/tdm/data/disney/total.parquet')

disney.head()

disney.columns

disney['ride_name']

isney['ride_name'].head()

# to look at the unique entry in that column

disney['ride_name'].unique()

# if everything is wrapped up in a print, array will not show again. 
# output looks more natural

print(disney['ride_name'].unique())

# How many rows of data are there for each ride?

disney.groupby(['ride_name']).count()

disney['ride_name'].value_counts()

# What is different about the information that you receive if you use the groupby() vs value.count()? For groupby it gave four columns output which both data and datetime gave same value, while value count gave a single columns and with no confussion.

# Which one yields the information asked by question 1b? value count Why? gave a single columns and with no confussion

disney.shape

disney['ride_name'].shape

# Go ahead and import the numpy package and see if you can find the frequency of JUST the ride named hall_of_presidents from the column ride_name. Under Helpful Hint there are two different ways to do that, but can you come up with a third?

import numpy as np
disney[disney.ride_name == 'hall_of_presidents'].shape[0]

disney[disney.ride_name == 'hall_of_presidents']

(disney['ride_name']=='hall_of_presidents').sum()

disney['ride_name'].value_counts()['hall_of_presidents']

# this will display both true and false

len(disney['ride_name']=='hall_of_presidents')

# This gives a value for 'hall_of_presidents'

len(disney[disney['ride_name']=='hall_of_presidents'])

# Create a new function that accepts a ride name as an argument, and prints two things: (1) the first year the data for that ride was collected, and (2) the most recent year that the data for that ride was collected.

# picking 'kilimanjaro_safaris'
# look for the row of the dataframe = 'kilimanjaro_safaris'

disney[disney['ride_name'] == 'kilimanjaro_safaris'].shape

disney[disney['ride_name'] == 'kilimanjaro_safaris'].head()

disney[disney['ride_name'] == 'kilimanjaro_safaris'].tail()

disney[disney['ride_name'] == 'kilimanjaro_safaris']['date']

# converting the data to datetime first
# then .dt.year will work afterwards

pd.to_datetime(disney[disney['ride_name'] == 'kilimanjaro_safaris']['date']).dt.year

# then i can aggregate my data to pull out whatever i want.

pd.to_datetime(disney[disney['ride_name'] == 'kilimanjaro_safaris']['date']).dt.year.agg(['min','max'])

disney[disney['ride_name'] == 'flight_of_passage'].head()

disney[disney['ride_name'] == 'flight_of_passage'].tail()

pd.to_datetime(disney[disney['ride_name'] =='flight_of_passage']['date']).dt.year.agg(['min','max'])

def oldandrecentyears(myride: str)-> None:
    """
    oldadrecentyears accept myride as an arguments and print old and recent years for that ride
    Args:
        my ride (str): The ride for which we want to find old and recent years
    Returns:
        None: This function doesnot return any value.
              Instead it prints old and recent values of the years for a ride    
    """
    # make a data frame with the rows corresponding to my ride and extract old and recent years
    print(pd.to_datetime(disney[disney['ride_name'] ==myride]['date']).dt.year.agg(['min','max'])) 
    return None

oldandrecentyears('kilimanjaro_safaris')

oldandrecentyears('flight_of_passage')

oldandrecentyears('mad_tea_party')

# How many total rows of data do we have?
# the total row
disney.shape[0]

# How many non-null rows for SPOSTMIN?

disney['SPOSTMIN'].head()

disney['SACTMIN'].head()

# Lookig in to see, are those values null?
# the first values are not null 
# the last values are not null

disney['SPOSTMIN'].isnull()

#Then we can summ up to know the null values that are in between
# sum up the trues and falses
# True values become a 1 when we sum and false values become 0
# There are 192389 NAN values in the SPOSTMIN column


disney['SPOSTMIN'].isnull().sum()

# How many non-null rows for SACTMIN?

#Then we can summ up to know the null values that are in between
# sum up the trues and falses
# True values become a 1 when we sum and false values become 0
# There are 10113751 NAN values in the SPOSTMIN column

disney['SACTMIN'].isnull().sum()

# Combine columns SPOSTMIN and SACTMIN to create a new variable named newcolumn

# The total number of NAN values is the same as the total number of rows in the data frame
# There is one NAN value per row, in either column 
# there is going to one NAN value and one actual value 

disney['SPOSTMIN'].isnull().sum() + disney['SACTMIN'].isnull().sum()

# we will not actually integrate this into the data frame as a new column, 
# but we could if we wanted to 

newcolumn = disney['SACTMIN'].combine_first(disney['SPOSTMIN'])

# we have removed all NAN values when building this new column! Every value is present now; nothing missing

newcolumn.isnull().sum()

# What is the length of newcolumn? Is that the same as the number of rows in the disney dataframe?

# the length of the newcolumn is the same as the number of rows in the data frame itself 

len(newcolumn)

# Note that the value -999 indicates that the attraction was closed.

# Find the max and min SACTMIN time for each ride

disney.groupby('ride_name')['SACTMIN'].agg(['min','max'])




# Find the max and min SPOSTMIN time for each ride

disney.groupby('ride_name')['SPOSTMIN'].agg(['min','max'])

# Instead of working on the entire data frame you can go in 
# and work on the value that the SPOSTMIN is not equal to -999
# then we can work around the values with min 0

disney[disney['SPOSTMIN'] !=-999.0].groupby('ride_name')['SPOSTMIN'].agg(['min','max'])

# Find the average SPOSTMIN time for each ride

disney.groupby('ride_name')['SACTMIN'].mean()

# Find the average SACTMIN time for each ride

disney.groupby('ride_name')['SPOSTMIN'].mean()

disney[disney['SPOSTMIN'] !=-999.0].groupby('ride_name')['SPOSTMIN'].mean()


# Find the date that each ride was most frequently checked.

# What was the most commonly closed ride? (Again, note that the value -999 indicates that the attraction was closed.)

disney.groupby('ride_name')['date'].value_counts()

checked = disney.groupby('ride_name')['date'].value_counts()
checked

# go into group according to ride_name in checked, work with each of the ride individually
# And pull out what were the maximum values

checked.groupby('ride_name').idxmax()

# Then you can go ahead and look at the ride individually

checked['7_dwarfs_train']

checked['flight_of_passage']

checked['winnie_the_pooh']

# Again, note that the value -999 indicates that the attraction was closed.

disney[disney['SPOSTMIN'] ==-999.0].groupby('ride_name')['SPOSTMIN'].count()


