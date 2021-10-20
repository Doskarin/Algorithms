'''
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 104
No two stones are at the same coordinate point.


'''

class UnionFind:
    #Initialize parents to i initially because stones have not been merged
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size
        
    #Method to find the root of the stone part
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    #Union method to merge stones between each other
    #Part with bigger rank 'swallows' the one with smaller rank
    #As a result we decrease total group count by 1 since stone became part of existing group
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        self.count -= 1
        if self.rank[rootX] > self.rank[rootY]:
            self.rank[rootX] += self.rank[rootY]
            self.parent[rootY] = rootX
        else:
            self.rank[rootY] += self.rank[rootX]
            self.parent[rootX] = rootY
        return True

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        
        #Initialize union find object with size n
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i + 1, n):
                #If either rows or cols of two stones are equal - we union them
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        #At the end we return total stones minus stones that are left
        return n - uf.count