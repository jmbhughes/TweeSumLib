import os
corpus = "standwithpp_all.txt.pos.filtered"
cmd = "python ./src/Random.py ./data/{} ./results/Random.summ 15".format(corpus)
os.system(cmd)
cmd = "python ./src/MostRecent.py ./data/{} ./results/MostRecent.summ 15".format(corpus)
os.system(cmd)
cmd = "python ./src/SumBasic.py ./data/{} ./results/SumBasic.summ 15".format(corpus)
os.system(cmd)
cmd = "python ./src/Hybrid-TFIDF.py ./data/{} ./results/Hybrid-TFIDF.summ 15 true".format(corpus)
os.system(cmd)
cmd = "python ./src/TFIDF.py ./data/{} ./results/TFIDF.summ 15 true".format(corpus)
os.system(cmd)
