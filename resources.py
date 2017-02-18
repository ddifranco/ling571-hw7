#!/bin/bash/python3.4

import sys
import numpy as np
import structs as st
import pickle

def preprocess(raw):

	punc = [',', '.', '?', '!', '$', '-', '/', '\\', '(', ')', ':', '"', '\'']

	if raw in punc:
		return None

	return raw.lower()

class featureExtractor():

	def __init__(self):

		self.tally = st.expandableArray()
		self.cvec  = list()
		self.key   = st.strMap()

	def increment(self, word):
		isNewEntry, code = self.key.encode(word)
		if isNewEntry:
			self.cvec.append(1)
			self.tally.expand()
		else:
			self.cvec[code] += 1
		print(self.cvec)

	def decrement(self, word):
		self.cvec[self.key.getEncoding(word)] -= 1
		print(self.cvec)

	def updateTally(self, target):
		print('Upating tally of target: '+target)
		tcode = self.key.getEncoding(target) 
		self.tally.data[tcode] += np.array(self.cvec)
		self.tally.data[tcode][tcode] -= 1

	def report(self, target=None):

		for code, word in enumerate(self.key.decodings):
			print('Reporting collocation frequencies for: '+word)
			for coloCode, coloFreq in enumerate(self.tally.data[code]):
				if coloFreq > 0:
					print('\t{}:{}'.format(self.key.getDecoding(coloCode), coloFreq))

	def save(self, out_file):
		f =  open(out_file, 'wb')
		pickle.dump(self, f)
