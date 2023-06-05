# a. Write a function called mycarcount that takes two parameters: cars as a data frame, and year as an integer, and outputs the number of cars from that year. (Alternatively, you can just use 1 argument, the year, as a parameter, and then read through the cars data frame inside the function. Either way is OK.)


import pandas as pd
cars = pd.read_csv("/anvil/projects/tdm/data/craigslist/vehicles.csv")

def mycarcount(cars, year):
    """
    mycarcount is a function that accept cars and year as argument
    and returns the number of cars that occur on year for cars.
    
    Args:
    cars (df): The dataframe from which we are counting the number of cars.
    year (int): The years on which we are counting the number of vehicles.
    
    Returns:
        The numbers of cars on my dataframe during the year
    """
    # you are telling the python to run a row at atime and compare the values within the row
    
    total_count = 0
    for index, row in cars.iterrows ():
        if row ['year'] ==year:
            total_count +=1    
    return total_count

# b. Run the function for each of the years from Project 4, Question 4, namely, for the years 2011, 1989, 1997. Make sure that your answers agree with the results from that earlier project.

mycarcount(cars, 2016)

mycarcount(cars, 2011)

mycarcount(cars, 1989)

mycarcount(cars, 1997)

# The other way is putting the year at the begining of the fuction first


def mycarcount(year):
    """
    mycarcount is a function that accept cars and year as argument
    and returns the number of cars that occur on year for cars.
    
    Args:
    cars (df): The dataframe from which we are counting the number of cars.
    year (int): The years on which we are counting the number of vehicles.
    
    Returns:
        The numbers of cars on my dataframe during the year
    """
    # you are telling the python to run a row at a time and compare the values within the row
   
    # Defining the cars as varriable before ruuning the code
    cars = pd.read_csv("/anvil/projects/tdm/data/craigslist/vehicles.csv")
    total_count = 0
    for index, row in cars.iterrows ():
        if row ['year'] ==year:
            total_count +=1 
    return total_count

mycarcount(2016)
    
mycarcount(2011)

mycarcount(1989)

# You can run it like this too
# len will let you run through dataframe and the rows and the corresponding year.

# To write a function just named it anything eg cc

def cc(carsdf, myyear):
    mycount = len(carsdf[carsdf.year == myyear])
    return mycount

cc(cars, 2011)

cc(cars, 1989)

cc(cars, 1997)

# a. Run the function mycarcount for each year in the data set. (Of course, be sure to only run it once for each year!)

# b. Now make sure that the results agree, if you compare with the value_counts() from the year column.


# to generate the unique years in the data

cars.year.unique()

# To make it a variable
yrlist =cars.year.unique()

# To sort them out, rearranged
yrlist.sort()

# To generate the values after sorting
yrlist

# To eliminate the nan 
ylist = yrlist[:-1]

# The years after removing nan
ylist

# i used for loop to generate my output

for i in yrlist:
    a = cc(cars,i)
    print (i, a)
    
    
# a Write a function that takes two parameters: myorigin as a string with three characters, and year as an integer, and outputs the number of flights that depart during that year, from the Origin airport indicated in myorigin.

# b. Test your function for a few years and airports of your choice. You can choose! Do your results look reasonable, i.e., do the airports in the big cities have lots of flights, compared to airports in smaller cities?


import pandas as pd
from pathlib import Path

def getflight(myorigin, yr):
    
# f' means for the most path we have regular string, instead for the curly bracket everything in it we turn into a string also
# year is an integer. they dont play well together.

    total_count=0
    airport = pd.read_csv(f'/anvil/projects/tdm/data/flights/subset/{yr}.csv')
    for index, row in airport.iterrows ():
        if row ['Origin'] ==myorigin:
            total_count +=1   
    return total_count 

# this is specified to csv file of year 2016
f'/anvil/projects/tdm/data/flights/subset/{2016}.csv'

# To know the different Origin available
# You will consider for a particular year (1989)
# Then look for the uniqueness

airport = pd.read_csv(f'/anvil/projects/tdm/data/flights/subset/1989.csv')

# to know all the origin available, then we consider a particular year.
airport.Origin.unique()

getflight("ORD", 1989)

getflight("BTR", 1989)

getflight("PUB", 1999)

getflight("ATL", 2004)

getflight("DFW", 1998)

getflight('IND',1997)


# another mean to get it done

def getflight(myorigin, yr):
    file = Path(f'/anvil/projects/tdm/data/flights/subset/{yr}.csv')
    count = 0
    with open(file, 'r') as f: 
# file destination, r decides what you are using it for, 
# just for reading alone.store it in variable name f
        for line in f:
            if line.split(",")[16] == myorigin: # we spiliting into a list, removing the commas . index number 16
                count += 1
    return count  

getflight('IND',2004)

getflight('ATL',2004)

getflight('DFW',1998)



# c. Run the function for each of the years from 1987 to 2008, checking how many flights depart from IND in each year. Make sure that you use the method from the end of Project 3, Question 5.

for i in range(1987,2009):
    print(f"{i}:{getflight(f'IND', i)}")
    
   
 # a. Modify your function so that it takes three parameters: myorigin and mydest as strings that each have three characters, and year as an integer, and outputs the number of flights that depart during that year, from the Origin airport indicated in myorigin, and arrive at the Dest airport indicated in mydest.
    

def getflight(myorigin,mydest, yr):
    
# f' means for the most path we have regular string, instead for the curly bracket everything in it we turn into a string also
# year is an integer. they dont play well together.
    total_count=0
    airport = pd.read_csv(f'/anvil/projects/tdm/data/flights/subset/{yr}.csv')
    for index, row in airport.iterrows ():
        if (row ['Origin'] ==myorigin) and (row ['Dest'] ==mydest):
            total_count +=1   
    return total_count  

    
# b. Test your function for a few years and pairs of airports (origin and destination airports) of your choice. Do the results look reasonable, e.g., if you compare popular flight paths, versus unpopular flight paths?

getflight('IND','ORD', 1987)

getflight('IND','MDW', 1997)

getflight('SLC','GNV',2000)

getflight('GNV','ORD', 1997)


# c. Run the function for each of the years from 1987 to 2008, 
# checking how many flights depart from IND and arrive at ORD in each year.

for k in range(1987,2009):
    print(f"{k}:{getflight(f'IND','ORD', k)}")
    
# a. Write a function that takes two parameters: Sex (which will be F or M) and MaritalStatus (D or M or S or U or W), and outputs the number of people with the indicated Sex and MaritalStatus in the data set. (If you look at an earlier version of this question, in which we asked about the year of death, well, everyone in the data set died in 2014, so you do not need to worry about the year of death.)

def records(sex,maritalstatus):
    
# f' means for the most path we have regular string, instead for the curly bracket everything in it we turn into a string also
# year is an integer. they dont play well together.
    total_count=0
    people = pd.read_csv(f'/anvil/projects/tdm/data/death_records/DeathRecords.csv') # Varriable read in
    for index, row in people.iterrows ():
        if (row ['Sex'] ==sex) and (row ['MaritalStatus'] ==maritalstatus):
            total_count +=1   
    return total_count 


# This is the csv file
pd.read_csv(f'/anvil/projects/tdm/data/death_records/DeathRecords.csv')
# read it into variable people
people = pd.read_csv(f'/anvil/projects/tdm/data/death_records/DeathRecords.csv')

records("F","D")

records("M","D")

records("F","M")

records("M","S")