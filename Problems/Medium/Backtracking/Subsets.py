'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

'''


class Solution:
    #Backtracking solution
    def subsets_backtracking(self, nums: List[int]) -> List[List[int]]:
        
        
        #Backtracking method
        #keeps track of current index and combination we have so far
        #Since we need to output all possible combinations
        #we append everytime we enter backtrack function
        
        def backtrack(i, comb):
            ans.append(comb[:])
            
            for j in range(i, len(nums)):
                comb.append(nums[j])
                backtrack(j + 1, comb)
                comb.pop()
                
        ans = []
        backtrack(0, [])
        
        return ans
    
    #Bit manipulation
    def subsets_bit(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        #There are 2^n combinations
        #for example for 3 elements in an array there are 2^3 = 8 combinations [1,2,3]
        #000 - 0 -  []
        #001 - 1 - [3]
        #010 - 2 - [2]
        #011 - 3 - [2,3]
        #100 - 4 - [1]
        #101 - 5 - [1,3]
        #110 - 6 - [1,2]
        #111 - 7 - [1,2,3]
        
        
        for mask in range(1 << n):
            cur_subset = []
            for j in range(n):
                #Check what bit is set in the mask
                #and append corresponding element
                if mask & (1 << j):
                    cur_subset.append(nums[j])
            output.append(cur_subset)
        return output