#!/bin/python3.4

import structs as st
import pdb

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
