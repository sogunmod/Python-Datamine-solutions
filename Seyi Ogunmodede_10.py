# Bar chart can be stacked or grouped. 
# This involves three varibles to be compared together. 
# It must have discrete value to enable ploting
# Colour coding (hue) good for distinguishing data from various groups
# Histogram shows the distribution of a set of Data
# To draw a histogram, the data are grouped into bins or intervals
# Visualisation provides insight that canot be appreciated 
# by any other approach to learning from data.
# A large amount of quantitative information can be packed into a small region.


import pandas as pd

pd.read_csv("/anvil/projects/tdm/data/beer/beers.csv")

mybeer=pd.read_csv("/anvil/projects/tdm/data/beer/beers.csv")

mybeer.head()

mybeer.tail()

mybeer.columns

# 1. considering the country, style and their respictive occurrence using bar chart

# 2. looking at the retired column to the abv column using box plot. Also, Abv to availability

# 3. Using group by to relate availability to those that have retired using Stacked bar and grouped bar

import pandas as pd

pd.read_csv("/anvil/projects/tdm/data/beer/beers.csv")

mydf=pd.read_csv("/anvil/projects/tdm/data/beer/beers.csv")

mydf.head()

mydf=mydf.rename(columns={"country":"country_code"})

import pycountry

mydf.head()

# Extract the fisrt 5 conutry code

mydf.head()["country_code"]

mydf.head(20)["country_code"]

# To get the countries full names
# Diverse info will pop up 


pycountry.countries.get(alpha_2="US")

# we can just get the name alone

pycountry.countries.get(alpha_2="US").name

pycountry.countries.get(alpha_2="NO").name

pycountry.countries.get(alpha_2="JP").name

pycountry.countries.get(alpha_2="IT").name

# Then we can go through all of the countries in the head of the country code column
# To pull out what those codes are

[mycountry for mycountry in mydf.head()["country_code"]]

#Then instead of printing the contry itself,
# we can just use the techniques from above
# That is the first five full country names

[pycountry.countries.get(alpha_2=mycountry).name for mycountry in mydf.head()["country_code"]]

# let us look for the first 30 country full names
# you can do it for number 50, 100,200

[pycountry.countries.get(alpha_2=mycountry).name for mycountry in mydf.head(30)["country_code"]]

# But if you do it for 201 there will be an error

[pycountry.countries.get(alpha_2=mycountry).name for mycountry in mydf.head(201)["country_code"]]

# Let us look at our first 201 DataFrame
# for 201st row there is an NAN on the country code
# Then we need to go in and get rid of the NAN in just the country code
# You don"t want to get rid of them together because,
# contry that are not US we have an NAN in their state

mydf.head(201)

# But the NAN in the country code we want to drop them
# And keep track of the numbers we are dropping

mydf.shape

# There are 358873 rows all together.

# look at the country code columns to see how many are NAs
#There are 154 that are NAs
# we are only going to loose 154 entries if we drop the ones that are NAs

sum(mydf["country_code"].isna())

# Make a new DataFrame where we throw away those that were Nas 
# The syntax code mydf["country_code"].isna() means finding the ones that were NAs
# ~mydf["country_code"].isna() means let get those that are not NAs
# the output are for those that are not NAs

mynewdf = mydf[~mydf["country_code"].isna()]

# The shape of our new DataFrame
# It is almost thesame as the shape of our old DataFrame

mynewdf.shape

# we will go back to our code above
# we will now use our new DataFrame
# it gives me all of the country names for all of the rows in my new data frame

[pycountry.countries.get(alpha_2=mycountry).name for mycountry in mynewdf["country_code"]]

# I will take my new DataFrame and add a column call contry_name  

mynewdf["country_name"]=[pycountry.countries.get(alpha_2=mycountry).name for mycountry in mynewdf["country_code"]]

mynewdf.head(20)

mybeer['country'].value_counts()

mybeerct=mybeer['country'].value_counts()

# reset_index() help in generating an indexing for my counts
#Then i created a column for counts

mybeerct=mybeerct.reset_index()

mybeerct.columns=['country', 'counts']

mybeerct

mybeerct=mybeer['country'].value_counts()

mybeerct.loc[mybeerct["counts"]>1000]

jkbeer=mybeerct.loc[mybeerct["counts"]>1000]

jkbeer.plot(kind="bar",x="country",y="counts")


mybeer['style'].value_counts()

mybeerct=mybeer['style'].value_counts()

mybeerct=mybeerct.reset_index()

mybeerct.columns=['style', 'counts']

mybeerct

mybeer.groupby(['style']).mean()       

dfmybeer=mybeer.groupby(['style']).mean().reset_index()

dfmybeer.plot(kind="bar", x="style", y = "abv")

dfmybeer.plot(kind="bar", x="style", y = "abv", figsize=(20,4))

dfmybeer.loc[dfmybeer["abv"]>8]

ftmybeer=dfmybeer.loc[dfmybeer["abv"]>8]

ftmybeer.plot(kind="bar", x="style", y = "abv")

mybeer.plot.box(column="abv", by="retired", figsize=(10, 8))

mybeer.plot.box(column="abv", by='availability', figsize=(10, 8), rot=90)

mybeer.groupby(['availability','retired'])

mybeer.groupby(['availability','retired']).size()

mybeer.groupby(['availability','retired']).size().unstack().plot(kind='bar', stacked=True)

mybeer.groupby(['availability','retired']).size().unstack().plot(kind='bar', stacked=False)