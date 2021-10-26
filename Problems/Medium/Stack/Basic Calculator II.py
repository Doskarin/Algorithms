'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 10^5
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
The answer is guaranteed to fit in a 32-bit integer.

'''

class Solution:
    def calculate(self, s: str) -> int:
        #initiatlize number as 0, sign as plus
        #and empty stack
        num, sign, stack = 0, '+', []
        
        for i in range(len(s)):
            #If current character is a number
            #we need to build it up from scratch
            #there could be cases like 1, 12, 1234 or 12345 etc.
            if s[i].isdigit():
                num = 10 * num + int(s[i])
                
            #Once we encounter sign character or reached the end
            #we need to append corresponding number to the stack
            #depending on the operation
            if s[i] in '-+*/' or i == len(s) - 1:
                
                #If sign is a plus - just add number to the stack
                if sign == '+':
                    stack.append(num)
                    
                #If minus - add number with negative sign
                elif sign == '-':
                    stack.append(-num)
                    
                #If multiplication - we need to pop
                #last element of the stack and multiply it
                #with current number
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    #if division - do the same as in case with
                    #multiplication and keep in mind flooring
                    stack.append(int(stack.pop() / num))
                #reinitialize num to zero
                #and save the sign
                num = 0
                sign = s[i]
        
        #at the end we are left with the stack filled in
        #with numbers with intermediary result which we need to sum
        return sum(stack)