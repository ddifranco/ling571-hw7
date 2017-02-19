#!/bin/bash/python3.5

import time

class stopwatch():

	def __init__(self, splits):

		self.times = dict()
		for split in splits:
			self.times[split] = [0, 0]	#start, total

	def start(self, split):
		self.times[split][0] =  time.time()

	def stop(self, split, report=False):
		self.times[split][1] =  time.time() - self.times[split][0]
		if report:
			print(time.time()) 
			print(self.times[split][0])
			

	def report(self):

		print('Printing timings')

		for k, v in self.times.items():
			print('\t{}:{}'.format(k, v[1]))
