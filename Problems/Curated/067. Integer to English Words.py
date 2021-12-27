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

class Solution:
    def numberToWords(self, num: int) -> str:
        
        ones = "One Two Three Four Five Six Seven Eight Nine "\
               "Ten Eleven Twelve Thirteen Fourteen Fifteen "\
               "Sixteen Seventeen Eighteen Nineteen".split()
        tens = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        #print(ones)
        
        if num == 0:
            return "Zero"
        
        def rec(i):
            if i == 0:
                return ""  
            
            if i <= 19:
                return ones[i - 1]
            
            if i <= 99:
                return (tens[i//10 - 2] + " " + rec(i % 10)).rstrip()
            
            if i <= 999:
                return (rec(i // 100) + " Hundred " + rec(i % 100)).rstrip()
            
            # 1 000 000
            #   999 999 - Thousands
            if i <= 10**6 - 1:
                return (rec(i // 10**3) + " Thousand " + rec(i % 10**3)).rstrip()
            
            # 1 000 000 000
            #   999 999 999
            if i <= 10**9 - 1:
                return (rec(i // 10**6) + " Million " + rec(i % 10**6)).rstrip()
            
            else:
                return (rec(i // 10**9) + " Billion " + rec(i % 10**9)).rstrip()
            
        return rec(num)
    
    """
    Time : O(N), the output is proportional to the number N of digits in the input
    Space : O(N), call stack
    
    
    """