''' In its original version, Opinosis requires Penn Treebank POS tags instead of Twitter POS tags. 
    To meet this request, I retag all the tweets using the NLTK POS tagger. This also formats for the correct 
    input Opinosis expects. 

    An alternative and arguably safer way (certainly quicker) would be to manually define a map of 
    Twitter POS tags to Penn Treebank POS tags. That may be added at a later time. 
'''


import sys, time, nltk
SRC_DIR = "/Users/mhughes/google_drive/codedungeon/tweet_summarization/src"
sys.path.append(SRC_DIR)
from tweet import *
from multiprocessing import Pool 


def usage():
    return "Usage: python twitterPOS_to_treebankPOS.py <input JSON list> <output location>"

def reformat(tweet):
    return " ".join([word + "/" + tag for word, tag in zip(tweet.clean_text.split(),[tag for word, tag in nltk.pos_tag(tweet.clean_text.split(" "))])])
        
if __name__ == "__main__":
    start_time = time.time()
    args = sys.argv[1:]
    if len(args) != 2:
        print(usage())
        exit()
    else:
        print("Converting twitter POS to treebank POS with:")
        print("\t input as", args[0])
        print("\t output as", args[1])

    # manage args
    input_jsonlist = args[0]
    output_location = args[1]
    
    # load tweets
    tweets = TweetCollection()
    tweets.add_from_file(input_jsonlist)

    # retag and format
    pool = Pool()
    results = pool.map(reformat, tweets.as_list())
    pool.close() 
    pool.join()

    # write out to text file
    with open(output_location, "w") as text_file:
        for tweet in results:
            print(tweet, file=text_file)
            print("",file=text_file)
    print("Finished in ", time.time() - start_time, " seconds")
