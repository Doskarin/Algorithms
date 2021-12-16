'''
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.

'''

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        from itertools import lru_cache
        @lru_cache(None)
        def dfs(i, balance):
            ans = set()
            
            if balance < 0:
                return ans
            
            if i == len(s):
                if balance == 0:
                    ans.add("")
                return ans
                
            if s[i] == "(" or s[i] == ")":
                ans.update(dfs(i + 1, balance))
            
            if s[i] == "(":
                balance += 1
                
            elif s[i] == ")":
                balance -= 1
                
            for suffix in dfs(i + 1, balance):
                ans.add(s[i] + suffix)
            
            return ans
        
        valid = dfs(0, 0)
        
        maxLen = len(max(valid, key = len))
        
        return filter(lambda x : len(x) == maxLen, valid)
    
    
    
    '''
    Time : O(2^N)
    
    Space : O(N)
    
    '''