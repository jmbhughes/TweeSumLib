import math

class TFIDF:
    def __init__(self, tweet_collection):
        self.tweets = tweet_collection


    def normalizing_factor(self, tweet):
        return max(MINIMUM_THRESHOLD, len(tweet))

    def idf(self, word):
        return self.tweets.word_count / len(self.tweets.word_locations[word])

    def tf(self, word):
        return sum([tweet.word_freq(word) for tweet in self.tweets.word_locations[word]])

    def weight_word(self, word):
        return tf(word) * math.log(idf(word), 2.0)

    def weight_tweet(self, tweet):
        return sum([self.weight_word(word) for word in tweet.clean_text.split()]) / normalizing_factor(tweet)
