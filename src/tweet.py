import json
from dateutil import parser as dateparser

class Tweet:
    def __init__(self, json_tweet):
        self.clean_text = json_tweet['text']
        self.raw_text = json_tweet['unmodified_text']
        self.category = json_tweet['label']
        self.is_quote = json_tweet['is_quote_status']
        self.reply_id = json_tweet['in_reply_to_status_id']
        self.reply_user = json_tweet['in_reply_to_user_id']
        self.conf = [float(num) for num in json_tweet['conf'].split()]
        self.idnum = json_tweet['id']
        self.date = dateparser.parse(json_tweet['created_at'])
        self.pos = json_tweet['pos'].split()

class TweetCollection:
    def __init__(self, tweets=[]):
        self.collection = dict()
        self.words = []
        self.word_frequencies = dict()
        self.word_locations = dict()
        self.word_count = 0
        for tweet in tweets:
            self.add_tweet(tweet)

    def __iter__(self):
        return self.collection.__iter__()

    def add_tweet(self, tweet):
        #Build the frequency chart for word frequency
        for word in tweet.clean_text.split():
            self.word_count += 1
            if word in self.word_frequencies:
                self.word_frequencies[word] += 1
                self.word_locations[word] += [tweet.idnum]
            else:
                self.word_frequencies[word] = 1
                self.word_locations[word] = [tweet.idnum]
                self.words.append(word)
        self.collection[tweet.idnum] = tweet
        
    def word_probability(self, word):
        if word in self.words:
            return self.word_frequencies[word] / self.word_count
        else:
            return 0

    def tweet_probability(self, tweet_id, word_probabilities = None):
        tweet = self.collection[tweet_id]
        probability = 1
        if word_probabilities: #if a dict of word probabilities is given
            for word in tweet.clean_text.split():
                probability *= word_probabilities[word]
        else: #no word probabilities given, so calculate on the fly
            for word in tweet.clean_text.split():
                probability *= self.word_probability(word)
        return probability / len(tweet.clean_text.split())

    def add_from_file(self, file_path):
        ''' Assumes that the file is formatted so that each line is a json entry'''
        with open(file_path) as file:
            lines = file.readlines()
        tweets = [Tweet(json.loads(line)) for line in lines]
        for tweet in tweets:
            self.add_tweet(tweet)        
        
