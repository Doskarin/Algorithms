'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length

'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #Define zero freq as our current number of zeros we have so far
        #this variable will be used to compare with k
        max_ones, start, zero_freq = 0, 0, 0
        for end in range(len(nums)):
            #whenever current value is equal to zero
            #increase zero freq by 1
            if nums[end] == 0:
                zero_freq += 1
            #While value of zero freq is greater than allowed quota
            #we try to move start pointer of sliding window and if it is equal to zero
            #decrease freq by 1
            
            while zero_freq > k and start < len(nums):
                if nums[start] == 0:
                    zero_freq -= 1
                start += 1
                
            #After finishing this loop it is assured that we are not overusing given quota
            #and can save max result
            max_ones = max(max_ones, end - start + 1)
        return max_ones