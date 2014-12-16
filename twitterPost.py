import twitter

def tweet():
    api = twitter.Api(consumer_key='yiGoImO08HPNmlndr8I5eJ1RV',
                          consumer_secret='oP5MkI0YqhsbTo8oT1tOjpiWGnhhGEptvZddpXjnHbZxKVUn3H',
                          access_token_key='2922352907-07W2oqOgnVfUIKVmo98xrpzPYqSUZfXX7uXEKwj',
                          access_token_secret='ZadXs4WmVQ85kmw4LjBV6bVARYoMfbbgiv0phL3nfVFLZ')

    #print api.VerifyCredentials()

    status = api.PostUpdate('blargh')

    print status.text

