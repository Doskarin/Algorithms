'''
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.

'''

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        output = 0
        
        
        def backtrack(x, y):
            #Base case : if we are out of bounds
            #or if current grid does not contain gold
            #return 0
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0:
                return 0
            #Initialize ans to zero
            ans = 0
            
            #Save current cell's value
            #so that we could backtrack later
            cur_gold = grid[x][y]
            
            #set cell's value to zero
            grid[x][y] = 0
            
            #Continue exploring along the path
            #and save the result
            for dx, dy in d:
                xx, yy = x + dx, y + dy
                ans = max(ans, backtrack(xx, yy))
            
            #Backtrack
            grid[x][y] = cur_gold
            
            
            return ans + grid[x][y]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    output = max(output, backtrack(i, j))
        return output