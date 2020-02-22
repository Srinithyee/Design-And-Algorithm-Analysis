import math
def LengthDPred(A,n):
    L=[0 for i in range(n)]
    P=[-math.inf for i in range(n)]
    for j in range(n):
        L[j]=1
        for i in range(j):
            if(A[i]<A[j]):
                L[j]=max(L[i]+1,L[j])
                if L[j]>1:
                    if L[j]==L[i]+1:
                        P[j]=i
                    else:
                        P[j]=j
    return L,P

LengthDPred([5,2,8,6,3,6,9,7],8)