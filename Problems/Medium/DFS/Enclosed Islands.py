'''
BinarySearch problem

You are given a two-dimensional integer matrix of 1s and 0s. A 1 represents land and 0 represents water. From any land cell you can move up, down, left or right to another land cell or go off the matrix.

Return the number of land cells from which we cannot go off the matrix.

Constraints

n, m ≤ 250 where n and m are the number of rows and columns in matrix
Example 1
Input
matrix = [
    [0, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]
Output
4
Explanation
There's 4 land squares in the middle from which we cannot walk off the matrix.


'''
class Solution:
    def solve(self, grid):
        rows, cols = len(grid), len(grid[0])
        #Helper array to explore the grid in 4 directions
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        
        #Dfs method to perform final calculation of enclaves on the grid
        def dfs(x, y):
            nonlocal enclave
            enclave += 1
            grid[x][y] = -1
            for dx, dy in d:
                xx, yy = x + dx, y + dy
                if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == 1:
                    dfs(xx, yy)
            return
        
        #Mark method used to perform flood fill on islands that have an access to the borders
        def mark(x, y):
            grid[x][y] = -1
            for dx, dy in d:
                xx, yy = x + dx, y + dy
                if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == 1:
                    mark(xx, yy)
        
        #Iterate through all borders and if 1 is encountered - perform flood fill with mark method
        for i in range(rows):
            if grid[i][0] == 1:
                mark(i, 0)
            if grid[i][cols - 1] == 1:
                mark(i, cols -1)
        for j in range(cols):
            if grid[0][j] == 1:
                mark(0, j)
            if grid[rows - 1][j] == 1:
                mark(rows - 1, j)
        
        #Now we are left only with enclaves (if there are any)
        #Initialize enclave as 0
        enclave = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 1:
                    continue
                #Perform dfs on cells with value of 1 and update enclave value
                dfs(i, j)
        
        return enclave