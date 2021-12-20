'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5


'''

class Solution:
    def trap_dp(self, height: List[int]) -> int:
        
        n = len(height)
        
        left = [0] * n
        max_from_left = 0
        for i in range(n):
            left[i] = max_from_left
            max_from_left = max(max_from_left, height[i])
            
        right = [0] * n
        max_from_right = 0
        for i in range(n - 1, -1, -1):
            right[i] = max_from_right
            max_from_right = max(max_from_right, height[i])
            
        output = [0] * n
        
        for i in range(n):
            if min(left[i], right[i]) > height[i]:
                output[i] += min(left[i], right[i]) - height[i]
                
        return sum(output)
    
    '''
    Time : O(N), three passes to build left, right and fill in the output
    Space : O(N), three auxiliary arrays    
    
    '''

    def trap_two_pointers(self, height: List[int]) -> int:
        
        '''
        Let's look at the maximum_left,
        maximum_right, lower_bound
        used in dynamic programming
        and think about how to improve them. 

        height =         [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        maximum_left =   [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
        maximum_right =  [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
        lower_bound =    [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0]
        water_trap_at_i =[0, 0, 1, -1, 1,2, 1, -1,0, 1, -1, 0]  

        ✨Are they necessary?✨
        No. they are not.  
        We only need store them as variables.
        l_max: moving from left to right, 
        updating the maximum height seeing so far.
        r_max: moving from right to left,
        updating the maximum height seeing so far.
        It becomes 2 pointers moving towards to each other.

        height =         [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
                          ^                                ^
        l = 0, r = 11     l_max = 0                        r_max = 1   answer = 0
                             ^                          ^
        l = 1, r = 10     l_max = 1                     r_max = 2      answer = 0
        
        '''
        left, right = 0, len(height) - 1
        
        left_max, right_max = 0, 0
        
        total = 0
        
        while left < right:
            
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total += left_max - height[left]
                left += 1
                
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total += right_max - height[right]
                right -= 1
        return total
    
    '''
    Time : O(N)
    
    Space : O(1)
    
    '''