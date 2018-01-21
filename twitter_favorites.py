import tweepy

# generate this values at https://apps.twitter.com/
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

file_name = 'favs.txt'
item_delimiter = '========================\n'


def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    fav_file = open(file_name, "w")
    for fav_item in tweepy.Cursor(api.favorites).items():
        fav_file.write("{}\n".format(fav_item.text.encode('utf-8'))+item_delimiter)
    fav_file.close()


if __name__ == '__main__':
    main()
