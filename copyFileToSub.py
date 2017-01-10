#!/usr/bin/env python
 
import glob
from shutil import copyfile
 
for name in glob.glob('007*'):
    copyfile('default.pvsm', '%s/default.pvsm' % name)