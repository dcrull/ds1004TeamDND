#!/usr/bin/python
import sys

current_key = None
ACSP = []
FCC = []
#read in each line and split into key and values 
for line in sys.stdin:
	#split by tabs
	key, value = line.strip().split('\t')
	vsplit = len(value.split(','))
	#split the values by value
	if current_key == key:
		if vsplit == 10:
			FCC.append(value)
		else:
			ACSP.append(value)
	else:
		if current_key:
			if (len(FCC) != 0)  & (len(ACSP) != 0):
				for i in range(len(FCC)):
					for j in range(len(ACSP)):
						print ('%s,%s,%s') % (current_key, FCC[i], ACSP[j])

		current_key = key
		FCC = []
		ACSP = []
		if vsplit == 10:
			FCC.append(value)
		else:
			ACSP.append(value)
if current_key == key:
	if (len(ACSP) != 0)  & (len(FCC) != 0):
		for i in range(len(FCC)):
			for j in range(len(ACSP)):
				print ('%s,%s,%s') % (current_key, FCC[i], ACSP[j])
