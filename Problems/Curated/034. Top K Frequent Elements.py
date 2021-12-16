'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        
        buckets = [[] for _ in range(len(nums) + 1)]
        
        counter = Counter(nums)
        for num, freq in counter.items():
            buckets[freq].append(num)
        
        result = []
        j = len(buckets) - 1
        
        while k:
            
            if not buckets[j]:
                j -= 1
                continue
                
            for num in buckets[j]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result
                
            if k == 0:
                return result
            j -= 1
    '''
    Time : O(N), because we first iterate over nums
    once and create buckets, then we flatten list of lists with total number of elements
    
    Space : O(N), hashmap and buckets at worst could be O(N)
    
    '''