
# coding: utf-8

# In[1]:

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
tweets=pd.read_csv("/Users/padhya/Documents/Python/My_Practice/Demonetization_Analysis/demonetization-tweets.csv",encoding = "ISO-8859-1")
tweets.head()


# In[7]:

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *

from nltk import tokenize
#If error while executing nltk then download import nltk nltk.download() and select all packages

sid = SentimentIntensityAnalyzer()

tweets['sentiment_compound_polarity']=tweets.text.apply(lambda x:sid.polarity_scores(x)['compound'])
tweets['sentiment_neutral']=tweets.text.apply(lambda x:sid.polarity_scores(x)['neu'])
tweets['sentiment_negative']=tweets.text.apply(lambda x:sid.polarity_scores(x)['neg'])
tweets['sentiment_pos']=tweets.text.apply(lambda x:sid.polarity_scores(x)['pos'])
tweets['sentiment_type']=''
tweets.loc[tweets.sentiment_compound_polarity>0,'sentiment_type']='POSITIVE'
tweets.loc[tweets.sentiment_compound_polarity==0,'sentiment_type']='NEUTRAL'
tweets.loc[tweets.sentiment_compound_polarity<0,'sentiment_type']='NEGATIVE'
tweets.head()


# In[19]:

tweets.sentiment_type.value_counts().plot(kind='bar',title="Sentiment Analysis")


# In[18]:

from ggplot import *
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.rcParams['figure.figsize'] = (6.0, 6.0)

tweets['hour'] = pd.DatetimeIndex(tweets['created']).hour
tweets['date'] = pd.DatetimeIndex(tweets['created']).date
tweets['minute'] = pd.DatetimeIndex(tweets['created']).minute
df=(tweets.groupby('hour',as_index=False).sentiment_compound_polarity.mean())
print(ggplot(aes(x='hour',y='sentiment_compound_polarity'),data=df)+geom_line())


# In[ ]:



