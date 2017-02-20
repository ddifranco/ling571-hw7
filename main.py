#!/usr/bin/python3

		# Modules & Settings

import sys
import nltk
import pdb
import resources as rc
from scipy.stats.stats import spearmanr

wlen    = int(sys.argv[1])
wscheme = sys.argv[2].upper()
human   = open(sys.argv[3], 'r')
output  = sys.argv[4]

			# Main 

punc = [',', '.', '?', '!', '$', '-', '/', '\\', '(', ')', ':', '"', '\'', '\'\'', '``', '--', ';'] 

words, vocabSize, corpusSize = rc.prepareSample('fbrown', punc)
fx = rc.featureExtractor(vocabSize)
window = list()

		# Part 1: Generate Feature Matrix

for i, word in enumerate(words, 1):

	if i % 10000 == 1:
		print('Processing word {} of {}'.format(i, corpusSize))

	window.append(word)
	fx.increment(word)

	if len(window) >= (wlen * 2) + 1:
		fx.updateTally(window[wlen:wlen+1][0])
		fx.decrement(window.pop(0))

		# Part 2: Evaluate against human judgements

fx.setScheme(wscheme)
humanJudgements = []
modelResults = []

for w1, w2, sim in tuple([x.strip('\n').split(',') for x in human.readlines()]):

        fx.reportTop10(w1)
        fx.reportTop10(w2)
        cDist = fx.getCosineDistance(w1, w2)

        humanJudgements.append(sim)
        modelResults.append(cDist)

        print('{},{}:{}'.format(w1, w2, cDist))

rho, pval = spearmanr(humanJudgements, modelResults)
print('Correlation:{}'.format(rho))
print('P-value:{}'.format(pval))
