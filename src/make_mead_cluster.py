MEAD_DIR = "/Users/mhughes/google_drive/codedungeon/tweet_summarization/lib/mead-3.10/"
from tweet import *
import sys, os, time


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        print(usage())
    else:
        print("Building mead cluster with parameters:")
        print("\t input tweets: ", args[0])
        print("\t output directory: ", args[1])

        input_file, output_dir = args[0], args[1]

        #cmd = "export PERL5LIB=$PATH:{}bin/addons/formatting".format(MEAD_DIR)
        #os.system(cmd)
        
        tweets = TweetCollection()
        tweets.add_from_file(input_file)

        cmd = "cp -r {}data/blank {}data/".format(MEAD_DIR, MEAD_DIR) + output_dir
        os.system(cmd)

        cmd = "mv {}data/{}/blank.cluster {}/data/{}/{}.cluster".format(MEAD_DIR, output_dir, MEAD_DIR, output_dir, output_dir)
        os.system(cmd)

        with open(MEAD_DIR + "data/" +  output_dir + "/docsent/1", "w") as text_file:
            for tweetid, tweet in tweets.collection.items():
                print(tweet.clean_text, "~~~", file=text_file)

        cmd = "cd {}bin/addons/formatting".format(MEAD_DIR)
        os.system(cmd)
        
        cmd = "perl text2cluster.pl {}data/{}/docsent/1 ~~~".format(MEAD_DIR, output_dir)
        os.system(cmd)
