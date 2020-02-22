def TraceLISRecur(A,LIS,P):
    
    if max(P)<=0:
        return LIS[::-1]
    if len(LIS)==0:
        LIS.append(A[L.index(max(L))])
    ix=max(P)
    LIS.append(A[ix])
    
    P=[x for x in P if x!=ix]
    
    TraceLISRecur(A,LIS,P)
    return LIS[::-1]

L,P=LengthDPred([5,2,8,6,3,6,9,7],8)
LIS=[]
TraceLISRecur([5,2,8,6,3,6,9,7],LIS,P)