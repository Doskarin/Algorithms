'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 10^8

'''

class Solution:
    def maximumSwap_1(self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        # At each digit, if there is a larger digit that occurs later,
        # we want the swap it with the largest such digit that occurs the latest.
        last = {x : i for i, x in enumerate(nums)}
        
        for index, x in enumerate(nums):
            
            for candidate in range(9, x, -1):
                if candidate in last:
                    if last[candidate] > index:
                        
                        nums[last[candidate]], nums[index] = nums[index], nums[last[candidate]]
                        
                        return int("".join(map(str,nums)))
        return num
    
    
    '''
    Time : O(N) - one pass using hashmap with last occurrences
    Space : O(N) - hashmap to store last occurrences of a number
    
    '''
    def maximumSwap_2(self, num: int) -> int:
        
        
        nums = [x for x in str(num)]
        if len(nums) == 1:
            return num
        
        largest = "".join(nums)
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                    
                nums[i], nums[j] = nums[j], nums[i]
                
                if "".join(nums) > largest:
                    largest = "".join(nums)
                
                nums[i], nums[j] = nums[j], nums[i]
                
        return int(largest)
    
    '''
    Time : O(N^2)
    Space : O(N)
    
    '''