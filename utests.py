#!/usr/bin/python3

import structs as st
import resources as rc
import pdb
import numpy as np
import sys

r1 = [1, 5, 2 , 3]
r2 = [2, 6, 8 , 1]
r3 = [2, 2, 9 , 5]
r4 = [3, 6, 8 , 2]

x = np.array([r1, r2, r3, r4])

sum_ij, normalizedDvec_i, normalizedDvec_j = rc.memoizePPMIterms(x)

t = rc.getPPMIVec(x, 2, sum_ij, normalizedDvec_i, normalizedDvec_j)

pdb.set_trace()
sys.exit(0)

o = np.zeros((4, 4), np.float32)
y =  rc.derivePPMI(x, o)

pdb.set_trace()
sys.exit(0)

f =  open(out_file, 'rb')
favorite_color = { "lion": "yellow", "kitty": "red" }	
pickle.dump(favorite_color, f)

sys.exit(0)

xa = st.expandableArray()

xa.inspect()
xa.expand()
xa.inspect()
xa.expand()
xa.inspect()
xa.expand()
xa.inspect()
xa.expand()
xa.inspect()
