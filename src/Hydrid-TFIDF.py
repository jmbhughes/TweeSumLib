from tweet import *
import math, time, sys, os

MINIMUM_THRESHOLD = 12

class HTFIDF:
    ''' Hybrid TF-IDF is a summarization algorithm described by Sharifi, Hutton, Kalita in their paper "Experiments in Microblog Summarization
        It is a modification of TF-IDF such that when calculating term frequencies, the document is considered all tweets instead of just a single tweet (otherwise tf really doesn't matter with such short documents). 
    '''

    def __init__(self, tweet_collection):
        self.tweets = tweet_collection

    def normalizing_factor(self, tweet):
        return max(MINIMUM_THRESHOLD, tweet.length)

    def idf(self, word):
        ''' Inverse document frequency for a given word '''
        return self.tweets.word_count / len(self.tweets.word_locations[word])

    def tf(self, word):
        ''' term frequency over all documents for a given word '''
        return sum([self.tweets.collection[tweet].word_freq(word) for tweet in self.tweets.word_locations[word]])

    def weight_word(self, word):
        ''' The weight of a word under h-tfidf '''
        return self.tf(word) * math.log(self.idf(word), 2.0)

    def weight_tweet(self, tweet):
        ''' The weight of a tweet under h-tfidf '''
        return sum([self.weight_word(word) for word in tweet.clean_text.split()]) / self.normalizing_factor(tweet)

    def build_summary(self, length=5):
        ''' Generates a summary of specified length using the sumbasic algorithm 

            Parameters:
                length -- the number of tweets the summary should take 
        '''

        weights = [(tweet, self.weight_tweet(tweet)) for tweetid, tweet in self.tweets.collection.items()]
        weights = sorted(weights, key = lambda pair: pair[1])
        if len(weights) < length:
            return [tweet for tweet, weight in weights]
        else:
            return [tweet for tweet, weight in weights[-length:]]

def usage():
    string = "python SumBasic.py <path to tweets> <location to save> <length>\n\n"
    string += "the file of the tweets should be in jsonlist format\n"
    string += "summary length is the number of tweets\n"
    return string
    
if __name__ == "__main__":
    start_time = time.time()
    args = sys.argv[1:]
    if len(args) != 3:
        print(usage())
    else:
        print("Running Hybrid-TF-IDF summarizer with parameters:")
        print("\t input tweet corpus: ", args[0])
        print("\t output location: ", args[1])
        print("\t summary length: ", args[2])

    input_location, output_location, length = args[0], args[1], int(args[2])
    tweets = TweetCollection()
    tweets.add_from_file(input_location)
    summarizer = HTFIDF(tweets)
    summary = summarizer.build_summary(length)

    with open(output_location, "w") as summary_out:
        for tweet in summary:
            print(tweet.raw_text, file=summary_out)
    print("Finished in ", time.time() - start_time, " seconds")

