'''
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

Example 1:


Input: grid = [[1,0,2,0,1],
               [0,0,0,0,0],
               [0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
Example 2:

Input: grid = [[1,0]]
Output: 1
Example 3:

Input: grid = [[1]]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0, 1, or 2.
There will be at least one building in the grid.


'''

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        d = [(-1,0),(0,-1),(1,0),(0,1)]
        total_buildings = 0
        #Hit matrix to keep track of how many times cell with 0 has been reached
        hit = [[0] * cols for _ in range(rows)]
        
        #Distances from 1s to the cells with 0 
        distances = [[0] * cols for _ in range(rows)]
        
        #Calculate number of total buildings
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    total_buildings += 1
        
        #Bfs method to fill in hit and distance matrices
        def bfs(i, j):
            cur_count = 1
            #visited set to prevent inifinite loop
            visited = set()
            visited.add((i, j))
            #Initialize queue with start at (i, j) and distance 0
            q = deque([(i, j, 0)])
            while q:
                i, j, dist = q.popleft()
                for dx, dy in d:
                    ii, jj = i + dx, j + dy
                    #Check if inbounds and in visited
                    if 0 <= ii < rows and 0 <= jj < cols and (ii, jj) not in visited:
                        visited.add((ii, jj))
                        
                        #If grid cell is 0 it means we can reach this cell from building
                        if grid[ii][jj] == 0:
                            
                            #Increase hit value for cell by 1
                            hit[ii][jj] += 1
                            #Add next frontier to the queue
                            q.append((ii, jj, dist + 1))
                            distances[ii][jj] += dist + 1
                        elif grid[ii][jj] == 1:
                            cur_count += 1
            return

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    bfs(i, j)
        min_distance = float('inf')
        for i in range(rows):
            for j in range(cols):
                if hit[i][j] == total_buildings:
                    min_distance = min(min_distance, distances[i][j])
        return min_distance if min_distance != float('inf') else -1