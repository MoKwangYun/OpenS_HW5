#!/usr/bin/python3
#2017112823 MoKwangYun
#edit from UI
#git pull(edit from UI - check)

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
	print("{:10}".format(str(wordCnt[i][0])) + "%5s"%str(wordCnt[i][1]))
