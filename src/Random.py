from tweet import *
import sys, time, random

class Random:
    def __init__(self, tweet_collection):
        self.tweets = tweet_collection.as_list()

    def build_summary(self, length=5):
        ''' Generates a summary of specified length using the Random algorithm 

            Parameters:
                length -- the number of tweets the summary should take 
        '''
        return random.sample(self.tweets, length)

def usage():
    string = "python Random.py <path to tweets> <location to save> <length>\n\n"
    string += "the file of the tweets should be in jsonlist format\n"
    string += "summary length is the number of tweets\n"
    return string
    
if __name__ == "__main__":
    start_time = time.time()
    args = sys.argv[1:]
    if len(args) != 3:
        print(usage())
        exit()
    else:
        print("Running Random summarizer with parameters:")
        print("\t input tweet corpus: ", args[0])
        print("\t output location: ", args[1])
        print("\t summary length: ", args[2])

    input_location, output_location, length = args[0], args[1], int(args[2])
    tweets = TweetCollection()
    tweets.add_from_file(input_location)
    summarizer = Random(tweets)
    summary = summarizer.build_summary(length)
    print(len(summary))
    with open(output_location, "w") as summary_out:
        for tweet in summary:
            print(tweet.raw_text, file=summary_out)

    print("Finished in ", time.time() - start_time, " seconds")
