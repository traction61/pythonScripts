#!/usr/bin/env python
 
import os
import glob
 
for name in glob.glob('007*'):
    os.system('pyFoamPVSnapshot.py --latest-time --state-file=default.pvsm %s/' % name)