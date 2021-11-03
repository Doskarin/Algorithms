'''
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 

Constraints:

1 <= nums.length <= 2 * 10^4
1 <= nums[i] < 2^16
1 <= k <= floor(nums.length / 3)

'''

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        curSum = 0
        window_sums = [0] * n
        
        #Build all window sums
        #ending at index i
        for i in range(n):
            curSum += nums[i]
            if i >= k:
                curSum -= nums[i - k]
            window_sums[i] = curSum
        
        largestIndex = 0
        #Build the largest sum seen from left
        left = [0] * n
        for i in range(n):
            if window_sums[i] > window_sums[largestIndex]:
                largestIndex = i
            left[i] = largestIndex
        
        #Build the largest sum seen from right
        right = [0] * n
        largestIndex = n - 1
        for i in range(n - 1, -1, -1):
            #assures we look at lexicographically smallest
            #possible result
            if window_sums[i] >= window_sums[largestIndex]:
                largestIndex = i
            right[i] = largestIndex
        
        ans = None
        maxSum = -1
        #Now starting from mid each time
        #try looking at left and right
        #non-overlapping sums
        #and keep track of max sum
        for j in range(2*k - 1, n - k):
            l, r = left[j - k], right[j + k]
            
            if not ans or window_sums[l] + window_sums[j] + window_sums[r] > maxSum:
                maxSum = window_sums[l] + window_sums[j] + window_sums[r]
                ans = l - k + 1, j - k + 1, r - k + 1
        return ans