'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


Example 1:


      |
  > | | <
    | |
    | |   |
    | | | |
| | | | | |
    
    ^ ^


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:

    |
    |
> | | <
  | |
  
  ^ ^
Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104



'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        #Instantiate stack with -1 so that it is never empty and we can have access to stack[-1] element
        stack = [-1]
        n = len(heights)
        
        for i in range(n):
            #If the last element of stack is not -1 and current height
            #is less than last element of the stack it means that last element is bounded
            #by our current index and whatever comes before that last element
            
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                #save index of lastly popped element of the stack, it will be our base
                #to calculate the area
                cur_idx = stack.pop()
                
                #Width is right boundary - left boundary - 1
                width = i - stack[-1] - 1
                
                #Finally update max area
                max_area = max(max_area, width * heights[cur_idx])
            stack.append(i)
        
        #If stack is not empty it means there can still be boundary cases with left limit being 0
        #and right element being size of the input array
        while stack[-1] != -1:
            cur_idx = stack.pop()
            width = n - stack[-1] - 1
            max_area = max(max_area, width * heights[cur_idx])
        return max_area