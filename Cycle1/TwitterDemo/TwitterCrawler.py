import twitter
import TwitterSearch

class TwitterCrawler(object):

	# Login to api
	def login(self):
		self.api = twitter.Api(consumer_key='684nljJUHfn6SCaYSCG0yAhbW',
						consumer_secret='mIRCyxLdIC5cQc7HukUtb7KhKqIvSYOB6LjBZb3CQOQ2n4ents',
						access_token_key='2805813624-2V4XKmbtM18s8osRDpSsr4H2An7JTpMdBE5N2la',
						access_token_secret='szChpRZhXg9F7n5gmlQhG2gEXe5C5g1vgYLGfqmeViPj8'
						)
		return self.api
	
	# Search
	def BasicSearch(self, query, db, scorer):
		self.query = query
		search = TwitterSearch.BasicTwitterSearch()
		return search.search(self.api, query, db, scorer)