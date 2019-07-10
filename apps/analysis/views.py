from django.shortcuts import render

from apps.search.forms import SearchForm
from apps.analysis.sa import TweetSentiment
_ts = TweetSentiment()

def index(request):

	form = SearchForm()

	if request.method == 'POST':

		form = SearchForm(request.POST)

		context = {}

		if form.is_valid(): # do analysis

			query = form.cleaned_data['query']
			try:
				tweets = _ts.client.get_tweets(query=query)['statuses']
			except KeyError:
				tweets = []

			parsed = _ts.parse_tweets(tweets)

			ptweets = [tw['text'] for tw in parsed if tw['sentiment'] == 'positive']
			ntweets = [tw['text'] for tw in parsed if tw['sentiment'] == 'negative']
			netweets = [tw['text'] for tw in parsed if tw['sentiment'] == 'neutral']

			ptweets = (round(100*(len(ptweets)/len(parsed))),ptweets) if len(ptweets) > 0 else None
			ntweets = (round(100*(len(ntweets)/len(parsed))),ntweets) if len(ntweets) > 0 else None
			netweets = (round(100*(len(netweets)/len(parsed))),netweets) if len(netweets) > 0 else None

			
			context['ptweets'] = ptweets
			context['ntweets'] = ntweets
			context['netweets'] = netweets

		context['form'] = form

	return render(request, 'analysis/index.html', context)

