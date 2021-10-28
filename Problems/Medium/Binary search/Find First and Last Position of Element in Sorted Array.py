'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9

'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #We use two binary search approach
        
        
        #Left binary search - to find leftmost element
        
        def leftMost(nums):
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                #if we found desired element
                #we try moving as left as possible
                #while saving our potential last answer
                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return ans
        
        #Right binary search - to find rightmost element
        def rightMost(nums):
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                #if we found desired element
                #we try moving as right as possible
                #while saving our potential last answer
                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        
        return [leftMost(nums), rightMost(nums)]