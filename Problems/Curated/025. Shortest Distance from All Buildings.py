'''
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

 

Example 1:


Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
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
        from collections import deque
        R, C = len(grid), len(grid[0])
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        hits = [[0] * C for _ in range(R)]
        distances = [[0] * C for _ in range(R)]
        total = 0
        
        # Calculate total number of buildings
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    total += 1
                    
        # BFS method
        
        def bfs(r, c):
            q = deque([(r,c,0)])
            visited = {(r,c)}
            while q:
                x, y, dist = q.popleft()
                for dx, dy in d:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < R and 0 <= yy < C and (xx, yy) not in visited and grid[xx][yy] != 2:
                        visited.add((xx, yy))
                        if grid[xx][yy] == 0:
                            hits[xx][yy] += 1
                            distances[xx][yy] += dist + 1
                            q.append((xx, yy, dist + 1))

        #Main loop
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    bfs(i, j)
                    
        
        #Getting an answer
        shortest_distance = float('inf')
        for i in range(R):
            for j in range(C):
                
                if hits[i][j] == total:
                    shortest_distance = min(shortest_distance, distances[i][j])
        
        return shortest_distance if shortest_distance != float('inf') else -1
    
    '''
    Time : O(N^2 * M^2), For each house, we will traverse
    across all reachable land. This will require O(number of zeros * number of ones) time
    and the number of zeros and ones in the matrix is of order N * M.
    Consider that when half of the values in grid are 0 and half of the values are 1,
    total elements in grid will be (M * N) so their counts are (M * N) / 2 and (M * N) / 2
    respectively, thus giving time complexity (M * N) / 2 * (M * N) / 2 which results in
    O(N^2 * M^2)
    
    Space : O(N * M), we are using extra arrays hits and distances
    

    '''