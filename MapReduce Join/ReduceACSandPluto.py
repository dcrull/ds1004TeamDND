#!/usr/bin/python
import sys

current_key = None
#read in each line and split into key and values 
for line in sys.stdin:
	#split by tabs
	key, value = line.strip().split('\t')
	vsplit = len(value.split(','))
	#split the values by value
	if current_key == key:
		if vsplit == 23:
			PLUTO.append(value)
		else:
			ACS.append(value)
	else:
		if current_key:
			if (len(PLUTO) != 0)  & (len(ACS) != 0):
				for i in range(len(PLUTO)):
					for j in range(len(ACS)):
						print ('%s,%s,%s') % (current_key, PLUTO[i], ACS[j])

		current_key = key
		PLUTO = []
		ACS = []
		if vsplit == 23:
			PLUTO.append(value)
		else:
			ACS.append(value)
if current_key == key:
	if (len(ACS) != 0)  & (len(PLUTO) != 0):
		for i in range(len(PLUTO)):
			for j in range(len(ACS)):
				print ('%s,%s,%s') % (current_key, PLUTO[i], ACS[j])