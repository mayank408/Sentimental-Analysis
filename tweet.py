from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

ckey="qroXen6sDjQRRcl0Cn2Rl5JOi"
csecret="s6ZKFJxxRRUzcSJVItYeMlumoWAWSuDiJat7ZVhOcLjg2u7Hn5"
atoken="829709201681313793-9U8f63lyEQGCxJMbrZLEyHmsyjx5rBB"
asecret="jA71pbU4nypx6STJRLIgj5hIsxPz02oqtCHxVrO6tkCax"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]

        print(tweet)
        
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])