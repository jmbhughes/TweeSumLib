from blist import sortedlist
from tweet import *
import sys, time

class SumBasic:
    def __init__(self, tweet_collection):
        self.tweets = tweet_collection
        self.word_probabilities = dict() #sortedlist(key = lambda x: -x[-1])
        self.tweet_probabilities = dict()

        # compute the word probabilities
        for word in self.tweets.words:
            self.word_probabilities[word] = self.tweets.word_probability(word) #.add((word, self.tweets.word_probability(word)))

        # compute the tweet probabilities
        for tweetid in self.tweets:
            self.tweet_probabilities[tweetid] = self.tweets.tweet_probability(tweetid)

    def build_summary(self, length=5):
        ''' Generates a summary of specified length using the sumbasic algorithm 

            Parameters:
                length -- the number of tweets the summary should take 
        '''
        summary = []

        while len(summary) < length:
            # while not long enough
            best_word = max([(word, self.word_probabilities[word]) for word in self.word_probabilities], key = lambda x: x[1])[0] # highest probability word
            
            best_tweet = max([(tweetid, self.tweet_probabilities[tweetid]) for tweetid in self.tweets.word_locations[best_word]], key = lambda x: x[1])[0] # highest probability tweet containing the highest probability word
            
            summary.append(self.tweets.collection[best_tweet])

            self.word_probabilities[best_word] *= self.word_probabilities[best_word]
            # decrease the probability of the highest probability word
            
            for tweetid in self.tweets.word_locations[best_word]:
                # update all tweet probabilities that contain the highest probability word 
                self.tweet_probabilities[tweetid] = self.tweets.tweet_probability(tweetid, self.word_probabilities)
                
        return summary

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
        print("Running SumBasic summarizer with parameters:")
        print("\t input tweet corpus: ", args[0])
        print("\t output location: ", args[1])
        print("\t summary length: ", args[2])

    input_location, output_location, length = args[0], args[1], int(args[2])
    tweets = TweetCollection()
    tweets.add_from_file(input_location)
    summarizer = SumBasic(tweets)
    summary = summarizer.build_summary(length)

    with open(output_location, "w") as summary_out:
        for tweet in summary:
            print(tweet.raw_text, file=summary_out)
    print("Finished in ", time.time() - start_time, " seconds")
