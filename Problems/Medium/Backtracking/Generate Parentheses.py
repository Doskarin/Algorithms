'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def backtrack(left, right, path):
            #Base case : if left balance exceeded right one
            #or left one or right one is negative balance - backtrack
            if left > right or left < 0 or right < 0:
                return
            
            #if both balances are 0 it means
            #we found one of the combinations and should append it to the result
            #then backtrack
            if left == 0 and right == 0:
                res.append(path)
                return
                
            backtrack(left - 1, right, path + "(")
            backtrack(left, right - 1, path + ")")
        
        #Start if balance of n from both sides
        backtrack(n, n, "")
        return res