'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length


'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        queue = deque()
        
        #Build up initial double ended queue
        for i in range(k):
            #While last element is less than current element we keep popping
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        for i in range(k, len(nums)):
            #Since we are keeping decreasing queue
            #First element will always be our maximum so we can append it to the result
            output.append(nums[queue[0]])
            
            #To make sure we are within the bounds if the first elements
            #have indices less than or equal to i - k
            #Consider example
            #nums = [1,3,-1,-3,5,3,6,7], k = 3
            #                  ^ Here we are currently at index 4
            #and index of our maximum we have in our queue is 1 which
            #corresponds to the value of 3
            #Since its index is 1 <= 4 - 3 = 1 we need to pop it from the queue
            while queue and queue[0] <= i - k:
                queue.popleft()
            
            #To our queue decreasing we pop last element as long as
            #it's less than current elements
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
                
            queue.append(i)
        #At the end we are always left with queue with at least with 1 element
        #Append it to the result
        output.append(nums[queue[0]])
        
        return output