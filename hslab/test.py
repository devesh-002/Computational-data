import twint
import nest_asyncio

nest_asyncio.apply()

fetchedTweets = []
t = twint.Config()

t.Search = '#covid'
t.Limit = 100
t.Store_object = True

t.Store_object_tweets_list = fetchedTweets
t.Store_csv=True
t.Output= "test.csv"
twint.run.Search(t)

# print(fetchedTweets[0].tweet)