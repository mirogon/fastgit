# use git push --set-upstream github master first to be able to use push without a remote/branch
import sys
import os

if len(sys.argv) == 2:

    os.system("git add .")
    os.system("git commit -m " + sys.argv[1])
    os.system("git push")