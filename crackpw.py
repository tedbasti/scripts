#!/usr/bin/env python

import hashlib
import sys

if (len(sys.argv) <3):
    print("Usage: " + sys.argv[0] + " <md5Value> <wordlist>")
    sys.exit(1)

searchedHash = sys.argv[1]
wordlistFilename = sys.argv[2]

with open(wordlistFilename, 'r') as f:
    for r in f:
        line = r.replace('\n','').replace('\r','')
        m = hashlib.md5(line.encode())
        if (m.hexdigest().lower() == searchedHash.lower()):
            print("Found password: '" + line + "'")
            sys.exit(0)
    print("Found no password")
    sys.exit(2)

