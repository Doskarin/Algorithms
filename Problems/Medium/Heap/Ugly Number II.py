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
        #Start heap with known value of 1
        #which the smallest ugly number
        q = [1]
        
        for _ in range(n - 1):
            #pop smallest value
            top = heappop(q)
            
            #keep popping if there are still values
            #equal to the smallest one left
            while q and top == q[0]:
                heappop(q)
            #push smallest value multiplied by 2,3 and 5   
            heappush(q, top * 2)
            heappush(q, top * 3)
            heappush(q, top * 5)
            
        #return last element left in the heap
        return q[0]