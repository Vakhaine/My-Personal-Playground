# working with modules
import glob

# 1. glob

myfiles = glob.glob("*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as files:
        print(files.read().upper())

