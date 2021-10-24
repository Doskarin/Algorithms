'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #For this problem we use monotonic stack to keep track of closest warmer day
        #Consider following example : [73,74,75,71,69,72,76,73]
        #Initially [0] is in our stack which corresponds to temperature of 73
        #Next up is index 1 with temperature of 74 therefore we pop until there is no temperature
        #that is less than our current temperature of 74
        #As we pop indices from the stack we assign index - idx to output[idx] corresponding to the
        #number of days between certain day and closest warmer one
        
        stack = [-1]
        output = [None] * len(temperatures)
        for index, temp in enumerate(temperatures):
            
            while stack[-1] != -1 and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                output[idx] = index - idx
            stack.append(index)
        #If it happens that some elements are left at the end
        #it means that there were no warmer days ahead of these days
        #for example consider stack [76, 73, 72,..] - for these days the answer will be 0
        while stack:
            output[stack.pop()] = 0
        
        return output