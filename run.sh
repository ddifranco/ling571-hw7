#!/bin/bash

HUMAN='/dropbox/16-17/571/hw7/mc_similarity.txt'
SWINDOW=2
LWINDOW=10

./main.py $SWINDOW PMI $HUMAN hw7_sim_$SWINDOW_PMI_output.txt

#./utests.py

