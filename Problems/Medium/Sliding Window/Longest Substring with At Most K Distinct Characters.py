'''
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 10^4
0 <= k <= 50

'''

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start, max_length = 0, float("-inf")
        d = {}
        for end in range(len(s)):
            
            #Fill in hashmap with frequency of character
            if s[end] not in d:
                d[s[end]] = 1
            else:
                d[s[end]] += 1
            #Since size of the hashmap shows how many distinct characters we have
            #we can start shirnking start pointer of sliding window and as we shrink
            #we check if frequency of our character is equal to zero, if it is - delete it from hashmap
            while len(d) > k:
                d[s[start]] -= 1
                
                if d[s[start]] == 0:
                    del d[s[start]]
                #Continue moving start pointer of sliding window
                start += 1
            #Since the condition is 'at most' K distinct character 
            #We keep track the length everytime this condition is met
            if len(d) <= k:
                max_length = max(max_length, end - start + 1)
        return max_length