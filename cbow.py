#!/usr/bin/python3

		# Modules & Settings
#import cbow
import sys
import resources as rc

wlen    = int(sys.argv[1])
human   = open(sys.argv[2], 'r')
output  = sys.argv[3]

			# Main 

punc = [',', '.', '?', '!', '$', '-', '/', '\\', '(', ')', ':', '"', '\'', '\'\'', '``', '--', ';'] 

words, vocabSize, corpusSize = rc.prepareSample('fgetty', punc)

		# Part 1: Build Model

sys.exit(0)

		# Part 2: Evaluate against human judgements

humanJudgements = []
modelResults = []

for w1, w2, sim in tuple([x.strip('\n').split(',') for x in human.readlines()]):
	pass

rho, pval = spearmanr(humanJudgements, modelResults)
print('Correlation:{}'.format(rho))
print('P-value:{}'.format(pval))
