def suffixMax(arr):
	suffix_max = []
	suffix_max.append(max(arr[0],0))
	for i in range(1, len(arr)):
		suffix_max.append(max(suffix_max[i-1] + arr[i],0))
	
	return suffix_max


def subarrayMax(arr):
	suffix_max = suffixMax(arr)
	max_sum, from_ind, to_ind = 0, 0, 0
	for i in range(len(arr)):
		max_sum = max(max_sum, suffix_max[i])
		if(suffix_max[i] == 0):
			from_ind = i
		if(suffix_max[i] == max_sum):
			to_ind = i
	return from_ind, to_ind, max_sum
	
print(subarrayMax([7,5,4,8,3,-2,-5,-3,-1,7])
	

	#graphplot()


