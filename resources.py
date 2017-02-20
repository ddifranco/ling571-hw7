#!/bin/bash/python3.5

import sys
import numpy as np
import structs as st
import pickle
import pdb
import nltk
import scipy.spatial
import gc

def prepareSample(sample, punc): 

	validSamples = ['sgetty', 'fgetty', 'sbrown', 'mbrown', 'fbrown']

	if sample not in validSamples:
		sys.stdout.write('Sorry, "{}" is not a valid sample.'.format(sample))
		sys.exit(0)

	if sample in ['sgetty', 'fgetty']:
		with open('gettysburg.txt', 'r') as myfile:
		    speech=myfile.read().replace('\n', ' ') 
		if sample == 'sgetty':
			words = nltk.tokenize.word_tokenize(speech)[0:33]
		else:
			words = nltk.tokenize.word_tokenize(speech)

	if sample in ['sbrown', 'mbrown', 'fbrown']:
		if sample == 'sbrown':
			words = list(nltk.corpus.brown.words())[0:25000]
		if sample == 'mbrown': words = list(nltk.corpus.brown.words())[0:100000]
		if sample == 'fbrown':
			words = list(nltk.corpus.brown.words())

	cleaned = [preprocess(x, punc) for x in words]
	
	return cleaned, len(set(cleaned)), len(cleaned)

def preprocess(raw, punc):

	if raw in punc:
		return None

	return raw.lower()

def memoizePPMIterms(iArray):

	print('Memoizing reusable terms')

	sum_ij = np.sum(iArray)		#Sum of matrix
	sum_i  = np.sum(iArray, 0)	#Vector of rowsums
	sum_j  = np.sum(iArray, 1)	#Vector of colsums

	normalizedDvec_i = np.log2(sum_i)  - np.log2(sum_ij)
	normalizedDvec_j = np.log2(sum_j)  - np.log2(sum_ij)

	return sum_ij, normalizedDvec_i, normalizedDvec_j

def getPPMIVec(iArray, code, sum_ij, normalizedDvec_i, normalizedDvec_j, key=None):

	iVec = iArray[code]

	numVec = np.log2(iArray[code])  - np.log2(sum_ij)			
	pmi = (numVec - normalizedDvec_i) - normalizedDvec_j[code]
	ppmi =  np.maximum(pmi, 0)
	return np.nan_to_num(ppmi)		#Based on spot-checks, nans are due to division by zero somewhere along the chain, and may be replaced with zeros

class featureExtractor(): 

	def __init__(self, vsize):

		self.tally = np.zeros((vsize, vsize), np.uint32)
		self.cvec  = np.zeros((vsize), np.uint32)
		self.key   = st.strMap()

	def increment(self, word):
		isNewEntry, code = self.key.encode(word)
		self.cvec[code] += 1

	def decrement(self, word):
		self.cvec[self.key.getEncoding(word)] -= 1

	def updateTally(self, target):
		tcode = self.key.getEncoding(target) 
		self.tally[tcode] += self.cvec
		self.tally[tcode][tcode] -= 1

	def report(self, target=None):

		for code, word in enumerate(self.key.decodings):
			print('Reporting collocation frequencies for: '+word)
			for coloCode, coloFreq in enumerate(self.tally.data[code]):
				if coloFreq > 0:
					print('\t{}:{}'.format(self.key.getDecoding(coloCode), coloFreq))

	def reportTop10(self, word):
		code = self.key.getEncoding(word)
		#print('Reporting top 10 for "{}" (code == {})'.format(word, code))

	def setScheme(self, wscheme):
		if wscheme not in  ['FREQ', 'PMI']:
			sys.stdout.write('"{}" is not a valid weighting scheme.'.format(wscheme))
			sys.stdout.write('Weighting scheme must be specified as either "FREQ" of "PMI".')
			sys.exit(0)

		if wscheme == 'PMI':
			self.sum_ij, self.normalizedDvec_i, self.normalizedDvec_j = memoizePPMIterms(self.tally)
		
		self.wscheme = wscheme

	def getCosineDistance(self, word1, word2):
		code1 = self.key.getEncoding(word1)
		code2 = self.key.getEncoding(word2)
		if self.wscheme == 'FREQ':
			vec1 = self.tally[code1]
			vec2 = self.tally[code2]
		if self.wscheme == 'PMI':
			vec1 = getPPMIVec(self.tally, code1, self.sum_ij, self.normalizedDvec_i, self.normalizedDvec_j)
			vec2 = getPPMIVec(self.tally, code2, self.sum_ij, self.normalizedDvec_i, self.normalizedDvec_j)

		csim = 1 - scipy.spatial.distance.cosine(vec1, vec2)
		return csim
