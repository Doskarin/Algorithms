'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.

'''

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        
        R, C = len(grid), len(grid[0])
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        island_id = 2
        island_areas = defaultdict(int)
        largest = 0
        
        def bfs(i, j):
            
            q = deque([(i, j)])
            seen = {(i, j)}
            total = 1
            while q:
                x, y = q.popleft()
                grid[x][y] = island_id
                
                for dx, dy in d:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < R and 0 <= yy < C and (xx, yy) not in seen and grid[xx][yy] == 1:
                        total += 1
                        seen.add((xx, yy))
                        q.append((xx, yy))
            return total

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    cur_area = bfs(i, j)
                    island_areas[island_id] = cur_area
                    island_id += 1
        
        for i in range(R):
            for j in range(C):

                if grid[i][j] == 0:
                    cur_area = 1
                    visited_ids = set()

                    for dx, dy in d:
                        xx, yy = i + dx, j + dy

                        if 0 <= xx < R and 0 <= yy < C and grid[xx][yy] != 0:
                            if grid[xx][yy] not in visited_ids:
                                visited_ids.add(grid[xx][yy])
                                cur_area += island_areas[grid[xx][yy]]

                    largest = max(largest, cur_area)
        
        
        return largest if largest != 0 else sum([sum(row) for row in grid]) // 2

    '''
    Time : O(N^2), N - length and width of the grid
    Space : O(N^2), we could possibly store N by N different IDs at most
    
    
    '''