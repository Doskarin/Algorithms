'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],
               [1,1,0],
               [0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],
               [0,1,1],
               [1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        
        fresh_oranges = 0
        rotten = deque()
        #Calculate fresh oranges we have in the grid
        #also collecting coordinates of rotten oranges
        #in the deque
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                if grid[i][j] == 2:
                    rotten.append((i, j))
        #If number of fresh oranges
        #is zero it means there is nothing
        #to be rotting - return 0
        if fresh_oranges == 0:
            return 0
        #Start with minute 0
        minutes = 0
        while rotten:
            #Increase minute by 1
            #and start processing first layer
            #of rotten oranges
            minutes += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in d:
                    rr, cc = r + dr, c + dc
                    #if new coordinate is inbounds and is fresh orange
                    #it becomes rotten in this particular minute
                    #and we can decrease count of fresh oranges by 1
                    if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        fresh_oranges -= 1
                        #if number of fresh oranges is 0
                        #return minutes passed so far
                        if fresh_oranges == 0:
                            return minutes
                        #append next coordinate to next layer
                        rotten.append((rr, cc))
        #return -1 if there are still some fresh oranges left
        return -1