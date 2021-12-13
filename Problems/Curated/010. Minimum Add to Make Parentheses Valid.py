'''
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
Example 3:

Input: s = "()"
Output: 0
Example 4:

Input: s = "()))(("
Output: 4
 

Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.


'''

class Solution:
    def minAddToMakeValid_1(self, s: str) -> int:
        
        stack = []
        
        for char in s:
            
            if stack and stack[-1] == "(" and char == ")":
                
                stack.pop()
                
            else:
                stack.append(char)
                
        return len(stack)
    
    '''
    Time : O(N) - one pass
    Space : O(N) - stack to keep all elements

    '''

    def minAddToMakeValid_2(self, s: str) -> int:
        ans = balance = 0
        
        for char in s:
            
            balance += 1 if char == "(" else -1
            
            if balance == -1:
                ans += 1
                balance += 1
                
        return ans + balance
    
    '''
    Time : O(N) - one pass
    Space : O(1) - no extra space is used
    
    
    '''