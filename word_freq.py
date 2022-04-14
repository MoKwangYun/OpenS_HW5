#!/usr/bin/python3

import sys
import re


fileName = sys.argv[1]
num = int(sys.argv[2])

f = open(fileName, 'r')


line = f.readline()

wordLst = []

while line:
	s = re.sub(r"[^a-zA-Z0-9 ]","", line)
	for l in s.split(' '):
		if l != '':
			wordLst.append(l)
	line = f.readline()


