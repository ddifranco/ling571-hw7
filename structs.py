#!/bin/bash/python3.4

import numpy as np
import pdb

class strMap():

	def __init__(self):

		self.i = 0
		self.encodings = dict()
		self.decodings = list()

	def encode(self, tkn):

		if tkn in self.encodings:
			return False, self.encodings[tkn]

		self.encodings[tkn] = self.i
		self.decodings.append(tkn)
		self.i += 1

		return True, self.i-1

	def getEncoding(self, tkn):
		return self.encodings[tkn]

	def getDecoding(self, code):
		return self.decodings[code]

class expandableArray():

	def __init__(self):

		#Starting with a blank array - while elegant - would require a time-consuming consideration of edge cases
		#The difference should not matter for this application, but be careful about porting this code to another application

		self.data = np.array([[0, 0], [0, 0]])
		self.rank = 2 			#Requirement and rank expressed in terms of a one-based array
		self.requirement = 0  		#e.g., self.rank=2 corresponds to a 2x2 array

	def expand(self):

		#Expand append across then down with respect to how the array is printed
		#Effectively, append to the inner index
		#Note, first argument in the zeros corresponds to the up-down axis, 
		#while second argument corresponds to the left-righ axis. 

		self.requirement += 1 
		if self.requirement <= self.rank:
			return
		
		leftRightZs = np.zeros((self.rank, 1), int)
		upDownZs = np.zeros((1, self.requirement), int)

		self.data = np.concatenate((self.data, leftRightZs), axis=1)
		self.data = np.concatenate((self.data, upDownZs), axis=0)

		self.rank += 1

	def inspect(self, row=None):

		if row is None:
			print(self.data)
			print('Rank: '+str(self.rank))
			print('Requirement: '+str(self.requirement))
		else:
			print(self.data[row])
	
