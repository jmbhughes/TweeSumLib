import json

def load_tweets(file_path):
    ''' Assumes that the file is formatted so that each line is a json entry'''
    with open(file_path) as file:
        lines = file.readlines()
    tweets = [json.loads(line) for line in lines]
    return tweets





