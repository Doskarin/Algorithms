'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 10^4
-10^4 < xi, yi < 10^4

'''
class Solution:
    def kClosest_heap(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        from heapq import heappush, heappop
        p1 = [0,0]
        heap = []
        for point in points:
            dist = self.getDistance(point, p1)
            
            if len(heap) == k:
                
                if -heap[0][0] > dist:
                    
                    heappop(heap)
                    heappush(heap, (-dist, point))
            else:
                
                heappush(heap,(-dist, point))
                
        ans = []
        
        for _, point in heap:
            
            ans.append(point)
        
        return ans

    def getDistance(self, p1, p2):
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    '''
    Time : O(NlogK), where K is k elements, add/removing elements to the heap takes O(logK)
    Space : O(K), the heap will contain at most K elements
    '''
    def kClosest_quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        return self.quickSelect(points, k)
    
    
    
    def quickSelect(self, points, k):
        left, right = 0, len(points) - 1
        pivot_index = len(points)
        
        while pivot_index != k:
            pivot_index = self.partition(points, left, right)
            
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1        
        
        return points[:k]
    
    def partition(self, points, left, right):

        pivot = points[left + (right - left) // 2]
        pivot_dist = self.squaredDist(pivot)
        
        while left < right:

            if self.squaredDist(points[left]) >= pivot_dist:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1

        if self.squaredDist(points[left]) < pivot_dist:
            left += 1
            
        return left
    
    '''
    Time : O(N), if the worst pivot is chosen worst case becomes O(N^2),
    on average it is O(N) because if halves (roughly) the remaining elements needed to be processed at each iteration:
    N + N/2 + N/4 + N/8 + ... + N/N = 2N total processes, yielding an average time complexity of O(N)
    
    Space : O(1) the quickselect algorithm conducts the partial sort of points in place with no recursion, so only constant extra space is required
    
    
    '''
                
        
    