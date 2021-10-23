'''
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.


Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5

'''

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        low, high = 0, len(nums) - 1
        #Continue to increase low pointer until property of sorted array holds
        while low < len(nums) - 1 and nums[low+1] >= nums[low]:
            low += 1
            
        #If low reached the last index it means that array is already sorted
        #so we return 0
        if low == len(nums) - 1:
            return 0
        #Continue shrinking high pointer until property of sorted array holds
        while high >= 0 and nums[high] >= nums[high - 1]:
            high -= 1
            
        #Now we need to define min and max value inside of subarray [low , high]
        #because we could potentially have to expand our boundaries further
        #consider following example
        # 1 3 5 6 4 -999 15 999 16 17 18
        #       ^               ^
        #      low              high
        #initially we would stop at indices low = 3 and high = 8
        #and seemingly answer would high - low + 1 = 8 - 3 + 1 = 6 which is wrong
        #because as one can notice there are still values like -999 and 999
        #which would force our subarray boundaries to expand
        #more generally, if we break down array into subarray following property should hold:
        #[min1,...,max1] [min2,...,max2] [min3,...,max3] --> where minimum value of the second
        #subarray should always be greater than any value of the previous subarray
        #same applies to the maximum
        dmin, dmax = float('inf'), float('-inf')
        for i in range(low, high + 1):
            if nums[i] < dmin:
                dmin = nums[i]
            if nums[i] > dmax:
                dmax = nums[i]
        
        #As long as there are greater numbers than our minimum - continue expanding leftwards
        while low > 0 and nums[low - 1] > dmin:
            
            low -= 1
            
        #As long as there are numbers that are less than our maximum - continue expanding rightwards
        while high < len(nums) - 1 and nums[high + 1] < dmax:
            
            high += 1
        #return the width of subarray
        return high - low + 1