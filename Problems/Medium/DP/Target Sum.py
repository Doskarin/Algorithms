'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        memo = { }
        #We define state as (sum that we have at current index i)
        def dp(curSum, i):
            #if we already have this state present
            #in our cache - just return it
            if (curSum, i) in memo:
                return memo[(curSum, i)]
            #Base case - if index reached the end of an array
            #check if current sum achieved target, if yes - 
            #return 1 to the answer
            #return 0 if not
            if i == n:
                if curSum == target:
                    return 1
                else:
                    return 0
            #in the answer we explore both operation (addition and substraction)   
            ans = dp(curSum + nums[i], i + 1) + dp(curSum - nums[i], i + 1)
            
            #Finally, cache our result in memo
            memo[(curSum, i)] = ans
            
            return ans
        #Start with sum of 0 and index 0
        return dp(0, 0)