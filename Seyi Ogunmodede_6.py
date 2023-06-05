#Modify your mycarcount function from Question 1 of Project 5, so that it takes a list of years as a parameter, and prints the number of vehicles from  each year in your list.

# Now test your mycarcount function on the list of years [2011, 1989, 1997]. The output from mycarcount(cars, [2011, 1989, 1997]) or from mycarcount([2011, 1989, 1997]) should be the number of vehicles from each of the years 2011, 1989, and 1997, respectively.

import pandas as pd
cars = pd.read_csv("/anvil/projects/tdm/data/craigslist/vehicles.csv")

def mycarcount(cars, year):
    """
    mycarcount is a function that accept cars and year as argument
    and returns the number of cars that occur in each year for cars.
    
    Args:
    cars (df): The dataframe from which we are counting the number of cars.
    year (int): The years on which we are counting the number of vehicles.
    
    Returns:
        The numbers of cars on my dataframe during the year
    """
    # you are telling the python to run a row at atime and compare the values within the rows
    # Then return the total_count afterwards
    
    total_count = 0
    for index, row in cars.iterrows ():
        if row ['year'] ==year:
            total_count +=1    
    return total_count

# This is for each year 
mycarcount(cars, 2016)

mycarcount(cars, 2011)

# This is for loop for the list of year as parameter and take 
# To prints the number of vehicles from each year in the list
# The syntax code has a comma separator in it

for year in [2011, 1989, 1997]:
    print(f'On the year', year, 'there were a total of', mycarcount(cars, year), 'vehicles')

    
# This is for loop for the list of year as parameter and take 
# To prints the number of vehicles from each year in the  list
# The syntax code has a curly bracket in it

for year in [2011, 1989, 1997]:
    print(f'On the year {year} there were a total of', mycarcount(cars, year), 'vehicles')
    
    
    
def mycarcount(cars,listofyear):
    """
    mycarcount is a function that accept cars and listofyear as argument
    and print the total number of cars that occur from each year in the list.
    
    Args:
    cars (df): The dataframe from which we are counting the number of cars.
   listofyear (int): The years on which we are counting the number of vehicles.
    
   print:
        The total numbers of cars from each year in the listofyear 
    """
    # you are telling the python to run a row at atime and compare the values within the row
    # for loop for each year in the listofyear
    
    for year in listofyear:
        total_count = 0
        for index, row in cars.iterrows ():
            if row ['year'] ==year:
                total_count +=1
        print (total_count) 
        
        
mycarcount(cars, [2011, 1989, 1997])

def mycarcount(listofyear):
    """
    mycarcount is a function that accept one argument, listofyear as an argument
    and print the total number of cars that occur from each year in the list.
    
    Args:
    cars (df): The dataframe from which we are counting the number of cars.
    year (int): The years on which we are counting the number of vehicles.
    
    print:
        The total numbers of cars from each year in the listofyear 
    """
    # First, you have to run the Dataframe from which to count the number of cars from
    # you are telling the python to run a row at atime and compare the values within the row
    
    cars = pd.read_csv("/anvil/projects/tdm/data/craigslist/vehicles.csv")
    for year in listofyear:
        total_count = 0
        for index, row in cars.iterrows ():
            if row ['year'] ==year:
                total_count +=1 
        print(total_count)
               
mycarcount([2011, 1989, 1997])

# Write a loop that prints the number of vehicles from chicago as the region in each of the years 2016, 2017, 2018. (I.e., you should have 3 lines of output.)

# Now write a double-loop that prints the number of vehicles from each region in the list [chicago, indianapolis, cincinnati] in each of the years 2016, 2017, 2018. (I.e., you should have 9 lines of output.)


def records(region,year):  
    """
    records is a function that accept region and year as argument
    and returns the number of cars that occur in each year for cars.
    
    Args:
    region(str): The region which we are counting the number of cars.
    year (int): The years on which we are counting the number of vehicles.
    
    Returns:
        The numbers of cars on each region during each year 
    """
# First, you have to run the Dataframe from which to count the number of cars from
# you are telling the python to run a row at atime and compare the values within the row

    total_count=0
    cars = pd.read_csv("/anvil/projects/tdm/data/craigslist/vehicles.csv")
    for index, row in cars.iterrows ():
        if (row ['year'] ==year) and (row ['region'] ==region):
            total_count +=1   
    return total_count 

# first define what year is, to be list of years
year=[2016, 2017, 2018]

# Different ways to write the syntax code.

for i in (year):
    a =records("chicago",i)
    print (f'On the year', i, 'there were a total of', a, 'vehicles from chicago')
    
    
for i in [2016, 2017, 2018]:
    a =records("chicago",i)
    print (f'On the year', i, 'there were a total of', a, 'vehicles from chicago')
    
for year in [2016, 2017, 2018]:
    counts=records("chicago",year)
    print (counts, year)
    
# Double for loop

for year in [2016,2017,2018]:
    for region in['chicago','indianapolis','cincinnati']:
        print(f'On the year', {year}, 'there were a total of', records(region,year),f'vehicles from {region}')

# Write a function with two arguments: a list of regions, and a list of years. The function should print a listing that shows the number of vehicles from each of those regions in each of those years. (I.e., it will print one line of output for each region during each year.)

# Use your new function to re-create the answer to question 2b.

# Test your function on some lists of regions and lists of years of your choice.        
        
for year in [2016,2017,2018]:
    for region in['chicago','indianapolis','cincinnati']:
        print(f'On the year', {year}, 'there were a total of', records(region,year),f'vehicles from {region}')
        
def rv(mylistofyear, mylistofregion):
    """
   rv is a function that accepts mylistofyear and mylistofregion as arguments,
    and returns the number of vehicles that during on each year in mylistofyear and each car in mylistofregion.

    Args:
        mylistofyear (list): The year on which we are counting the number of cars.
        mylistofregion (list): The cars on which we are counting in a region.

    Returns:
        Nothing.  Instead, we just print the values on each year for the cars.
    """
    for year in mylistofyear:
        for region in mylistofregion:
            print(f'On the year', {year}, 'there were a total of', records(region,year),f'vehicles from {region}')
            
rv([2011,1989,1997], ['chicago','indianapolis','cincinnati'])

pd.options.display.max_columns = None

cars.head()

cars.tail()

rv([2011,1989,1997], ['oregon coast','mohave county','maine'])


# Write a loop that prints the number of flights that depart from IND as the Origin airport in each of the years 1988, 1989, 1990. (I.e., you should have 3 lines of output.)

# Now write a double-loop that prints the number of flights that depart from each of the airports IND, ORD, CVG as the Origin airport in each of the years 1988, 1989, 1990. (I.e., you should have 9 lines of output.)

import pandas as pd
from pathlib import Path

def getflight(myorigin, yr):
    

    total_count=0
    airport = pd.read_csv(f'/anvil/projects/tdm/data/flights/subset/{yr}.csv')
    for index, row in airport.iterrows ():
        if row ['Origin'] ==myorigin:
            total_count +=1   
    return total_count 

getflight("IND", 1988)
            
getflight("IND", 1989)


for i in [1988, 1989, 1990]:
    print(f"{i}:{getflight(f'IND', i)}")
    

for yr in [1988, 1989, 1990]:
 
    print(f'On the year {yr} there were a total of', getflight("IND", yr), 'flights')
    
for yr in [1988, 1989, 1990]:
    for myorigin in['IND', 'ORD', 'CVG']:
        print(f'On the year {yr} there were a total of', getflight(myorigin, yr),f'flights from {myorigin}')

        
# Write a function with two arguments: a list of Origin airports, and a list of years. The function should print a listing that shows the number of flights departing from each of those Origin airports in each of those years. (I.e., it will have one line of output for each Origin airport during each year.)

# Use your new function to re-create the answer to question 4b.

# Test your function on some lists of Origin airports and lists of years of your choice.

        
def getlist(mylistofyear, mylistoforigin):
    """
  getlist is a function that accepts mylistofyear and mylistoforigin as arguments,
    and returns the number of flights departing from each Origin airports during 
    each year in mylistofyear and each car in mylistoforigin.

    Args:
        mylistofyear (list): The year on which we are counting the number of flight.
        mylistoforigin (list): The flights on which we are counting in a origin.

    Returns:
        Nothing.  Instead, we just print the values on each year for the cars.
    """
    for yr in mylistofyear:
        for myorigin in mylistoforigin:
            print(f'On the year {yr} there were a total of', getflight(myorigin, yr),f'flights from {myorigin}')
            
for yr in [1988, 1989, 1990]:
    for myorigin in['IND', 'ORD', 'CVG']:
        print(f'On the year {yr} there were a total of', getflight(myorigin, yr),f'vehicles of{myorigin}')
        
    
pd.options.display.max_columns = None  

airport = pd.read_csv(f'/anvil/projects/tdm/data/flights/subset/1989.csv')

airport.head()

for yr in [1988, 1989, 1990]:
    for myorigin in['MSP', 'MSO', 'MYR']:
        print(f'On the year {yr} there were a total of', getflight(myorigin, yr),f'vehicles of{myorigin}')