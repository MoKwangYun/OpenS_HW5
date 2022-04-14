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

wordCnt = {}
for word in wordLst:
	try: wordCnt[word] += 1
	except: wordCnt[word] = 1

wordCnt = sorted(wordCnt.items(), key=lambda x: x[1], reverse=True)

for i in range(num):
	print(str(wordCnt[i][0]) + "\t" + str(wordCnt[i][1]))
