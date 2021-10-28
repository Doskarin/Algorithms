'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5


'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort an array in order to move two pointers
        nums.sort()
        n = len(nums)
        target = 0
        res = [ ]
        for i in range(n):
            #If current and previous elements are equal
            #we continue because we already explored all combinations
            #with this number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                
                #If current sum is equal to target we append 
                #three numbers to the result and move both pointers
                if curSum == target:
                    
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    #If current left element is equal to the previous one
                    #we continue expanding
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    #If current right element is equal to the previous one
                    #we continue expanding
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                #If current sum is too much
                #we decrease right pointer
                elif curSum > target:
                    right -= 1
                
                #If current sum is too small
                #we increase left pointer
                else:
                    left += 1
        return res