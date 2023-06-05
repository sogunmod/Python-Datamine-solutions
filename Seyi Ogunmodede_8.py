# I will be using 10 Cores for the yelp data
# I will use 20 GB of memory to read the data set

import pandas as pd

users = pd.read_parquet("/anvil/projects/tdm/data/yelp/data/parquet/users.parquet")

# reviews data frame takes longer time to load
reviews = pd.read_parquet("/anvil/projects/tdm/data/yelp/data/parquet/reviews.parquet")

# This help to display as many columns i have in the dataframes
pd.set_option('display.max_columns', None)

users.head()

reviews.head()

# Takes entries from the users Dataframe
# Where the user ID = "ntlvfPzc8eglqvk92iDIAw"
# Then get all of the data from the users dataframe
# then load the head

users[users["user_id"]== "ntlvfPzc8eglqvk92iDIAw"]. head()

# i am interested in the friends column
# Instead of looking for the head, i will go in and extract the friends' column
# it is like a list, happen to be index by 0

users[users["user_id"]== "ntlvfPzc8eglqvk92iDIAw"]['friends']

# let us do for other ID's

users[users["user_id"]== "xvu8G900tezTzbbfqmTKvA"]['friends'] 

# This will help me to get the list of friends out 
# this is wierd because we dont know the row number these people are on
# Regardless of the row in which they are on originally,
# in this new result here, They are just on a very zeroth row

users[users["user_id"]== "ntlvfPzc8eglqvk92iDIAw"]['friends'][0]

# This will help me to get the list of friends out 
# this is wierd because we dont know the row number these people are on
# Regardless of the row in which they are on originally,
# in this new result here, They are just on a very zeroth row

users[users["user_id"]== "xvu8G900tezTzbbfqmTKvA"]['friends'] [4]

# so you can go independently of where they are originally
# you can go in and use the indexing, instead of putting [0]
# You can put in .iLoc[0]
# That will go get the zeroth row of each of these results

users[users["user_id"]== "ntlvfPzc8eglqvk92iDIAw"]['friends'].iloc[0]

users[users["user_id"]== "xvu8G900tezTzbbfqmTKvA"]['friends'].iloc[0]

# then you want to take the friends and split them up
# with a comma and a space. That is split ", " in between each of them
    
users[users["user_id"]== "ntlvfPzc8eglqvk92iDIAw"]['friends'].iloc[0].split(", ")

users[users["user_id"]== "xvu8G900tezTzbbfqmTKvA"]['friends'].iloc[0].split(", ")

# then save the list of friends in a variable

mylistoffriends=users[users["user_id"]== "ntlvfPzc8eglqvk92iDIAw"]['friends'].iloc[0].split(", ")

mylistoffriends=users[users["user_id"]== "xvu8G900tezTzbbfqmTKvA"]['friends'].iloc[0].split(", ")

# go into the data frame and look for element of the users ID that are in this 
#  new list of friends that we just built.
# let find how many they were.
# This is the total for the new list of friends

users[users["user_id"].isin (mylistoffriends)].shape

# then you will now run for each to confirm what each has.

mylistoffriends=users[users["user_id"]== "ntlvfPzc8eglqvk92iDIAw"]['friends'].iloc[0].split(", ")

users[users["user_id"].isin (mylistoffriends)].shape

mylistoffriends=users[users["user_id"]== "xvu8G900tezTzbbfqmTKvA"]['friends'].iloc[0].split(", ")

users[users["user_id"].isin (mylistoffriends)].shape

def get_friends_friends_data (myuserid:str) ->pd.DataFrame:
    """
    get_friends_friends_data accepts myuserid and returns a Pandas DataFrame that contains the user information for myuserid 
    Arg:
       myuserid (str): The yelp user Id for which you want to get the friends data.
    Returns:
        pd.DataFrame:  A pandas DataFrame containing the user information for each friend of myuserid 
    """
    mylistoffriends=users[users["user_id"]==myuserid]['friends'].iloc[0].split(", ")
    return users[users["user_id"].isin (mylistoffriends)]

    # remember you are to return the entire dataframe not just the shape of the dataframe!
    
get_friends_friends_data("ntlvfPzc8eglqvk92iDIAw")

get_friends_friends_data("ntlvfPzc8eglqvk92iDIAw").shape

get_friends_friends_data("xvu8G900tezTzbbfqmTKvA")

get_friends_friends_data("xvu8G900tezTzbbfqmTKvA").shape

# Look at a particular business and find the average of the number of stars in it review

# Let us go into review DataFrame
# look at bussiness id = "-MhfebM0QIsKt87iDN-FNw"
# And get all of the reviews with those rows and look at the head
# Notice, business id is the same for all of them,
# but the number of stars will vary

reviews[reviews["business_id"]== "-MhfebM0QIsKt87iDN-FNw"].head()

# we can extract the stars

reviews[reviews["business_id"]== "-MhfebM0QIsKt87iDN-FNw"]["stars"].head()

# to look for the average of "-MhfebM0QIsKt87iDN-FNw"

reviews[reviews["business_id"]== "-MhfebM0QIsKt87iDN-FNw"]["stars"].mean()

reviews[reviews["business_id"]== "5JxlZaqCnk1MnbgRirs40Q"]["stars"].mean()

reviews[reviews["business_id"]== "VKVDDHKtsdrnigeIf9S8RA"]["stars"].mean()

# let us wrap it into a function

def calculate_avg_business_stars(mybusinessid: str) -> float:
    """
    calculate_avg_business_stars accepts mybusinessid and returns a floating point number that contains the average numbers of stars
    Arg:
       mybusinessid (str): The yelp business id for which you want to get the average numbers of stars in the reviews
    Returns:
       float: A floating point number that is the average numbers of stars in the reviews of the business
    """
    return reviews[reviews["business_id"]== mybusinessid]["stars"].mean()


calculate_avg_business_stars("-MhfebM0QIsKt87iDN-FNw")

calculate_avg_business_stars("5JxlZaqCnk1MnbgRirs40Q")

calculate_avg_business_stars("VKVDDHKtsdrnigeIf9S8RA")

reviews

# Another way to do it using groupby () function
# we could actually go find the average number of stars for all the businesses
# And then pull out the one we wanted

# go to reviews dataframes and group all the entries according to  business id
# then pull out the stars column, then take the mean
# for each business id this will generate the mean number of stars

reviews.groupby(["business_id"])["stars"].mean ().head()

# to look up specific business id

reviews.groupby(["business_id"])["stars"].mean()["-MhfebM0QIsKt87iDN-FNw"]

reviews.groupby(["business_id"])["stars"].mean()["5JxlZaqCnk1MnbgRirs40Q"]

reviews.groupby(["business_id"])["stars"].mean()["VKVDDHKtsdrnigeIf9S8RA"]

def calculate_avg_business_stars(mybusinessid: str) -> float:
    """
    calculate_avg_business_stars accepts mybusinessid and returns a floating point number that contains the average numbers of stars
    Arg:
       mybusinessid (str): The yelp business id for which you want to get the average numbers of stars in the reviews
    Returns:
       float: A floating point number that is the average numbers of stars in the reviews of the business
    """
    return reviews.groupby(["business_id"])["stars"].mean()[mybusinessid]

calculate_avg_business_stars("-MhfebM0QIsKt87iDN-FNw")

calculate_avg_business_stars("5JxlZaqCnk1MnbgRirs40Q")

calculate_avg_business_stars("VKVDDHKtsdrnigeIf9S8RA")

import matplotlib.pyplot as plt

mydf=reviews[reviews["business_id"]== "-MhfebM0QIsKt87iDN-FNw"]

mydf.shape

mydf.head()

# we want to go into the data frame for this data  "-MhfebM0QIsKt87iDN-FNw"
# then groupby whatever the date was, but only pull out the year from the date (.dt.year)
# then look at the stars data
# then take the mean

mydf.groupby(mydf["date"].dt.year)["stars"].mean()

# then we go plot the data for which we data in those years

plt.plot(mydf.groupby(mydf["date"].dt.year)["stars"].mean())

# For other two businesses

mydf=reviews[reviews["business_id"]== "5JxlZaqCnk1MnbgRirs40Q"]

plt.plot(mydf.groupby(mydf["date"].dt.year)["stars"].mean())

mydf=reviews[reviews["business_id"]== "VKVDDHKtsdrnigeIf9S8RA"]

plt.plot(mydf.groupby(mydf["date"].dt.year)["stars"].mean())

# we want to wrap our work into a function

def visualize_stars_over_time(mybusinessid: str) -> None:
    """
    visualize_stars_over_time accepts mybusinessid as an argumet and generates 
    a line plot showing the average number of stars in each year (for which the business has reviews)
    Arg:
       mybusinessid (str): The yelp business id
    Returns:
        None: This function does not return any value!  Instead, it draws the line plot
              for the average number of stars for the business during the year.
    """
    # make a data frame with the rows corresponding to mybusinessid
    mydf=reviews[reviews["business_id"]== mybusinessid]
    
    # Now group the data according to the dt.year of the date,
    # we extract the stars data and take a mean of the stars data in each year.
    
    plt.plot(mydf.groupby(mydf["date"].dt.year)["stars"].mean())
    return None

visualize_stars_over_time("-MhfebM0QIsKt87iDN-FNw")

visualize_stars_over_time("5JxlZaqCnk1MnbgRirs40Q")

visualize_stars_over_time("VKVDDHKtsdrnigeIf9S8RA")

def visualize_stars_over_time(mybusinessid: str, granularity: str = "years" ) -> None:
    """
    visualize_stars_over_time accepts mybusinessid as an argumet and generates 
    a line plot showing the average number of stars in each year or in each year-and-month pair (e.g., 2014 11 for Nov 2014)
    according to whatever we pass into the granularity argument ("years" or "months")
    Arg:
       mybusinessid (str): The yelp business id
       granularity (str): either "months" or "years" (it is years by default),
                          according to whether we want to see the plot by year or by month 
    Returns:
        None: This function does not return any value!  Instead, it draws the line plot
              for the average number of stars for the business during each year or during each set of year-and-month pairs .
    """
    # make a data frame with the rows corresponding to mybusinessid
    mydf=reviews[reviews["business_id"]== mybusinessid]
    
    if (granularity == "months"):
        # do something different here!
        # Now we are going to group the data according to the dt.year and the dt.month of the date,
        # Extract the stars data and take the mean of the stars data in each year-and-month pair
        plt.plot(mydf.groupby([mydf["date"].dt.year,mydf["date"].dt.month])["stars"].mean().reset_index(drop=True))
        
    else:  
    
        # Now group the data according to the dt.year of the date,
        # we extract the stars data and take a mean of the stars data in each year.
    
        plt.plot(mydf.groupby(mydf["date"].dt.year)["stars"].mean())
    return None

visualize_stars_over_time("-MhfebM0QIsKt87iDN-FNw")

# This is plot by year
visualize_stars_over_time("-MhfebM0QIsKt87iDN-FNw","years")

# This is plot by months, it look similar but clumsy

visualize_stars_over_time("-MhfebM0QIsKt87iDN-FNw","months")

visualize_stars_over_time("5JxlZaqCnk1MnbgRirs40Q")

visualize_stars_over_time("5JxlZaqCnk1MnbgRirs40Q", "years")

visualize_stars_over_time("5JxlZaqCnk1MnbgRirs40Q", "months")

visualize_stars_over_time("VKVDDHKtsdrnigeIf9S8RA")

visualize_stars_over_time("VKVDDHKtsdrnigeIf9S8RA", "years")

visualize_stars_over_time("VKVDDHKtsdrnigeIf9S8RA", "months")

# To add ability to make plot for several businesses all at once
# the * represent that we can put as many arguments as we like there 

def visualize_stars_over_time(*allofmybusinessids) -> None:
    """
    visualize_stars_over_time accepts as many business ids as we like (in allofmybusinessids) and generates 
    a line plot showing the average number of stars in each year 
    Arg:
       allofmybusinessids: As many argument as we like, each one corresponding to a yelp business id
       
    Returns:
        None: This function does not return any value!  Instead, it draws the line plot
              for the average number of stars for the businesses in all allofmybusinessids during each year.
    """
    for mybusinessid in allofmybusinessids:
        
        # make a data frame with the rows corresponding to mybusinessid
        mydf=reviews[reviews["business_id"]== mybusinessid]
    
 
        # Now group the data according to the dt.year of the date,
        # we extract the stars data and take a mean of the stars data in each year.
    
        plt.plot(mydf.groupby(mydf["date"].dt.year)["stars"].mean())
    plt.show()
    return None

visualize_stars_over_time("-MhfebM0QIsKt87iDN-FNw", "5JxlZaqCnk1MnbgRirs40Q","VKVDDHKtsdrnigeIf9S8RA" )