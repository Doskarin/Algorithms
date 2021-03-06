'''
Given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
Example 4:

Input: nums = [5,2,4,1,7,6,8], target = 16
Output: 127
Explanation: All non-empty subset satisfy the condition (2^7 - 1) = 127
 

Constraints:

1 <= nums.length <= 15
1 <= nums[i] <= 10^6
1 <= target <= 10^6

'''

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        '''
        Sort the array, because subsequence is nothing but a subset.

        reason: A window can be maintained [imin,j] such that
        if A[imin]+A[j]<=target
        then,
        for all i such that imin<=i<j
        A[imin]+A[i] <= target is true.

        The idea is to find the imin for every j.
        Then,add all the possible subsequences that can be generated from this [imin,j] window.

        for a window [imin,j], we can change the max by reducing j.
        But,when imin changes the window shifts and the min+max<=target may not
        be true anymore.
        
        '''
        nums.sort()
        res = 0
        mod = 10**9 + 7
        n = len(nums)
        left, right = 0, n - 1
        
        '''
        No of subsequences for a window of [imin,j] are calculated as below:
        Example:
        sorted nums : [a,b,c,d]
        lets say a+d<=target.
        no of subsequences are:
            1)when max reduces the min+max cant exceed target,so
              [a,b,c,d], [a,b,c],[a,b],[a] => 3
            2)[a,b,c,d] gives [a,b,d],[a,c,d],[a,d] with same min+max
            3)[a,b,c] gives [a,c] with same min+max
            4)[a,b] doesnt give anything new
            5)[a] also remains same

        The key thing to observe here is that, [a ,......] is the pattern
        for every subsequence.
        The no of subsets of the rest of the numbers
        is the total no of subsequnces. i.e 1<<(numberofelements) or power(2,numberoflements)
        
        '''
        while left <= right:
            
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += pow(2, right - left, mod)
                left += 1
        return res % mod