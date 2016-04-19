import twitter
import pprint

api = twitter.Api(consumer_key="xxxxxx",
        consumer_secret="xxxxxx",
        access_token_key="xxxxxx",
        access_token_secret="xxxxxx"
        )

USERS = ["clozed2u", "teamofz"]

def main():
    for t in api.GetStreamFilter(follow=USERS):
        try:
            print t['id']
            print t['created_at']
            print t['text']
        except:
            pass


if __name__ == '__main__':
    main()
