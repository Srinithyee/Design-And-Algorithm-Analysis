def lcs(a,b):
	n=len(a)
	m=len(b)
	l= [[0 for i in range(n)] for j in range(m)]
	for i in range(n+1):
		for j in range(m+1):
			if (i==0 or j==0):
				l[i][j]=0
			elif (a[i-1]==b[j-1]):
				l[i][j]=l[i-1][j-1]+1
			else:
				l[i][j]=max(lcs[l[i-1][j],lcs[i][j-1])
	return l

def trace(a,b):

	l=lcs(a,b)
	m=len(a)
	n=len(b)
	index=l[m][n]

	i,j=m,n
	lcs=""

	while(i>0 and j>0):
		if(a[i-1]==b[j-1]:
			lcs=lcs+str(a[i-1])
			i-=1
			j-=1

		elif l[i-1][j]>l[i][j-1]
			i-=1

		else
			j-=1

	return l[::-1]

a=[1,2,3,4,5]
b=[2,3,4]
print(trace(a,b))_
