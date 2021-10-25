'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500

'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #Main backtracking method to keep track of current remainder
        #combination we have so far and current index
        def backtrack(remainder, comb, index):
            #Base case - remainder is zero it means
            #we found our taget value and can append
            #candidate array to the answer
            #then return (backtrack)
            if remainder == 0:
                output.append(comb[:])
                return
            #If remainder is less than zero
            #it means we exceeded the target
            #and should backtrack to continue exploring
            if remainder < 0:
                return
            
            #iterate through candidates and explore some options
            for i in range(index, len(candidates)):
                
                #Append current number to combinations list
                comb.append(candidates[i])
                
                #Pass remainder minus current candidate
                #We pass index i because we could be reusing the same
                #number over and over again until we exhaust the remainder
                backtrack(remainder - candidates[i], comb, i)
                
                #backtrack by popping last element
                comb.pop()
        output = []
        backtrack(target, [], 0)
        return output