import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import re

"# -- coding: utf-8 --"

def calctime(a):
    return time.time()-a

positive=0
negative=0
compound=0

initime=time.time()

count=0
plt.ion()


ckey= 'qroXen6sDjQRRcl0Cn2Rl5JOi'
csecret='s6ZKFJxxRRUzcSJVItYeMlumoWAWSuDiJat7ZVhOcLjg2u7Hn5'
atoken='829709201681313793-9U8f63lyEQGCxJMbrZLEyHmsyjx5rBB'
asecret='jA71pbU4nypx6STJRLIgj5hIsxPz02oqtCHxVrO6tkCax'

class listener(StreamListener):
    
    def on_data(self,data):
        
        global initime

        t=int(calctime(initime))


        all_data=json.loads(data)
        tweet=all_data["text"]
        #username=all_data["user"]["screen_name"]
        tweet=" ".join(re.findall("[a-zA-Z]+", tweet))
        blob=TextBlob(tweet.strip())

        global positive
        global negative     
        global compound  
        global count
        
        count=count+1
        senti=0
        for sen in blob.sentences:
            senti=senti+sen.sentiment.polarity
            if sen.sentiment.polarity >= 0:
                positive=positive+sen.sentiment.polarity   
            else:
                negative=negative+sen.sentiment.polarity  
        compound=compound+senti        
        print (count)
        print (tweet.strip())
        print (senti)
        print (t)
        print (str(positive) + ' ' + str(negative) + ' ' + str(compound) )
        
    
        plt.axis([ 0, 70, -20,20])
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.plot([t],[positive],'go',[t] ,[negative],'ro',[t],[compound],'bo')
        plt.show()
        plt.pause(0.0001)
        if count==200:
            return False
        else:
            return True
        
    def on_error(self,status):
        print (status)


auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

searchTerm = input("Enter Keyword/Tag to search about: ")
NoOfTerms = int(input("Enter how many tweets to search: "))

twitterStream=  Stream(auth, listener(NoOfTerms))
twitterStream.filter(track=[searchTerm])
      
 