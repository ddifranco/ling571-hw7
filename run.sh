#!/bin/bash

#HUMAN='/dropbox/16-17/571/hw7/mc_similarity.txt'
#HUMAN='hsamp.txt'
HUMAN='mc_similarity.txt'
#HUMAN='toy.txt'
SWINDOW=2
LWINDOW=10

#time ./main.py $SWINDOW PMI $HUMAN hw7_sim_$SWINDOW_PMI_output.txt

time ./cbow.py $SWINDOW $HUMAN hw7_sim_$SWINDOW_CBOW_output.txt

#./utests.py
#./utests.py
