def MaxSum(arr, low, high):
    if(low == high):	
        return arr[0]
    
    else:	
        mid = (low+high)//2
        return max(	dcMaxSum(arr,low, mid),
					dcMaxSum(arr, mid+1, high),
                    dcMiddleSum(arr, low, mid, high))


def MiddleSum(arr, low, mid, high):	
	max_sum, left_sum = 0, 0
	for i in range(mid, low-1, -1):	
		max_sum = max_sum + arr[i]

		if(max_sum > left_sum):
			left_sum = max_sum

	max_sum, right_sum = 0, 0
	for i in range(mid+1, high):	
		max_sum = max_sum + arr[i]

		if(max_sum > right_sum):
			right_sum = max_sum
	
	return left_sum + right_sum		

 MaxSum([7,5,4,8,3,-2,-5,-3,-1,7], 0, 10)
	print(MaxSum)
	
	#graphplot()