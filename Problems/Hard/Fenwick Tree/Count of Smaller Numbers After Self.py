'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

'''
#Binary Indexed tree structure will help us
#to make fast queries in logn time
class BIT:
    
    def __init__(self, size):
        #Tree size is twice the size to accomodate offset
        #negative numbers
        self.tree = [0] * (2*size + 1)
        self.size = len(self.tree)
        
    def query(self, index):
        
        total = 0
        while index != 0:
            total += self.tree[index]
            index -= index & -index
        return total
    
    def update(self, index, val):
        index += 1
        while index < self.size:
            self.tree[index] += val
            index += index & -index
            
    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        #Offset in order to account for negative numbers
        offset = 10**4
        tree = BIT(offset)
        ans = []
        for num in reversed(nums):
            #Count how many number are less than
            #than our current number
            count = tree.query(num + offset)
            ans.append(count)
            #update current num as index in the tree
            #with value of 1
            tree.update(num + offset, 1)
            
        return ans[::-1]