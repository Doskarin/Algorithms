'''
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:


Input: grid = [[1,0,0,0],
               [0,0,0,0],
               [0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:


Input: grid = [[1,0,0,0],
               [0,0,0,0],
               [0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:


Input: grid = [[0,1],
               [2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.

'''
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        from sortedcontainers import SortedSet
        
        
        rows, cols = len(grid), len(grid[0])
        d = [(0,1),(1,0),(0,-1),(-1,0)]
        count = 0
        empty = 0
        #Calculate number of empty cells
        #so that we can make sure we visited
        #everything while exploring potential paths
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start_row, start_col = i, j
                empty += int(grid[i][j] != -1)
        
        def backtrack(x, y, rest):
            nonlocal count
            
            #if out of bounds or
            #or there is an obstacle/visited cell
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] < 0:
                return
            
            #if we reached the target and
            #there is zero empty cells to be
            #visited - increment count by 1
            if grid[x][y] == 2 and rest == 0:
                count += 1
                
                
            #Explore in 4 direction
            for dx, dy in d:
                #Save current cell to backtrack later
                saved = grid[x][y]
                
                #Mark cell as obstacle
                grid[x][y] = -1
                
                xx, yy = x + dx, y + dy
                
                backtrack(xx, yy, rest - 1)
                
                #Backtrack
                grid[x][y] = saved
        
        
        #Empty - 1 because we are already at the empty
        #cell
        backtrack(start_row, start_col, empty - 1)
        
        return count