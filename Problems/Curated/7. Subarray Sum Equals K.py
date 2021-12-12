'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        running_sum = 0
        d = { }
        total = 0
        for num in nums:
            
            running_sum += num
            
            if running_sum == k:
                total += 1
                
            if running_sum - k in d:
                total += d[running_sum - k]
                
            if running_sum not in d:
                d[running_sum] = 1
            else:
                d[running_sum] += 1
            
        return total
    
    '''
    Time : O(N), The entire nums array is traversed only once
    Space : O(N), Hashmap can contain up to N distinct entries in the worse case
    
    '''