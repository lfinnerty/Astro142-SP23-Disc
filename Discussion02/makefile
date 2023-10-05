all: sayhi runpython

helloworld: helloworld.c
	gcc helloworld.c -o helloworld

sayhi: helloworld
	./helloworld

runpython: python_plot_demo.py
	python python_plot_demo.py

clean: 
	rm helloworld
	rm -f *.pdf
