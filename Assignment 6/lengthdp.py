def LengthDP(A,n):
    L=[0 for i in range(n)]
    for j in range(n):
        L[j]=1
        for i in range(j):
            if(A[i]<A[j]):
                L[j]=max(L[i]+1,L[j])
    return max(L)

LengthDP([2, 4, 3, 5, 1, 7, 6, 9, 8],9)