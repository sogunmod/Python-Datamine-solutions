import pandas as pd

# The airline data has lot of columns
# You will not see all of them unless you ask it to show all the columns
# i will set my pandas to show me all of them
# from 1987-2008,this takes a very long time in pandas

pd.set_option('display.max_columns', None)

# to make it faster, we can use things from the bass shell
# we could make a call to shell underneath the hood 
# we could talk to the operating system directly


# This indicates that is not python code
# This is show code. What does it do? I am doing two things

# I am taking my first line out of my 1987 flight data 
# and storing it in a new file in my home directory, Tilda (~)

# I take the first sign from 1987 dataset 
# and put it in a file called INDflights.csv

# That will just only get the header from the 1987 file 
# and store it in this new file i am building. You could do for any year it doesnot really matter.

# We just want to get the header first then afterwards we will know what the column represent.
# Then, from all of the other files that has (*.csv) extension on them, we are going to search for the phrase ",IND,"
# Then we will end up finding the Origin and Destination columns from them.
# None of the columns is going to say IND

%%bash
head -n1 /anvil/projects/tdm/data/flights/subset/1987.csv >~/INDflights.csv
grep -h ",IND," /anvil/projects/tdm/data/flights/subset/*.csv >>~/INDflights.csv


# Then, I can load in from this new files that i built
# Also, I put a tilda (~) in the front to say this is my home directory 

myDf=pd.read_csv('~/INDflights.csv')


# a. How many flights are there altogether in myDF? You can check this using myDF.shape.
# There are 1589899 flights in our file altogether

myDf.shape

# To know how many flight deoarted from indianapolis

# b. How many of the flights are departing from IND? (I.e., the Origin airport is IND.)
# There are 796496 flights departing from indianapolis.

myDf[myDf['Origin']=='IND'].shape

# c. How many of the flights are arriving to IND? (I.e., the Dest airport is IND.)
# There are 793403 flights ariving to indianapolis

myDf[myDf['Dest']=='IND'].shape

# for all flights departing from indiaapolis,
# we want to study the destination airport.
# and see how many times each destination airports occurs
# and display the most popular 20 of them.

myDf[myDf['Origin']=='IND']['Dest'].value_counts().head(20)

# for all flights departing from indiaapolis,
# we want to study the popular airlines.
# and see how many times each airline occurs
# and display the most popular 5 UniqueCarrier`s of them.

myDf[myDf['Origin']=='IND']['UniqueCarrier'].value_counts().head(5)

myDf.head()

myDf.tail()

myDf['UniqueCarrier'].value_counts()

def myrecords(myDf: pd.DataFrame, myairport: str)-> pd.Series:
    """
    myrecords is a function that accept myDf and myairport as arguments,
    and from all flights departing from myairport
    it returns a Series of the 20 most popular destination airports
    
    Arg:
        myDf(pd.DataFrame): The Data Frame that has the flight data 
                            corresponding to flights departing from myairport.
        myairport(str): The Origin airport that we are studying.      
        
    Returns:
        pd.Series: A Panda Series that contains 20 most popular destination airports.
    """
    return myDf[myDf['Origin']== myairport]['Dest'].value_counts().head(20)
    # do not forget to change the airport from 'IND' to my airport
    
myrecords(myDf,'IND' )


def takeoff(myDf: pd.DataFrame, myairlines: str)-> pd.Series:
    """
    takeoff is a function that accept myDf and myairlines as arguments,
    and for all flights departing myairlines
    it returns a Series of the 5 most popular departing airlines 
    
    Arg:
        myDf(pd.DataFrame): The Data Frame that has the flight data 
                            corresponding to flights departing myairlines .
        myairlines(str): The Origin airlines that we are studying.      
        
    Returns:
        pd.Series: A Panda Series that contains 5 most popular destination airlines.
    """
    return myDf[myDf['Origin']==myairlines]['UniqueCarrier'].value_counts().head(5)
    # do not forget to change the airport from 'IND' to myairport


takeoff(myDf,'IND')

# First import the data from Buffallo airport into a file

%%bash
head -n1 /anvil/projects/tdm/data/flights/subset/1987.csv >~/BUFflights.csv
grep -h ",BUF," /anvil/projects/tdm/data/flights/subset/*.csv >>~/BUFflights.csv

# Then read the data into a Pandas Data Frame

myDf=pd.read_csv('~/BUFflights.csv')

def myrecords(myDf: pd.DataFrame, myairport: str)-> pd.Series:
    """
    myrecords is a function that accept myDf and myairport as arguments,
    and from all flights departing from myairport
    it returns a Series of the 20 most popular destination airports
    
    Arg:
        myDf(pd.DataFrame): The Data Frame that has the flight data 
                            corresponding to flights departing from myairport.
        myairport(str): The Origin airport that we are studying.      
        
    Returns:
        pd.Series: A Panda Series that contains 20 most popular destination airports.
    """
    return myDf[myDf['Origin']== myairport]['Dest'].value_counts().head(20)
    # do not forget to change the airport from 'IND' to my airport
    
myrecords(myDf,'BUF' )

def takeoff(myDf: pd.DataFrame, myairlines: str)-> pd.Series:
    """
    takeoff is a function that accept myDf and myairlines as arguments,
    and for all flights departing myairlines
    it returns a Series of the 5 most popular departing airlines 
    
    Arg:
        myDf(pd.DataFrame): The Data Frame that has the flight data 
                            corresponding to flights departing myairlines .
        myairlines(str): The Origin airlines that we are studying.      
        
    Returns:
        pd.Series: A Panda Series that contains 5 most popular destination airlines.
    """
    return myDf[myDf['Origin']==myairlines]['UniqueCarrier'].value_counts().head(5)
    # do not forget to change the airport from 'IND' to myairport
    
    
# Then apply the function from question 3b

takeoff(myDf,'BUF')

# First import the data from Jacksonville (JAX) airport into a file

%%bash
head -n1 /anvil/projects/tdm/data/flights/subset/1987.csv >~/JAXflights.csv
grep -h ",JAX," /anvil/projects/tdm/data/flights/subset/*.csv >>~/JAXflights.csv

# Then read the data into a Pandas Data Frame

myDf=pd.read_csv('~/JAXflights.csv')


myrecords(myDf,'JAX' )


takeoff(myDf,'JAX')               
                 
