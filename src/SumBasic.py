from blist import sortedlist

class SumBasic:
    def __init__(self, tweet_collection):
        self.tweets = tweet_collection
        self.word_probabilities = dict() #sortedlist(key = lambda x: -x[-1])
        self.tweet_probabilities = dict()
        for word in self.tweets.words:
            self.word_probabilities[word] = self.tweets.word_probability(word) #.add((word, self.tweets.word_probability(word)))
        for tweetid in self.tweets:
            self.tweet_probabilities[tweetid] = self.tweets.tweet_probability(tweetid)
    def build_summary(self, length=5):
        summary = []
        while len(summary) < length:
            best_word = max([(word, self.word_probabilities[word]) for word in self.word_probabilities], key = lambda x: x[1])[0]
            print(best_word)
            best_tweet = max([(tweetid, self.tweet_probabilities[tweetid]) for tweetid in self.tweets.word_locations[best_word]], key = lambda x: x[1])[0]
            summary.append(self.tweets.collection[best_tweet])
            self.word_probabilities[best_word] *= self.word_probabilities[best_word]
            for tweetid in self.tweets.word_locations[best_word]:
                self.tweet_probabilities[tweetid] = self.tweets.tweet_probability(tweetid, self.word_probabilities)
        return summary
