'''
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.length)

'''

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        #Method to find if we can split array into m parts given particular threshold
        def canSplit(threshold):
            #Start with count 1
            count = 1
            total = 0
            for num in nums:
                total += num
                #If we already exceeded threshold we can move on
                if total > threshold:
                    #Increment number of subarrays
                    count += 1
                    total = num
# We can break the <= condition up:

# in the case that we are == m, it is possible to split the array into m subarrays, so this number is definitely a possibility
# For the "<" case, imagine a candidate for x that is much larger than our final solution would be. Since we are approaching this in a greedy manner, we would try and fit as many elements into a subarray as we can without hitting the upper limit x. Since this upper limit x is large, we may need a smaller number of subarrays to achieve this. And in general, the smaller we make x, the more subarrays we would need to fulfill our condition. By returning True for numSubarrays<m, we essentially signal to our binary search that we want to search in the search space to the left of the current x. So we would keep trying to drive x smaller in the process.
# A proof by contradiction, if you prefer: Assume for the sake of contradiction that we arrive at a value of x which is our final result, but the number of subarrays is smaller than m. We could always break up the largest sum subarray into two subarrays with smaller sums, thereby further minimizing our largest sum. Since we have now found a set of subarrays with smaller max sum, our x under consideration couldn't have been the final result. So we know that the final result that we return would have m subarrays.
                    if count > m:
                        return False
            return True
        
        left, right = max(nums), sum(nums)
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            
            if canSplit(mid):
                
                right = mid - 1
            else:
                left = mid + 1
        return left