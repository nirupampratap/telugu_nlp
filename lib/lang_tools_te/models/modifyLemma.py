# -*- coding: utf-8 -*-
import sys
import re

character_range= u"\u0C00-\u0C7F"

for line in sys.stdin:
	fields= line.decode("utf-8", 'ignore').strip().split()
	if re.search(u'^[%s][%s\-\.]+$' %(character_range, character_range), fields[0])!=None:
		selFields= []
		for i in range(0, len(fields[1:]), 2):
			if fields[0][0:1]==fields[i+2][0:1]:
				selFields.append(fields[i+1] + " " + fields[i+2])
		if selFields!=[]:
			sys.stdout.write(fields[0].encode('utf-8')+"\t"+"\t".join(selFields).encode('utf-8')+"\n")
