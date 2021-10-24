'''
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.

Example 2:

Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]
 

Constraints:

1 <= m, n, positions.length <= 104
1 <= m * n <= 104
positions[i].length == 2
0 <= ri < m
0 <= ci < n


'''
#Union Find data structure class
class UnionFind:
    #Initialize parents to -1 initially because island parts have not been added yet
    def __init__(self, size):
        self.parent = [-1] * size
        self.rank = [1] * size
        self.count = 0
        
    #Method to check if certain coordinate exists
    def exists(self, x):
        return self.parent[x] >= 0
    
    #Method to add island part, if it already exists - we do not proceed
    #Otherwise assign parent, rank and increase total count by one
    #Count might be reduced in the future if it happens to be connected with some other land parts
    def add(self, x):
        if self.exists(x):
            return
        self.parent[x] = x
        self.rank[x] = 1
        self.count += 1
        
    #Method to find the root of the land part
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    #Union method to merge island cells between each other
    #Part with bigger rank 'swallows' the one with smaller rank
    #As a result we decrease total land count by 1 since cell became part of existing land
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        #If cell parts are already connected - do nothing
        if rootX == rootY:
            return False
        #Merge operation
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.rank[rootX] += self.rank[rootY]
                self.parent[rootY] = rootX
            else:
                self.rank[rootY] += self.rank[rootX]
                self.parent[rootX] = rootY
        #Decrease total count by 1
        self.count -= 1
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        #Initialize uf object with size m * n (total size of our bracket)
        uf = UnionFind(m*n)
        ans = [0] * len(positions)
        #Method to get coordinates of the cells in a flattened manner
        def getID(r, c):
            return r * n + c
        
        #Method to get all neighbors
        def neighbors(r, c):
            for direction in directions:
                rr, cc = r + direction[0], c + direction[1]
                if 0 <= rr < m and 0 <= cc < n and uf.exists(getID(rr, cc)):
                    yield getID(rr, cc)
                    
        #Iterate through position in chronological order and union islands as we go (if applicable)
        for i, (r, c) in enumerate(positions):
            curID = getID(r, c)
            uf.add(curID)
            for neiID in neighbors(r, c):
                #Union cells
                uf.union(curID, neiID)
            #After each iteration update count of total islands to our answer
            ans[i] = uf.count
        return ans