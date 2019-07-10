from apps.api.twitter.client import TwitterClient
from textblob import TextBlob

class TweetSentiment:

	def __init__(self, client=None):

		try:
			self.client = TwitterClient()
		except:
			raise Exception("client not configured correctly")

	def parse_tweets(self, fetched_tweets):

		# empty list
		tweets = []

		for ft in fetched_tweets:
			parsed_tweet = {}

			parsed_tweet['text'] = ft['text']

			parsed_tweet['sentiment'] = self.get_tweet_sentiment(ft['text'])

			if ft['retweet_count'] > 0:
				# append retweets only once
				tweets.append(parsed_tweet) if parsed_tweet not in tweets else None
			else:
				tweets.append(parsed_tweet)

		return tweets

	def get_tweet_sentiment(self, tweet):

		analysis = TextBlob(self.client.clean_tweet(tweet))

		if analysis.sentiment.polarity > 0:
			return 'positive'

		elif analysis.sentiment.polarity == 0:
			return 'neutral'

		else:
			return 'negative'
