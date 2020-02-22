import math
def LengthDPMod(A,n):
    A.append(math.inf)
    L=[0 for i in range(n+1)]
    for j in range(n+1):
        L[j]=1
        for i in range(j):
            if(A[i]<A[j]):
                L[j]=max(L[i]+1,L[j])
    return max(L)

LengthDPMod([2, 4, 3, 5, 1, 7, 6, 9, 8],9)