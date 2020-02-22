ef TraceLISIter(A,LIS,P):
    while max(P)>0:
        if len(LIS)==0:
            LIS.append(A[L.index(max(L))])
        
        ix=max(P)
        LIS.append(A[ix])
        
        P=[x for x in P if x!=ix]
        
    return LIS[::-1]

L,P=LengthDPred([5,2,8,6,3,6,9,7],8)
LIS=[]
TraceLISIter([5,2,8,6,3,6,9,7],LIS,P)