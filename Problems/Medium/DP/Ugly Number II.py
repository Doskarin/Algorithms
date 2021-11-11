'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:

1 <= n <= 1690

'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        #All ugly number are multiples of either 2,3 or 5
        #Maintain list of ugly number starting from 1, which corresponds
        #to the multiplication of 2, 3 and 5 with the power of 0
        #We keep track of smallest pointers for corresponding factors
        two_pos, three_pos, five_pos = 0, 0, 0
        idx = 1
        res = [1]
        
        
        
        while len(res) < n:
            
            byTwo = res[two_pos] * 2
            byThree = res[three_pos] * 3
            byFive = res[five_pos] * 5
            #choose smallest of three and move its pointer
            minVal = min(byTwo, byThree, byFive)
            
            res.append(minVal)
            
            if minVal == byTwo:
                two_pos += 1
                
            if minVal == byThree:
                three_pos += 1
                
            if minVal == byFive:
                five_pos += 1
                
        return res[-1]