from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'efUkt179xuc7VYzS6gQEK2e5q'
csecret = 'JhZrWrsnotivRjLlhLPNGv1EsZrrBVSEG5Vnvnopc9yBtW0XIO'
atoken = '183782682-p5m04KkzmZ0ffj2JxlJ369S6Xith7nJ8CMgi0J1W'
asecret = 'aGdLW63aNiCmoLW94ibOStC3I2nPDSaZuZIPqEvOAVZid'

class listener(StreamListener):
    def on_data(self, data):
        print data
    	return True 

    def on_error(self, status):
	print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
