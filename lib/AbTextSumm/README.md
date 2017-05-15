<h1 align=center>AbTextSumm</h1>
Abstractive Summarization: Code of the ILP-based algorithm as described in the IJCAI paper

Please note that this code only tackles the summarization component and not the clustering part. 
The code takes a list of sentences, or a paragraph and produces an extractive or abstractive summary driven by the parameter "mode".

For language model (only required for abstractive summarization):
Needs kenlm: https://kheafield.com/code/kenlm/ [See how to install]
Use any available ARPA format language model and convert to kenlm format as binary. KENLM is really fast. 

Other several packages required: PuLP for optimization, sklearn, nltk, cpattern, igraph
Best option is to use Anaconda package. All the above mentioned packages can be installed using pip.
To install dependencies, use:
```
pip install - r requirements.txt
```
in the root folder of the project. 

A major part of the word graph generation code has been taken from https://github.com/boudinfl/takahe.

The main program is in txtsumm/Example.py.
Given a passage, it can generate a summary using the following code:
```
  list_Sentences=segmentize(passage)
  generateSummaries(list_Sentences, mode="Extractive")
```
Changing the mode = "Extractive" to:
```
mode="Abstractive"
```
will run Abstractive summarization with TextRank as the default ranking parameter. However, it requires a language model described earlier. By default, this code runs abstractive summarization. You can also use the length parameter (in words) to control length of the output summary. For example:

```
generateSummaries(list_Sentences, mode="Extractive", length=50)
```


**If you use the code here, please cite this paper:**

Siddhartha Banerjee, Prasenjit Mitra, and Kazunari Sugiyama. _"Multi-Document Abstractive Summarization Using ILP based Multi-Sentence Compression."_ Proceedings of the 24th International Joint Conference on Artificial Intelligence (IJCAI 2015), Buenos Aires, Argentina. 2015.
