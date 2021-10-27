'''
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: nums = [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: nums = [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: nums = [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 

Constraints:

n == nums.length
1 <= n <= 3 * 10^4
-3 * 104 <= nums[i] <= 3 * 10^4

'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        #Consider following example 
        #[a,b,c,d,e,f,g]
        #We can have two possible cases:
        #Case 1: when maximum is in the middle
        #[...c,d,e,..] --> for this we just track max_global
        #Case 2: when maximum is comprised of some elements from left
        # + some elements from the right
        #[a,b,...,f,g] --> for this we have to make sure elements in dots
        #are as small as possible and therefore we track min_global
        max_so_far, max_global = 0, nums[0]
        min_so_far, min_global = 0, nums[0]
        for num in nums:
            total += num
            max_so_far = max(max_so_far + num, num)
            max_global = max(max_so_far, max_global)
            min_so_far = min(min_so_far + num, num)
            min_global = min(min_so_far, min_global)
            
        return max(total - min_global, max_global) if max_global > 0 else max_global