import sys
import os

if len(sys.argv) == 2:

    os.system("git add .")
    os.system("git commit -m " + argv[1])
    os.system("git push")