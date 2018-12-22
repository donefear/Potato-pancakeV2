import ConfigParser
import twitter

############LOADING CONFIG FILES ##################
config = ConfigParser.ConfigParser()
config.read('Lib/API.cfg')
consumerkey = config.get("Twitter", 'consumer_key')
consumersecret = config.get("Twitter", 'consumer_secret')
accesstoken = config.get("Twitter", 'access_token')
accesstokensecret = config.get("Twitter", 'access_token_secret')
api = twitter.Api(consumer_key=[consumerkey],
                   consumer_secret=[consumersecret],
                   access_token_key=[accesstoken],
                   access_token_secret=[accesstokensecret])

def main(event):
    print ("twitter")

    message = 'test'
    status = api.PostUpdate(message)
    print("{0} just posted: {1}".format(status.user.name, status.text))
