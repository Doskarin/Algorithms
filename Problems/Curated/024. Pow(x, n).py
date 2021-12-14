'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= x^n <= 10^4

'''

class Solution:
    def myPow_rec(self, x: float, n: int) -> float:
        
        if n < 0:
            x = 1/x
            n = -n
            
        def power(num, p):
            if p == 0:
                return 1

            x = power(num, p // 2)
            
            if p % 2 == 0:
                
                return x * x
            
            else:
                return num * x * x
            
            
        return power(x, n)
    
    
    '''
    Time : O(logN), Each time we apply the formula (x^n)^2 = x^(2*n),
    n is reduced by half. Thus we need at most O(logn) computations to get
    the result
    
    Space : O(logN), For each computation, we need to store the result
    of x^(n/2). We need to do the computation for O(logN) times, so the space complexity is O(logN)
    
    
    '''

    class Solution:
        def myPow_iter(self, x: float, n: int) -> float:
            
            if n < 0:
                x = 1/x
                n = -n
                
            t = 1
            
            while n != 0:
                if n % 2 == 1:
                    t = x * t
                    n -= 1
                else:
                    x = x * x
                    n //= 2
            return t
                
    
    
    '''
    Time : O(logN), For each bit of n's binary representation,
    we will at most multiply once. So the total time complexity is O(logN)
    
    Space : O(1), We only need two variables for the current product
    and the final result of x
    
    
    '''