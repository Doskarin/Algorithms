'''
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 
Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
 

Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length

'''

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #Since we are allowed to take both from start and end only
        #k divides an array into two parts : one consisting only of
        #beginning, ending or both beginning and ending cards
        #for example : cardPoints = [1,2,3,4,5,6,1], k = 3
        #we can divide an array into [1,2] [3,4,5,6] [1] or [1,2,3] [4,5,6,1] etc
        #If we define two subarrays as X and Y, where X - is our card we are allowed to take
        #and Y - remaining part in the middle then
        # X = total -  Y, in order for X to be maximized Y should minimized
        #For this we create prefix array and using sliding window of size k
        #scan through prefix array and find smallest possible window
        n = len(cardPoints)
        window = n - k
        prefix = [0] + [num for num in cardPoints]
        #Build prefix array
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        
        smallest = float("inf")
        
        for i in range(n - window + 1):
            #Find smallest possible window
            current = prefix[i + window] - prefix[i]
            if current < smallest:
                smallest = current
        #Maximum possible points we can get is total - smallest window values
        return prefix[-1] - smallest