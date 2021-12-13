'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4

'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)
        
        
        
    def quickSelect(self, nums, left, right, k_smallest):
        import random
        # if the list contains only one element - return that element
        if left == right:
            return nums[left]
        
        # Select a random pivot_index between
        pivot_index = random.randint(left, right)
        
        # find the pivot position in a sorted list
        pivot_index = self.partition(nums, left, right, pivot_index)
        
        #the pivot is in its final sorted position and we can return the element
        if k_smallest == pivot_index:
            return nums[k_smallest]
        
        #if k_smallest is smaller than pivot_index it means we need to explore left part
        elif k_smallest < pivot_index:
            return self.quickSelect(nums, left, pivot_index - 1, k_smallest)
        
        #Explore right part
        else:
            return self.quickSelect(nums, pivot_index + 1, right, k_smallest)
        

    def partition(self, nums, left, right, pivot_index):
        
        pivot = nums[pivot_index]
        
        # 1. Move pivot ti end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        # 2. Move all smaller elements to the left
        store_index = left
        
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        # 3. Move pivot to its final place
        nums[store_index], nums[right] = nums[right], nums[store_index]
        
        return store_index
    
    
    '''
    Time : O(N) in the average case, O(N^2) in the worst case
    Space : O(1) ???
    
    
    '''