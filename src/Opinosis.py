from tweet import *
import sys, time, random, os
SRC_DIR = "/Users/mhughes/google_drive/codedungeon/tweet_summarization/src/"
OPINOSIS_DIR = "/Users/mhughes/google_drive/codedungeon/tweet_summarization/lib/OpinosisSummarizer-1.0/"
OPINOSIS_JAR = OPINOSIS_DIR + "opinosis.jar"

class Opinosis:
    def __init__(self, input_location, output_location, jar=OPINOSIS_JAR):
        self.tweets = None
        self.input_location = input_location
        self.output_location = output_location
        self.jar = jar
        
    def build_summary(self, length=5):
        ''' Generates a summary of specified length using the Opinosis algorithm 

            Parameters:
                length -- the number of tweets the summary should take 
        '''
        cmd = "cp -r {}tweets {}temp".format(OPINOSIS_DIR, OPINOSIS_DIR)
        os.system(cmd)
        cmd = "python {}twitterPOS_to_treebankPOS.py {} {}temp/input/temp.txt".format(SRC_DIR, self.input_location, OPINOSIS_DIR)
        os.system(cmd)
        os.chdir(OPINOSIS_DIR)
        cmd = "java -jar opinosis.jar -b temp"
        os.system(cmd)
        cmd = "cp {}temp/output/MyTestRun/temp.MyTestRun.system {}".format(OPINOSIS_DIR, self.output_location)
        os.system(cmd)
        cmd = "rm -r {}temp".format(OPINOSIS_DIR)
        os.system(cmd)

def usage():
    string = "python Opinosis.py <path to tweets> <location to save> <length>\n\n"
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
        print("Running Opinosis summarizer with parameters:")
        print("\t input tweet corpus: ", args[0])
        print("\t output location: ", args[1])
        print("\t summary length: ", args[2], "WARNING: this value means nothing now. It must be set in the opinosis config file")

    input_location, output_location, length = args[0], args[1], int(args[2])
    summarizer = Opinosis(input_location, output_location)
    summary = summarizer.build_summary(length)
    
    print("Finished in ", time.time() - start_time, " seconds")
