import pandas as pd

finefood = pd.read_csv("/anvil/projects/tdm/data/amazon/amazon_fine_food_reviews.csv")

finefood.head()

# from the data,HelpfulnessNumerator and HelpfulnessDenominator seems to have values either equals to each other, 
# or not always equal and HelpfulnessNumerator is never larger than HelpfulnessDenominator.    
# HelpfulnessNumerator seems to be number of people who rated the review to be helpful.
# HelpfulnessDenominator seems to be total number of people who rated the review whether or not they found it to be helpful

# what is the user id of review number 23789?
# You can use iloc to locate the location

finefood.iloc[23789]

finefood.iloc[23788]

# How many duplicate ProfileName values are there?

# checking with first five for duplication

finefood.ProfileName.duplicated().head()
# They are not.

# remember that when we sum False and True values, False become zero True becomes 1,
# so we could just sum() to get the number of true values

finefood.ProfileName.duplicated().sum()

#for a histogram
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
%matplotlib inline
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px

fig = px.histogram(finefood, x="Score")
fig.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='product rating')
fig.show()


#for a histogram
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
%matplotlib inline
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px

fig = px.histogram(finefood, x="ProductId")
fig.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='product Info' )
fig.show()

#for a histogram
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
%matplotlib inline
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px

fig = px.histogram(finefood, x="Time")
fig.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='timing' )
fig.show()


#for a piechart
import matplotlib.pyplot as plt
rating_counts = finefood["Score"].value_counts()

rating_counts 

plt.pie(rating_counts, labels=rating_counts.index)
plt.title("product rating")
plt.show()

#for a piechart
import matplotlib.pyplot as plt
rating_counts = finefood["HelpfulnessDenominator"].value_counts()

rating_counts

plt.pie(rating_counts, labels=rating_counts.index)
plt.title("Denominator")
plt.show()

#for a piechart
import matplotlib.pyplot as plt
rating_counts = finefood["HelpfulnessNumerator"].value_counts()

plt.pie(rating_counts, labels=rating_counts.index)
plt.title("Numerator")
plt.show()

# Histogram and pie chart visualisation was use for the score data
# They were chosen because they are numerical data
# For the score there rae lot of people that score 5, then follow by 4,1,3,2 and there were no zero.

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

mystopwords=stopwords.words('english') + ["br", "href","b","r"]

finefood.Text[0]

# i can first put it in lower case
# everything will be in lower case all through

finefood.Text[0].lower()

# then i can split it into list of individual words

mywords=finefood.Text[0].lower().split()

# for words in my words, if the words is not in mystopwords from up, i want to print that word

myfilteredwords=[word for word in mywords if word not in mystopwords ]

# then i will join them together again

onefilteredreview=' '.join(myfilteredwords)

onefilteredreview

myfilteredreviews=[]

# now we want to go do this for all of our reviews

for myreview in finefood.Text:
    mywords=myreview.lower().split()
    myfilteredwords=[word for word in mywords if word not in mystopwords]
    onefilteredreview=' '.join(myfilteredwords)
    myfilteredreviews.append(onefilteredreview)
    
myfilteredreviews[0]

# seeing from zero through 5

myfilteredreviews[0:5]

# I will make one huge string by joining everything together in myfilteredreviews by spaces

myhugestring=' '.join(myfilteredreviews)

import matplotlib.pyplot as plt
from wordcloud import WordCloud

# then build a world cloud and generate them from our hugestring

wordcloud=WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(myhugestring)

plt.figure(figsize=(8,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show

from collections import Counter

mycounts=Counter(myhugestring.lower().split())

mycounts.most_common(20)

mystopwords=stopwords.words('english') + ["br", "href","b","r",'/><br','like','product']

for myreview in finefood.Text:
    mywords=myreview.lower().split()
    myfilteredwords=[word for word in mywords if word not in mystopwords]
    onefilteredreview=' '.join(myfilteredwords)
    myfilteredreviews.append(onefilteredreview)
    
myhugestring=' '.join(myfilteredreviews)

wordcloud=WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(myhugestring)

plt.figure(figsize=(8,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show