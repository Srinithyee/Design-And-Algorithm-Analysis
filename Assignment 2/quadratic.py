def prefix_sum(A,n):
    prefix_array=[]
    sum=0
    for i in range(n):
        prefix_array.append(sum)
        sum+=A[i]
        
    return prefix_array

 def max_subarray_sum_quadratic(A,n):
    prefix_array=prefix_sum(A,n)
    print(prefix_array)
    max_subarray=[]
    max_subarray_sum=0
    for i in range(n):
        for j in range(i,n):
            if(sum(A,i,j)>max_subarray_sum):
                max_subarray_sum=prefix_array[j]-prefix_array[i]
                max_subarray.clear()
                max_subarray+=A[i:j]
    flag=0
    for i in max_subarray:
        if i >=0 :
            flag=1
            break
    if flag==0:
        max_subarray.clear()
        max_subarray_sum=0

    print(max_subarray_sum,max_subarray)

max_subarray_sum_quadratic([7,5,4,8,3,-2,-5,-3,-1,7],10)

#graphplot()