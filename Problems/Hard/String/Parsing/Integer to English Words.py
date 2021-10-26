'''
Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

Constraints:

0 <= num <= 2^31 - 1

'''
#In this problem we could be having numbers up to 2^31 - 1
#which corresponds to 2 147 483 647
#Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Thousand Six Hundred Forty Seven
#That means that the largest we need to be aware of is billion

class Solution:
    def numberToWords(self, num: int) -> str:
        #First of all we need to take care of the most
        #elementary forms of the numbers in english
        #this correspond to number from 1 to 19
        ones = 'One Two Three Four Five Six Seven Eight ' \
               'Nine Ten Eleven Twelve Thirteen Fourteen ' \
               'Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        
        #As well as numbers from 20 to 90
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        
        if num == 0:
            return "Zero"
        
        #We will use recursion in order to build up
        #our solution starting from bigger chunks and finishing with smallest ones
        def rec(num):
            
            #Base case : if number is zero - return empty string
            if num == 0:
                return ""
            
            #If number is less than or equal to 19
            #Return corresponding english word from 'ones' array
            #being aware of indexing
            if num <= 19:
                return ones[num - 1]
            
            #Else if number is in range 20 - 99
            #we need to build string starting from tens
            #and continue building up whatever is left
            #rstrip is for getting rid of unneccessary spaces after
            #concatenation
            if num <= 99:
                return (tens[num//10 - 2] + " " + rec(num % 10)).rstrip()
            
            #Build up hundreds and whatever is left from modulo operation
            if num <= 999:
                return (rec(num//10**2) + " Hundred " + rec(num % 10**2)).rstrip()
            
            #Build up thousands and whatever is left from modulo operation
            if num <= 10**6 - 1:
                
                return (rec(num//10**3) + " Thousand " + rec(num % 10**3)).rstrip()
            
            #Build up millions and whatever is left from modulo operation
            if num <= 10**9 - 1:
                return (rec(num//10**6) + " Million " + rec(num % 10**6)).rstrip()
            
            #Build up billionsa and whatever is left from modulo operation
            else:
                return (rec(num//10**9) + " Billion " + rec(num % 10**9)).rstrip()
            
        return rec(num)