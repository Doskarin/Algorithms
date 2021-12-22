'''
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.
 

Example 1:

Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
 

Constraints:

1 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
target is an integer from nums.
At most 10^4 calls will be made to pick.

'''

class Solution:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        

    def pick(self, target: int) -> int:
        from random import randint
        count = 0
        idx = None
        for index, num in enumerate(self.nums):
            if num == target:
                count += 1
                chance = randint(1, count)
                if chance == count:
                    idx = index
        return idx
        
    '''
    Reservoir sampling is a technique which
    is used to generate numbers randomly when 
    we have a large pool of numbers. 
    As mentioned in the note for this question,
    the array size can be large, hence it is a
    reasonable choice to use Reservoir Sampling.
    Consider an array of size nn from which we
    need to chose a number randomly. Consider
    these numbers to be coming in the form of a stream,
    hence at each step, we have to take the decision of 
    whether or not to choose a given number, such that the 
    overall probability of each number being chosen is same (1/n in this case).
    If we have total of n numbers and we pick the ith number, this implies that
    we do not pick any number further from index (i + 1) to n. In terms of
    probability, this can be represented as (1/i) * (i/i+ 1) *(i + 1/i + 2)*... *(n - 1/n)
    This can be interpreted as 
    - Picking the ith number from the list of i numbers
    - Not picking the (i + 1)th number from the list of (i + 1) numbers. Hence picking any
    any of the remaining i numbers
    - And so on..
    - Not picking nth number from the list of n numbers. Hence picking
    any of the remaining (n - 1) numbers

    Upon simplifying the above expression we can see that the probablity
    of chosing any number at the ith step comes out to be 1/n.
    Hence we can say reservoir sampling allows us to choose any number uniformly at
    random from the list of n numbers
    Note that for any i, the decision of whether or not to choose this ith
    number depends on the first term of the above mentioned expression, which is 
    1/i. In general, if count represents the total number of numbers we have 
    from which we need to chose a random number uniformly,
    we chose such a number with probability 1/count
    ​This is what we will be doing here.
    
    Time : O(N) for pick method
    
    Space : O(1), not extra space used in the process
    
    
    '''
    def __init__(self, nums: List[int]):
        from collections import defaultdict
        
        self.d = defaultdict(list)
        for index, num in enumerate(nums):
            self.d[num].append(index)
        

    def pick(self, target: int) -> int:
        from random import randint
        index = randint(0, len(self.d[target]) - 1)
        return self.d[target][index]
    
    '''
    Time : O(N), to create hashmap
    
    Space : O(N), to store indices in a hashmap   
    
    
    '''