def graphplot():
	import random
	import matplotlib.pyplot as plt
	import time

	times = []
	n_values = []

	for n in range(10, 1000, 50):
		res = [random.randrange(1000) for i in range(n)]
		start = time.time()
		max_sum = MaxSum(res, 0, len(res)) 
		end = time.time()

		n_values.append(n)
		times.append(end-start)

	plt.xlabel("Length of N")
	plt.ylabel("Running Time")
	plt.plot(n_values, times, label = "O(n)")   
	plt.grid()
	plt.legend()
	plt.show()
	plt.title("Time Complexity Analysis")