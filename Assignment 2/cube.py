def sum(A,i,j):
    sum=0
    for k in range(i,j):
        sum+=A[k]
    return sum

def max_subarray_sum_cubic(A,n):
    max_subarray=[]
    max_subarray_sum=0
    for i in range(n):
        for j in range(i,n):
            if(sum(A,i,j)>max_subarray_sum):
                max_subarray_sum=sum(A,i,j)
                max_subarray.clear()
                max_subarray+=A[i:j]

    print(max_subarray_sum,max_subarray)

max_subarray_sum_cubic([7,5,4,8,3,-2,-5,-3,-1,7],10)

	#graphplot()


