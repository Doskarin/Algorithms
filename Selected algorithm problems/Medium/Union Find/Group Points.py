'''
BinarySearch problem

You are given a two-dimensional list of integers points and an integer k. Each list in points is of the form (x, y) representing Cartesian coordinates. Assuming you can group any point a and b if the Euclidean distance between them is ≤ k, return the total number of disjoint groups.

Note that if points a and b are grouped and b and c are grouped, then a and c are in the same group.

Constraints

n ≤ 1,000 where n is length of points.
Example 1
Input
points = [
    [1, 1],
    [2, 2],
    [3, 3],
    [10, 10],
    [11, 11]
]
k = 2
Output
2
Explanation
There are two groups:

[1,1],[2,2],[3,3]
[10,10],[11,11]

'''
#Union Find data structure class
class UnionFind:
    
    #Initialize parents to i initially because points have not been merged
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size
        
    #Method to find the root of the land part
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    #Union method to merge points between each other
    #Part with bigger rank 'swallows' the one with smaller rank
    #As a result we decrease total group count by 1 since cell became part of existing group
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        self.count -= 1
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
        return True

class Solution:

    #Method to calculate Euclidean distance
    def calculateDistance(self, point1, point2):
        return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def solve(self, points, k):
        n = len(points)
        #Initialize union find object with size n
        uf = UnionFind(n)
        #Iterate through all possible point pairs and union them as we go
        for i in range(n):
            for j in range(i + 1, n):
                #Check if distance between these two points is less than or equal to k
                if self.calculateDistance(points[i], points[j]) <= k:
                    uf.union(i, j)
        #Return number of points
        return uf.count