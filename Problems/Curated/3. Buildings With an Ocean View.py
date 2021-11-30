'''
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
Example 4:

Input: heights = [2,2,2,2]
Output: [3]
Explanation: Buildings cannot see the ocean if there are buildings of the same height to its right.
 

Constraints:

1 <= heights.length <= 10^5
1 <= heights[i] <= 10^9

'''

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        
        for index, height in enumerate(heights):
            while stack and height >= heights[stack[-1]]:
                stack.pop()
                
            stack.append(index)
            
        return stack
    
    '''
    Time : O(N) - one pass
    Space : O(N) - Monotonic stack to maintain indices
    '''
    
    
    def findBuildings_2(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        output = []
        highest_from_right = [0] * n
        highest_so_far = 0
        
        for i in range(n - 1, -1, -1):
            highest_from_right[i] = highest_so_far
            highest_so_far = max(highest_so_far, heights[i])
        
        for i in range(n):
            if heights[i] > highest_from_right[i]:
                output.append(i)
        return output
    
    
    '''
    Time : O(N) - two pass: first to build heights_from_right array, second to check if ocean is seen from current building
    Space : O(N) - two arrays to maintain neccessary information
    
    '''