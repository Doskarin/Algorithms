'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is either'(' , ')', or lowercase English letter.


'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        s = self.remove_invalid_closing(s, "(", ")")
        s = self.remove_invalid_closing(s[::-1], ")", "(")
        
        return s[::-1]
        
    def remove_invalid_closing(self, string, open_symbol, close_symbol):
        sb = []
        balance = 0
        for char in string:
            
            if char == open_symbol:
                balance += 1
                
            elif char == close_symbol:
                if balance == 0:
                    continue
                balance -= 1
                
            sb.append(char)
            
        return "".join(sb)
    
    '''
    Time : O(n)
    Space : O(n) - still linear but constants are smaller
    
    '''
    
    def minRemoveToMakeValid_2(self, s: str) -> str:
        
        stack = []
        
        
        for index, char in enumerate(s):
            if stack and char == ")" and s[stack[-1]] == "(":
                stack.pop()
                
            elif char in "()":
                stack.append(index)
        
        valid_string = "".join([char for index, char in enumerate(s) if index not in set(stack)])
        
        return valid_string
    
    '''
    Time : O(n) - Iterate twice through original string and String builder
    Space : O(n) - Stack, Set and String builder
    
    '''