'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Same as subset I but this time we need to 
        #initially sort to account for duplicates as we go
        nums.sort()
        
        def backtrack(i, comb):
            res.append(comb[:])
            
            for j in range(i, len(nums)):
                if i != j and nums[j] == nums[j - 1]:
                    continue
                comb.append(nums[j])
                backtrack(j + 1, comb)
                comb.pop()
        
        res = []
        backtrack(0, [])
        
        return res