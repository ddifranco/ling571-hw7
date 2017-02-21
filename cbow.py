#!/usr/bin/python3

		# Modules & Settings

import sys
import pdb
import nltk
from gensim.models.word2vec import *
from scipy.stats.stats import spearmanr

wlen    = int(sys.argv[1])
human   = open(sys.argv[2], 'r')
output  = sys.argv[3]

			# Main 

punc = [',', '.', '?', '!', '$', '-', '/', '\\', '(', ')', ':', '"', '\'', '\'\'', '``', '--', ';'] 

print('Reading in Brown sentences... ')
sents =  list(nltk.corpus.brown.sents()) 
cleaned = [[word.lower() for word in sent if word not in punc] for sent in sents]

		#  Train model

print('Training word2vec model... ')
model = Word2Vec(cleaned,size=100,window=wlen,min_count=1,workers=1) 

		#  Evaluate against human judgements

humanJudgements = []
modelResults = []

for w1, w2, hsim in tuple([x.strip('\n').split(',') for x in human.readlines()]):

	msim = model.similarity(w1, w2)

	humanJudgements.append(hsim)
	modelResults.append(msim)

	print('{},{}:{}'.format(w1, w2, msim))

rho, pval = spearmanr(humanJudgements, modelResults)
print('Correlation:{}'.format(rho))
print('P-value:{}'.format(pval))
