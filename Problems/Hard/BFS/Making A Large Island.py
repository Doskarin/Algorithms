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
        #Initialize hashmap with island ID : total area pair that will be used in order to calculate largest possible island
        areas = defaultdict(int)
        
        
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        #Since islands are represented as 1s initial ID number is 2
        Id = 2
        
        #Flag to be used in case we do not find zero, answer is just sum of 1s
        foundZero = False
        rows, cols = len(grid), len(grid[0])
        
        #Main BFS method to mark neighbouring parts with corresponding ID and assign area in 'areas' hash-table
        def mark(i, j, Id):
            #Mark grid with corresponding ID
            grid[i][j] = Id
            
            #Initialize queue
            q = deque([(i, j)])
            
            #Keep track visited coordinates
            seen = {(i, j)}
            
            #Initialize current area to 1
            cur_area = 1
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    
                    #Explore 4-directionally
                    for dx, dy in d:
                        ii, jj = i + dx, j + dy
                        
                        #Check if inbounds, if coordinate has not been visited yet and if next coordinate is actual land
                        if 0 <= ii < rows and 0 <= jj < cols and (ii, jj) not in seen and grid[ii][jj] == 1:
                            
                            #Append to the queue, seen set, mark current part of island with ID and increment current area
                            q.append((ii, jj))
                            seen.add((ii, jj))
                            grid[ii][jj] = Id
                            cur_area += 1
            #Assing current area to corresponding ID
            areas[Id] = cur_area

        for i in range(rows):
            for j in range(cols):
                #Check if it is worth to explore current cell
                if grid[i][j] != 0 and grid[i][j] not in areas:
                    #Mark entire island and increment ID in order to distinguish
                    mark(i, j, Id)
                    Id += 1
                
        max_island = 1
        for i in range(rows):
            for j in range(cols):
                #Cells with 0s are our candidates that we need to explore
                if grid[i][j] == 0:
                    foundZero = True
                    #Given we are allowed to change one zero to 1 current island's area is 1
                    cur_island = 1
                    seen = set()
                    for dx, dy in d:
                        ii, jj = i + dx, j + dy
                        #Check if inbounds and cell's ID has not been considered yet
                        if 0 <= ii < rows and 0 <= jj < cols and grid[ii][jj] != 0  and grid[ii][jj] not in seen:
                            #Since we already precalculated our areas in hashmap we just access its area and add to current area
                            #22220333
                            #22444444
                            #11111111
                            #Consider example above: for the current zero we can add neighbouring areas with IDs 2 (to the left), 3 (to the right) and 4 (below)
                            
                            cur_island += areas[grid[ii][jj]]
                            seen.add(grid[ii][jj])
                    #Keep track of global max
                    max_island = max(max_island, cur_island)
        return max_island if foundZero else sum([sum(row) for row in grid]) // 2
    