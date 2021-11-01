'''
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

1. perm[i] is divisible by i.
2. i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 15


'''
'''
We can use usual backtracking and count answer, but potentially it is quite expensive, like O(n!).

Alternative approach is to use dynamic programming with bitmasks. The idea is to use function dp(mask, place), where:

mask is binary mask for visited numbers.
place is current place we want to fill. 
Idea is to start from the end, and fill places in opposite direction, because for big numbers we potentially have less candidates. (if we start form pl = 0 and go in increasing direction, then it is also will work fine, like 120ms vs 60ms)
Now, let us discuss how dp(mask, place) will work:

If we reached place 0 and procces was not interrupted so far, it means that we found beautiful arrangement.
For each number 1, 2, ..., N we try to put this number on place pl: and we need to check two conditions:
1. first, that this place is still empty, using bitmask 
2. and secondly that one of the two properties for beutiful arrangement holds.
In this case we add dp(mask^1<<i, place - 1) to final answer.
Finally, we run dp(0, N): from the last place and with empty bit-mask.
Complexity: First of all, notice that we have 2^N possible options for mask, N possible options for place.
But in all we have only 2^N states: pl is uniquely defined by number of nonzero bits in bm. Also we have N possible moves from one state to another, so time complexity is O(N*2^N). Space complexity is O(2^N).


'''

class Solution:
    def countArrangement(self, n: int) -> int:
        
        memo = { }
        
        
        def dp(mask, place):
            if place == 0:
                return 1
            
            if (mask, place) in memo:
                return memo[(mask, place)]
            
            ans = 0
            
            for i in range(n):
                if not mask & (1 << i) and ((i + 1) % place == 0 or place % (i + 1) == 0):
                    ans += dp(mask ^ (1 << i), place - 1)
            
            memo[(mask, place)] = ans
            
            return ans
        
        
        return dp(0, n)
        