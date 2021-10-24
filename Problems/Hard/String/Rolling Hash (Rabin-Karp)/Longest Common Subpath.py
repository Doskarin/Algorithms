'''
There is a country of n cities numbered from 0 to n - 1. In this country, there is a road connecting every pair of cities.

There are m friends numbered from 0 to m - 1 who are traveling through the country. Each one of them will take a path consisting of some cities. Each path is represented by an integer array that contains the visited cities in order. The path may contain a city more than once, but the same city will not be listed consecutively.

Given an integer n and a 2D integer array paths where paths[i] is an integer array representing the path of the ith friend, return the length of the longest common subpath that is shared by every friend's path, or 0 if there is no common subpath at all.

A subpath of a path is a contiguous sequence of cities within that path.

 

Example 1:

Input: n = 5, paths = [[0,1,2,3,4],
                       [2,3,4],
                       [4,0,1,2,3]]
Output: 2
Explanation: The longest common subpath is [2,3].
Example 2:

Input: n = 3, paths = [[0],[1],[2]]
Output: 0
Explanation: There is no common subpath shared by the three paths.
Example 3:

Input: n = 5, paths = [[0,1,2,3,4],
                       [4,3,2,1,0]]
Output: 1
Explanation: The possible longest common subpaths are [0], [1], [2], [3], and [4]. All have a length of 1.
 

Constraints:

1 <= n <= 10^5
m == paths.length
2 <= m <= 10^5
sum(paths[i].length) <= 10^5
0 <= paths[i][j] < n
The same city is not listed multiple times consecutively in paths[i].

'''
class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        #Modulo to avoid collisions and overflow
        mod = 2**63 - 1
        
        #Base
        a = random.randint(10 ** 6, 10 ** 7)
        
        def search(L, path):
            h = 0
            #Instantiate base rolling hash
            for i in range(L):
                h = (h * a + path[i]) % mod
                
            #Precalculate constant factor to account for largest power while rolling
            const = pow(a, L, mod)
            hashes = {h}
            #Rolling hash happens here
            for i in range(1, len(path) - L + 1):
                h = (h * a - const * path[i - 1] + path[i + L - 1]) % mod
                hashes.add(h)
        
            return hashes
        
        
        
        left, right = 1, len(min(paths, key = len))
        ans = 0
        #Binary search for the longest possible subpath where left is lowest possible subpath
        #and right is the length of the smallest subpath
        while left <= right:
            mid = left + (right - left) // 2
            common = set.intersection(*[search(mid, path) for path in paths])
            #If all subpaths have some common intersection it means we can still expand the window size
            if len(common) != 0:
                #Save the answer while binary searching
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans