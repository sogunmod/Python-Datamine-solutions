# ls - it means file listing , to show all the files in the folder
ls /anvil/projects/tdm/data/flights/subset/

ls /anvil/projects/tdm/data/flights/subset/2003.csv

# for more information about the files

ls -la /anvil/projects/tdm/data/flights/subset/2003.csv

# to check all of the files that begins with 2

ls -la /anvil/projects/tdm/data/flights/subset/2*.csv

# this syntax is used to look at all of them removing the year.
ls -la /anvil/projects/tdm/data/flights/subset/*.csv

import pandas as pd
from pathlib import Path

# Notice that, in a range in Python, the final number in the range is not included.
# This code uses list comprehension to create a list of file paths, 
# ranging from the years of 1987-2008 files will now 
# contain strings of file paths for all the csv files in this directory.

files = [Path(f'/anvil/projects/tdm/data/flights/subset/{year}.csv') for year in range(1987,2009)]

files

files[0]

eightyseven = pd.read_csv(files[0]) 
print(eightyseven.columns)
# 'Year', 'Month', 'DayofMonth', 'DayOfWeek', 'DepTime', 'CRSDepTime',
#        'ArrTime', 'CRSArrTime', 'UniqueCarrier', 'FlightNum', 'TailNum',
#        'ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay',
#        'DepDelay', 'Origin', 'Dest', 'Distance', 'TaxiIn', 'TaxiOut',
#        'Cancelled', 'CancellationCode', 'Diverted', 'CarrierDelay',
#        'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay'


eightyseven.shape
# How many columns are there? 29 columns are there


# i think that we have flight data from Oct 1987 through April 2008
# i think that each year from 1988 to 2007 has all 12 months
# but the first and the last files are just a portion of the year.

# When you run this code it displayed the hidden column
pd.options.display.max_columns = None

eightyseven.head()
# the data from the first five rows.

eightyseven.tail()

# from row 0 to row 1311825 it has three letters (SAN ORD, BOS and so on)
eightyseven['Origin']

# This will show all the origin where the flight will take off from
eightyseven['Origin'].value_counts()

# for unique/specific
eightyseven['Origin'].value_counts()['IND']
# 8817 times that IND occurs in the Origin column

# This extract all of the counts of the number of times that each airport
# is the Origin city for a flight, i.e, where the flight departs.
# Then we extract the value for the indianapolis, e.g, in this case
# Indianapolis was the origin city for 8817 flights between Oct 1987 and Dec 1987.

files[1]
eightyeight = pd.read_csv(files[1]) 
eightyeight['Origin'].value_counts()['IND']
# 37399 times was 'IND' the Origin airport in eightyeight

files[2]
eightynine = pd.read_csv(files[2]) 
eightynine['Origin'].value_counts()['IND']
# 40567 times was 'IND' the Origin airport in eightynine

files[3]
ninety = pd.read_csv(files[3]) 
ninety['Origin'].value_counts()['IND']
# 43826 times was 'IND' the Origin airport in ninety

import pandas as pd
from pathlib import Path

files = [Path(f'/anvil/projects/tdm/data/flights/subset/{year}.csv') for year in range(1987,2009)]

pd.options.display.max_columns = None

# This is good reasoning and it would work except 
# our files are large and our kernel will fail.
count = 0
for file in files:
    df = pd.read_csv(file)
    count += len(df[df['Origin'] == 'IND'])

print(count)
# 796496

# This method will work but, it will take a long time

total_count = 0
for file in files:
    for df in pd.read_csv(file, chunksize=10000):
        for index, row in df.iterrows():
            if row['Origin'] == 'IND':
                total_count += 1

print(total_count)

# this is a similar idea, but without the read_csv
# So we will not be storing the entire contents of any of the files in memory
# Instead, we will just loop through the file, one line at a time,
# checking to see if the Origin on that line of the file (the 16th field of the line)
# is equal to 'IND', and if it is, we add one to our counter called origin_ind
# At the very end we will print out the value of the counter, and that is equal to
# the total number of times that Indianapolis is the Origin city for a flight
# i.e, where a flight depart.

origin_ind = 0
for file in files:
    with open(file,'r') as f:
        for line in f:
            if line.split(",")[16] == 'IND':
                origin_ind += 1
print(origin_ind)
