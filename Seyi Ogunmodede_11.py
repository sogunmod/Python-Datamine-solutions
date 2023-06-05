# To see what is in the file, use ls and the files
# There is a folder for each year from 1975 - 2017
# # It has a file called 7581.csv and another state.csv

ls/anvil/projects/tdm/data/fars

# For me to see what is inside directory for 1985

ls/anvil/projects/tdm/data/fars/1985

import pandas as pd

myDF=pd.read_csv("/anvil/projects/tdm/data/fars/1985/ACCIDENT.CSV")

myDF.head(3)

# We want to put 19 infront of these 85
# To do this you can make/convert your column as string - myDF["myCol"].astype(str). 
# Then you can add another string. myDF["myCol"].astype(str) + "appending_this_string"
# We can append strings to every value in a column by first converting the column to str using astype then use the + operator:

# looking at the head focusing on the year column

myDF["YEAR"].head()

# Fisrt convert it to string and add 19 = 19+85 =1985

"19" + myDF["YEAR"].head().astype(str)

# If you run this nothing has changed, you have to assign it to the column

myDF.head()

# This code changed the column to 1985

myDF["YEAR"]="19" + myDF["YEAR"].astype(str)

myDF.head()

# I want to create a Dataframe called accidents that joins the ACCIDENT.CSV files 
# from the years 1985-1989 (inclusive) into one large Dataframe
# To do this, we can (Merge, Join,0r Concat) but i will concatenate them
# I will concatenate them on top of the next one

# https://pandas.pydata.org/docs/reference/api/pandas.concat.html

accidents=pd.concat([pd.read_csv("/anvil/projects/tdm/data/fars/1985/ACCIDENT.CSV"),
                    pd.read_csv("/anvil/projects/tdm/data/fars/1986/ACCIDENT.CSV"),
                    pd.read_csv("/anvil/projects/tdm/data/fars/1987/ACCIDENT.CSV"),
                    pd.read_csv("/anvil/projects/tdm/data/fars/1988/ACCIDENT.CSV"),
                    pd.read_csv("/anvil/projects/tdm/data/fars/1989/ACCIDENT.CSV")], ignore_index=True)

accidents.head(3)

accidents.tail(3)

# This gives the values each of the years

accidents["YEAR"].value_counts()

# To convert the YEAR column from a 2 digit year to a 4 digit year,
# like we did in the last question, but using a different method.
# we will use the to_datetime function, then take the old format 2digits represented by %y
# and once you have coverted to a datetime format, then you can display the year with %Y which is 4digits

#  the syntax code   pd.to_datetime(df[''], format='%y').dt.strftime('%Y')

pd.to_datetime(accidents["YEAR"], format='%y').dt.strftime('%Y')

accidents["YEAR"]= pd.to_datetime(accidents["YEAR"], format='%y').dt.strftime('%Y')

accidents.head(3)

accidents.tail(3)

# To know how many accidents are there in which one or more 
# drunk drivers were involved in an accident with a school bus

accidents["DRUNK_DR"].value_counts()

accidents["SCH_BUS"].value_counts()

accidents[(accidents["DRUNK_DR"] >= 1) & (accidents["SCH_BUS"]==1)]

accidents[(accidents["DRUNK_DR"] >= 1) & (accidents["SCH_BUS"]==1)].shape

# There are 79 rows, i.e, There are 79 accidents with at least 1 drunk driver and a school bus

# to find the accidents that happen in total per year between 1 or more drunk drivers and school bus.
# Instead of taken the shape, we can take the DataFrame and extract the year 

accidents[(accidents["DRUNK_DR"] >= 1) & (accidents["SCH_BUS"]==1)]["YEAR"]

accidents[(accidents["DRUNK_DR"] >= 1) & (accidents["SCH_BUS"]==1)]["YEAR"].value_counts()

# 1989 had the lowest number of accidents
# 1986 had the most number of accidents

# To know the days of the week that has the most accidents occurrence
# one of the days was recorded as 99 to have 31 but we don't know which day it was.

accidents["DAY"].value_counts()

# To avoid that, let see how many accident all together

accidents.shape

# let us make newaccidents to be the DataFrame
# That got everything from accidents, except the ones which day was equal to 99 

newaccidents = accidents [accidents["DAY"] !=99]

# Looking at the shape of accidents to newaccidents i only lost few values (31)

newaccidents.shape

# This will convert the year, month and day into a datetime value

pd.to_datetime(newaccidents[["YEAR", "MONTH", "DAY"]])

pd.to_datetime(newaccidents[["YEAR", "MONTH", "DAY"]]).dt.day_name()

pd.to_datetime(newaccidents[["YEAR", "MONTH", "DAY"]]).dt.day_name().value_counts()

# looking at the accidents, tons of accidents happened on Saturdays, Fridays and Sundays compared to the values durring the week
# Most accidents occur during the weekend.

# what time of day do you see more accidents? Using 12am-6am/ 6am-12pm/ 12pm-6pm/ 6pm-12am as your time frames

# First let us take look at the hour
# sometimes the hour is 99

accidents["HOUR"].value_counts()

# Same thing for the minutes if all were displayed
# sometimes the hour is 99
accidents["MINUTE"].value_counts()

# looking at the minutes values < 0, none of them are negative

accidents[accidents["MINUTE"]<0].shape

# There are rows that there minutes are bigger than 60

accidents[accidents["MINUTE"]>60].shape

# But fortunately, those are just the rows for  which is 99 
# Those are the ones that are unknown

accidents[accidents["MINUTE"]==99].shape

# i will make a new DataFrame, takes data from accidents and 
# ensure minutes not equal to 99 and ensure the hours also not equal to 99

newDF=accidents[(accidents["MINUTE"]!=99) & (accidents["HOUR"]!=99)]

# Looking at the shape of accident to newDF i only lost few values (1677)

accidents.shape

newDF.shape

# go into my newDF, take the hour and multiply by 60 to convert to minutes
# then add on the amount of minutes. Then output will be in minutes

pd.Series(newDF["HOUR"]*60 + newDF["MINUTE"]).between(0,360, inclusive="left")

# all these are between 12 midnight and 6:00 am
# meaning from Zero up to 360 in the day

pd.Series(newDF["HOUR"]*60 + newDF["MINUTE"]).between(0,360, inclusive="left").sum()

# Those are the ones between 6:00 am and 12:00 noon

pd.Series(newDF["HOUR"]*60 + newDF["MINUTE"]).between(360,720, inclusive="left").sum()

# Those are the ones between 12:00 noon and 6:00 pm

pd.Series(newDF["HOUR"]*60 + newDF["MINUTE"]).between(720, 1080, inclusive="left").sum()

# Those are the ones between 6:00 pm and 12 midnight

pd.Series(newDF["HOUR"]*60 + newDF["MINUTE"]).between(1080, 1440, inclusive="left").sum()

# for verification
# We are almost to the value in the newDF

46772+33815+55401+66733

# Those missing if you go all the way back are actually the ones for which the hour was 24
# In other words, for which the hour values was not recorded as Zero at midnight,
# but rather was recorded as it is 24 at midnight

202918-202721

# This sum to what was in the newDF

46772+33815+55401+66733+197

# Here is anothe way to solving it

import numpy as np

# considering the earlier coversion divide it by 360 and basically rounded down

pd.Series(newDF["HOUR"]*60 + newDF["MINUTE"])/360

# basically rounded down here to 0,1,2,3.......

(pd.Series(newDF["HOUR"]*60 + newDF["MINUTE"])/360).apply(np.floor)

(pd.Series(newDF["HOUR"]*60 + newDF["MINUTE"])/360).apply(np.floor).value_counts()

# 0.0    46772  between 12 midnight and 6:00 am
# 1.0    33815  between 6:00 am and 12:00 noon
# 2.0    55401  between 12:00 noon and 6:00 pm
# 3.0    66733  between 6:00 pm and 12 midnight
# 4.0      197  The extra 197 accidents are from those recorded at midnight as 24 instead of 0