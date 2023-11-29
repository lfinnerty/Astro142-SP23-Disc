import numpy as np
from multiprocessing import Pool, Queue
import multiprocessing as mp
from time import sleep

def myfunc(i):
	print(i)
	# raise ValueError
	return i

def producer(q, num, rest):
	for i in np.arange(num):
		q.put(i)
		sleep(rest)
	q.put(None)

def consumer(q):
	### This will run forever until
	### the queue has a None value
	while True:
		val = q.get()
		if val is None: 
			break
		else:
			print('This is the value', val)
	print('Cleared queue')
	

if __name__ == '__main__':
	## For loop version
	vals = []
	for i in range(30):
		vals.append(myfunc(i))
	print(vals)

	# 

	print('----------------------------------------')
	print('Pool version')
	### Pool version
	pool = Pool(8)
	result = pool.map(myfunc, np.arange(30))
	# pool.join()
	pool.close()
	pool.join()
	print(result)

	# assert 1==0

	print('-----------------------------------------')
	### Set up the queue processor
	q = Queue()
	con = mp.Process(target=consumer, args=(q,))
	con.start()

	### Add things to the queue using a different process
	prod = mp.Process(target=producer, args=(q,10,1))
	prod.start()


	prod.join()
	con.join()
	prod.close()
	con.close()
