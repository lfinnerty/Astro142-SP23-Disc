import sys

if __name__ == '__main__':
	val = sys.argv[1]
	# print(val)
	### Note that if one parallel execution fails,
	### the others will continue normally. You also
	### don't get a messy pool traceback
	print(float(val)+3)
		

