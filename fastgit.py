import sys
import os

if len(sys.argv) == 3:

    os.system("git add .")
    os.system("git commit -m " + sys.argv[2])
    os.system("git push " + sys.argv[1])