#!/usr/bin/python
import sys


for line in sys.stdin:
	line2 = line.strip().split(',')

	
	if ('FIPS' in line2[0]) | ('GEOID' in line2[0]) | (line == ''):
		continue
	else:
		key = line2[0]
		value = ','.join(line2[1:])
	
		print ('%s\t%s') % (key, value)