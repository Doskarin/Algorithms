'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.

Example 1:


Input: grid = [[1,1,0,0,0],
               [1,1,0,0,0],
               [0,0,0,1,1],
               [0,0,0,1,1]]
Output: 1
Example 2:


Input: grid = [[1,1,0,1,1],
               [1,0,0,0,0],
               [0,0,0,0,1],
               [1,1,0,1,1]]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        #Shapes set where we will be storing unique paths
        shapes = set()
        
        #Dfs method to explore the grid
        def dfs(row, col, direction):
            #If current coordiate if out of bounds - return
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            #If we already visited this cell or cell is not land - return
            if (row, col) in seen or not grid[row][col]:
                return
            
            #Add cell to the seen set
            seen.add((row, col))
            
            #Append current direction
            path.append(direction)
            #Start exploring in 4 directions
            dfs(row + 1, col, "D")
            dfs(row - 1, col, "U")
            dfs(row, col - 1, "L")
            dfs(row, col + 1, "R")
            
            #Once done append "E" to the path indicating the end of path
            path.append("E")
                
        seen = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    path = []
                    dfs(row, col, "S")
                    if path:
                        shapes.add(tuple(path))
        return len(shapes)