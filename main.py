#!/bin/python3.4

	# Modules & Settings

import sys
import resources
import nltk
import pdb
import resources as rc

wlen    = int(sys.argv[1])
wscheme = sys.argv[2].upper()
human   = open(sys.argv[3], 'r')
output  = open(sys.argv[4], 'w')

	# Main

with open('gettysburg.txt', 'r') as myfile:
    speech=myfile.read().replace('\n', ' ')
#tkns = nltk.tokenize.word_tokenize(speech)[0:33]
tkns = nltk.tokenize.word_tokenize(speech)
words = iter(tkns)

fx = rc.featureExtractor()
window = list()

while words.__length_hint__() > 0:

	word = words.__next__()
	clean = rc.preprocess(word)

	if clean is None:
		continue

	window.append(clean)
	fx.increment(clean)
	print(window)

	if len(window) >= (wlen * 2) + 1:
		fx.updateTally(window[wlen:wlen+1][0])
		fx.decrement(window.pop(0))

fx.report()
fx.save('test')
