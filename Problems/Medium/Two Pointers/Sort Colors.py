'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        The idea here is the following: we keep 3 pointers: for each of colors (numbers). I called them
beg = 0, mid = 0, end = len(nums) - 1. The idea here is to put sorted 0 and 1 to the beginning and sorted 2s to the end. Then we iterate over all elements and process each new element in the following way. Imagine, that we already sorted some of the elements, our invariant will be 00...0011...11......22....22, where we already put some 0 and 1 in the beggining and some 2 to the end. Then there are 3 possible optinos for new element ?:

00...0011...11?......22....22, where ? = 1, then we do not need to change any elements, just move mid pointer by 1 to the right.
00...0011...11?......22....22, where ? = 2, then we need to put this element befor the first already sorted 2, so we change these elements and then move pointer end by 1 to the left.
00...0011...11?......22....22, where ? = 0, then we need to swap this element with the last sorted 0 and also move two pointers mid and beg by 1.
We can see it this way, that pointers beg, mid and end always point at elements just after the last 0, after the last 1 and before the first 2.
        """
        n = len(nums)
        p0, p2 = 0, n - 1
        curr = 0
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1