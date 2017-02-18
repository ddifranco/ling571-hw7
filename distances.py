#!/bin/python3.4

for comparison in [x.strip('\n').split(',') for x in human.readlines()]:
	print(comparison[0])
	print(comparison[1])
	print(comparison[2])
