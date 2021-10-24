'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:

1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.

'''


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from decimal import Decimal
        n = len(points)
        max_points = 1
        d = defaultdict(int)
        for i in range(n):
            #Clear current hashmap internals
            d.clear()
            p1 = points[i]
            same, cur_max = 0, 0
            for j in range(i + 1, n):
                p2 = points[j]
                #Check if two points are the same --> No need to check slopes
                if p1 == p2:
                    same += 1
                    continue
                dx, dy = p1[0] - p2[0], p1[1] - p2[1]
                #Calculate slopes and store in a hashmap
                slope = Decimal(dy) / dx if dx != 0 else 'infinity'
                d[slope] += 1
                cur_max = max(cur_max, d[slope])
            #Update max points value
            max_points = max(max_points, cur_max + same + 1)
        return max_points