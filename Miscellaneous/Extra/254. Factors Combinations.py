'''
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].

 

Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:

Input: n = 37
Output: []
 

Constraints:

1 <= n <= 10^7

'''

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i, prod):
            
            if path:
                res.append(path[:] + [prod])
                
            j = i
            
            while j * j <= prod:
                if prod % j == 0:
                    
                    path.append(j)
                    
                    dfs(j, prod // j)
                    
                    path.pop()
                    
                j += 1
                    
        path = []
        
        dfs(2, n)
        
        return res
                    