# -*- mode: python; -*-
# PDB configuration
#
# NOTE .pdbrc only allows things you can type at the pdp prompt.  That means
# you can't include functions or scripts.  Put those in .pdbrc.py

import os
import sys
import pdb
import rlcompleter

alias ipy from IPython import embed;embed()
# refresh the terminal
os.system("stty sane")

# this rc file takes single lines, so define our complete function here
exec(open(os.path.expanduser("~/.pdbrc.py")).read())

# replace the Pdb class's complete method with ours
sys._getframe(1).f_globals['Pdb'].complete = complete

# set use_rawinput to 1 as tab completion relies on rawinput being used
sys._getframe(1).f_locals['self'].use_rawinput = 1