'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length

'''

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        '''
        
        The nice part about this question: 
        the indices can help us to get all the positive 
        numbers in sorted order (i + 1 if i denotes the index)
        Hence, A[i] - (i + 1) will be # of missing 
        positives at index i, and this will be our 3rd sorted sequences
        i.e.

        A:            [1,3,4,6]
        A[i] - (i+1): [0,1,1,2]
        let's call array A[i]-(i+1) as B,
        which is [0, 1, 1, 2] above, then B[i]
        represents how many missing positives so far at index i.

        So the question becomes: finding the largest index of array B so that B[j] is smaller than K.
        
        After while loop is stopped,
        l - 1 is our target index because,
        B[l - 1] represents how many positive 
        is missing at index l - 1 that is smaller
        than K, so result is A[l -1](the largest 
        number in A that is less than result) + K - B[l - 1](offset, how far from result)
        = (A[l - 1]) + (k - (A[l - 1] - l)) = l + k
               
        '''

        left, right = 0, len(arr)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
                
        return left + k
    
    '''
    Time : O(logN)
    
    Space : O(1)
    
    '''