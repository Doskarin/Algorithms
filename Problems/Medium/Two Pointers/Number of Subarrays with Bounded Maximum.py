'''
Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Example 2:

Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= left <= right <= 10^9

'''

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        prev = -1
        total = 0
        count = 0
        for i in range(len(nums)):
            #If number is in range we set count value and then add it to the total
            #Consider following example : left = 2, right = 6
            #0 0 0 0 1 1 1 2 2 3 3 5 6 7 8
            #              ^
            #Till index 7 we would be adding 0 to the total but at index 7 our count becomes i - prev
            # = 7 - (-1) = 8, i.e 8 subarrays where 2 is maximum:
            #1. [0 0 0 0 1 1 1 2]
            #2.   [0 0 0 1 1 1 2]
            #3.     [0 0 1 1 1 2]
            #4.       [0 1 1 1 2]
            #5.         [1 1 1 2]
            #6.           [1 1 2]
            #7.             [1 2]
            #8.               [2]
            if left <= nums[i] <= right:
                count = i - prev
                
            #Whenever we meet the number that is greater than our higher bound
            #reset count to 0
            elif nums[i] > right:
                prev = i
                count = 0
            total += count
            
        return total