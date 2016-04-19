import twitter

api = twitter.Api(consumer_key="xxxxxx",
        consumer_secret="xxxxxx",
        access_token_key="xxxxxx",
        access_token_secret="xxxxxx"
        )

keywords = ["snow", "hello", "twitter"]

def main():
    for s in api.GetStreamFilter(track=keywords):
        try:
            print s['id']
            print s['created_at']
            print s['text']
        except:
            pass


if __name__ == '__main__':
    main()
