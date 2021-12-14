'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
                
        i = len(nums) - 1
        while i >= 1 and nums[i - 1] >= nums[i]:
            i -= 1
        
        if i != 0:
            
            j = i
            while j + 1 < len(nums) and nums[j + 1] > nums[i - 1]:
                j += 1
            
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            
        reverse(nums, i, len(nums) - 1)
        
        return nums
    
    '''
    Time : O(N) - one pass
    Space : O(1)
    '''