import pandas as pd

products = pd.read_csv("/anvil/projects/tdm/data/icecream/products.csv")

reviews = pd.read_csv("/anvil/projects/tdm/data/icecream/reviews.csv")

# Let us look at the sizes of the dataset
# 57 - rows with 7 - columns

products.shape

# reviews is very large
# 21674 - rows with 13 - columns

reviews.shape

# To know the columns names for reviews
# They are wrapped inside a list and index there

reviews.columns

# To get up a column names themselves

reviews.columns.values

# you can put it to a list if you want

list(reviews.columns.values)

# To know the columns names for products

products.columns

list(products.columns.values)

# Notice that both DataFrames have a key column and an ingredient column in common

# Let us look at their heads

reviews.head()

products.head()

# indeed every products seem to have a unique key and does not seem to have a unique sets of ingredients
# The are lot of diferences in the ingredient, the key is the right thing to match on,
# if we have to merge the two DataFrames together.
# we want to match on common columns and not ones that has NAs in them.

# This is the merge DataFrame
# i will call my merged DataFrame, joinDF.
# i will merge the reviews and the products on the column called key

joinDF = pd.merge(reviews, products, on='key')

# Let us take a look at the new DataFrame (joinDF)
# it won't have quite as many rows as review, it only got 7943
# This is because there might be some keys there were not in the products dataframe 
# but were found in the reviews 

joinDF.shape

# There are smaller number of rows in joinDF than in reviews
# likely, there are some key values in reviews that are not in products
# Also, joinDF has 19 columns; reviews has 13 columns and products has 7 columns
# So, we basically preserved all of the columns but did not duplicate the column called 'key'.

joinDF.head()

# if you look at the merged  DataFrame, it only has one column for key
# while for ingredient, it has 'ingredients_x' column which is for 'reviews' 
# and 'ingredients_y' column which is for 'products'

# Another way to merge data frames
# first keeping all of the rows from reviews 

pd.merge(reviews, products, on='key').shape

# How did we actially did that? it is through inner join
# So it will keep track of therows that were containing the key in both DataFrames

pd.merge(reviews, products, on='key', how = 'inner').shape
# This is basically what I did before

# For instance if we decided to do left join
# It will give me one row for every rows in reviews
# It will respect the number of rows from the DataFrame on the left here "reviews"

revDF = pd.merge(reviews, products, on='key', how = 'left')

# It got the same number of rows as we did earlier

revDF.shape

# Here is another way to do it (but it preferable, to do the first way)

# For this new DataFrame (joinDF) looking at the head

# For ingredient, it has 'ingredients_x' column which has all the contents from'reviews' 
# and 'ingredients_y' column which has all the contents from'products'

joinDF.head()

# What happens and why if you tried to merge the dataframes on the column ingredients?
# It gives an error

tryDF = pd.merge(reviews, products, on='ingredients')

# What should we do instead, if we want to merge on ingredients?
# We have to adjust what is in the two columns
# We have to go look at what is in the ingredient column from the reviews dataframe
# what is in the ingredient column from the products dataframe
# And try to make them match

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
from wordcloud import STOPWORDS

import nltk
from nltk.probability import FreqDist

STOPWORDS

# This is for the first entry

products.ingredients[0]

# To ensure everythinh is in lower case

products.ingredients[0].lower()

# After which , i will split
# Then we can do a bunch of different words.

products.ingredients[0].lower().split()

# First save the list of the split words'products.ingredients[0].lower().split()' as mywords
# Then for all the word in 'mywords', if the word is not in 'STOPWORDS',
# I will take the list of all those words and call up 'myfilteredwords'
# Then i will join it back together with a space and it will be my 'onefilteredreview'

mywords = products.ingredients[0].lower().split()
myfilteredwords=[word for word in mywords if word not in STOPWORDS]
onefilteredreview=' '.join(myfilteredwords) 

onefilteredreview

# I will make an empty list 
myfilteredreviews=[]

for myreview in  products.ingredients:
    mywords=myreview.lower().split()
    myfilteredwords=[word for word in mywords if word not in STOPWORDS]
    onefilteredreview=' '.join(myfilteredwords)
    myfilteredreviews.append(onefilteredreview)
    
# This is the first five of them

myfilteredreviews[0:5]

# Now i want to join all of those together, into one very large string
# I call it 'myhugestring' 

myhugestring = ' '.join(myfilteredreviews)

# Then i want to make a wordcloud

wordcloud=WordCloud(width=800, height=800, background_color='pink', min_font_size=10).generate(myhugestring)

# Then i display it

plt.figure(figsize=(8,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show

# since the word 'sugar' appears twice
# Then to eliminate, i will 

from collections import Counter

# Then look for the top 20 words there

mycounts=Counter(myhugestring.lower().split())

mycounts.most_common(20)

# Load the image mask

icecream_mask = np.array(Image.open('/anvil/projects/tdm/data/icecream/icecream.png'))

# Extract the text to use for the word cloud
# No need to run this because my text has been generated for me using 'myhugestring'

### text = " ".join(str(each) for each in df.columnname)

# Create a WordCloud object with the mask
wordcloud = WordCloud(max_words=200, colormap='Set1', background_color="orange", mask=icecream_mask).generate(myhugestring)

# Display the word cloud on top of the image
fig, ax = plt.subplots(figsize=(8, 6))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis('off')

plt.show()