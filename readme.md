# TweeSumLib: Tweet Summarization Library for Python

This is a collection of summarization tools that have been somewhat optimized to run on tweets.  A python bound script is provided for easy running as well as some notes on each. Included here are the following algorithms:
* mead
* SumBasic
* TF-IDF
* Hybrid TF-IDF
* Opinosis
* Random
* MostRecent
     
## Getting Started

Because there are many different libraries, each must be addressed differently. In [startups](docs/startups/) you will find start up instructions for every library. Some of them require more library initialization than others.

For a general overview of the kinds of summarization this system can perform please check the [final report](docs/report/report.pdf).

Each algorithm, even if it is written originally in some other language, has a python binding. The running script can be found in [src][src/] with the appropriate ALGORITHM.py file. (The exception to this at the moment is mead. Mead must still be called from the bin directory in the mead library directory. This is because it has many more customizable features that would take more time to convey through a binding.)

## Example Summaries
Results can be found in the results directory. They are subdivided into the respective corpora. Filtered summarizations only draw from tweets labeled "with-reason" indicating they have a reason for their hashtag premise. 

## Authors

* **Marcus Hughes** - *Initial work* - [jmbhughes](https://github.com/jmbhughes)

## Acknowledgments
* TweeSumLib of the author's final project for CS 375 (Natural Language Processing) at Williams College.

