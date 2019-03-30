import tweepy
import time
#importing functions
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#tokens provided by the twitter API
ckey = 'FKIofCv16Ct93E3LhQGfRADk9'
csecret = 'eeWQXjuP88ovX2CAzxxZ7SKpsdKqdOFIVRDcpSPUwDrLEKYaec'
atoken = '2365425174-5KtFxyQSCp9NPvJoyXLXXZQyhJg6qWtBMxtypGX'
asecret = 'Q2BCdRYyIRq37xA1llOq9YkvhZajSgvaVFMIjGuj3pciL'

class listener(StreamListener):
    def on_data(self, data):
        try:
            #splitting the data to obtain the tweets only
            tweet = data.split(',"text":"')[1].split('","source')[0]
            print(tweet)
            #saving the tweets to a file with unix Timestmp
            savethis = str(time.time())+'::'+tweet
            saveFile = open('SavedTweets.csv', 'a')
            saveFile.write(savethis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            print('failed ondata', str(e))
            time.sleep(5)
    def on_error(self, status):
        print(status)
        
        
#sending twitter authentication information
auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['2015'])
            
