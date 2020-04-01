def insert(magic_grid,row,col):	
	if row==n or col==n:
		return 1
	else:
		for i in range(1,n+1):
			magic_grid[row][col]=i
			if checker(magic_grid,row,col)==1:		
				if col==n-1:
					if insert(magic_grid,row+1,0)==1:	
						return 1
				else:
					if insert(magic_grid,row,col+1)==1:	
						return 1
			else:
				magic_grid[row][col]=0
		return 0

def checker(magic_grid,r,col):	
	for i in range(n):
		if magic_grid[row][col]==magic_grid[row][i] and i!=col:
			return 0	
	for i in range(n):
		if magic_grid[row][col]==magic_grid[i][col] and i!=row:
			return 0	
	return 1

def display(magic_grid):
	for i in range(n):
		print(magic_grid[i])
	print("\n")
n=9
magic_grid=[[0 for i in range(n)] for j in range(n)]

insert(magic_grid,0,0)
display(magic_grid)
