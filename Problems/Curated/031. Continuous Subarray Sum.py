'''
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 2^31 - 1
1 <= k <= 2^31 - 1

'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        '''
        -1 is just before you start the index. 
        So if you get the first 2 elements sum to k,
        your current i is 1. So 1 - (-1) = 2 still satisfies the return True condition.
        
        '''
        d = {0 : -1}
        running_sum = 0
        
        '''
        If sum(nums[i:j]) % k == 0 for some i < j, 
        then sum(nums[:j]) % k == sum(nums[:i]) % k. 
        So we just need to use a dictionary to keep track of sum(nums[:i]) % k
        and the corresponding index i. 
        Once some later sum(nums[:i']) % k == sum(nums[:i]) % k 
        and i' - i > 1, we return True.
        '''
        for index, num in enumerate(nums):
            running_sum = (running_sum + num) % k
            
            if running_sum in d:
                if index - d[running_sum] >= 2:
                    return True
            else:
                d[running_sum] = index
        
        return False
    
    '''
    Time : O(N) - one pass with running sum 
    Space : O(min(k, N))
    
    '''