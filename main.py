from twitterscraper import query_tweets
import datetime

def main():
    keyword = input("What words would you like to search for?\n")
    number = int(input("How many tweets would you like me to filter through?\n"))
    days= int(input("How many days of tweets would you like, counting backwards from today?\n(1 = just today. 2 = yesterday and today, etc.)\n"))

    now = datetime.datetime.now()
    if days == 1:
        date = "%20since%3A{}-{}-{}".format(now.year,now.month,now.day)
        query = keyword + date
    else:
        if int(now.day) - days > 0:
            date = '%20since%3A{}-{}-{}%20until%3A{}-{}-{}'.format(now.year,now.month,str(int(now.day-1)),now.year,now.month,now.day)
            query = keyword + date
        else:
            print("Sorry I can't go back that far... yet.")
    print('Working on it...')
    list_of_tweets = query_tweets(query, number)
    file = open("tweet_json.txt","w")
    for tweet in list_of_tweets:
        if int(tweet.likes) > 1:
            mystr = str(tweet.text.encode('utf-8'))
            file.write(mystr + '\n')
        elif int(tweet.retweets) > 1:
            mystr = str(tweet.text.encode('utf-8'))
            file.write(mystr + '\n')
        elif int(tweet.replies) > 1:
            mystr = str(tweet.text.encode('utf-8'))
            file.write(mystr + '\n')
    file.close()
    with open("tweet_json.txt","r") as f:
        print("Reading from file:\n")
        for line in f:
            print(line)

if __name__ == "__main__":
    main()
