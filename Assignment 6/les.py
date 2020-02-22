from itertools import chain, combinations
def power_set(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def checkAscending(A,n):
    for i in range(1,n):
        if A[i]<A[i-1]:
            return 0
    return 1

def LengthES(A,n):
    pow_set=list(power_set(A))
    maxlen=0
    for i in pow_set:
        if checkAscending(i,len(i))==1:
            if len(i)>maxlen:
                maxlen=len(i)
    return maxlen

LengthES([2,3,4],3)