'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.

'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        #Create two separate stack
        # Stack [] - to track balanced parenthesis '()'
        # Stars [] - to track stars that could potentially
        # help us at the end to match unmatched brackets
        # whether it's open or closed ones
        # Since relative position of both start and brackets
        # matter, we will be storing indices
        stack = []
        stars = []
        for index, char in enumerate(s):
            #If stack is not empty and element at the last
            #index of the stack is equal to opening bracket
            #and current element is closing one - we pop
            if stack and char == ')' and s[stack[-1]] == '(':
                stack.pop()
            #if current character is star - we push it
            #to the corresponding stack - stars
            elif char == '*':
                stars.append(index)
            else:
                #if current character is opening bracket
                #push it to the stack
                if char == '(':
                    stack.append(index)
                    
                #if current character is closing bracket
                #and we do not have anything to match it with
                #from the stars stack - it means we will never
                #be able to match it in the future - return False
                elif char == ')':
                    if not stars or stars[-1] > index:
                        return False
                    #else if stars is not empty and latest index
                    #of star happens before current index - we use it
                    #to match closing bracket and therefore pop it
                    #from stars stack
                    else:
                        if stars and stars[-1] < index:
                            stars.pop()
        
        #At the end we could be having situation where
        #there are still some opening stacks that are left in 'stack' stack
        #consider following example :
        #['(', '(', '(', ...]
        #in order to match them we need to check if we have anything
        #at our balance of stars and we need to make sure indices of these
        #stars are greater than indices of unmatched brackets
        p_stack, s_stack = len(stack) - 1, len(stars) - 1
        while p_stack >= 0 and s_stack >= 0 and stars[s_stack] > stack[p_stack]:
            p_stack -= 1
            s_stack -= 1
        
        #at the end, if our p_stack pointer reached the beginning
        #it means we matched every unmatched opening bracket
        return p_stack == -1