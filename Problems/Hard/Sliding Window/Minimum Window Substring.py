'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?


'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Initialize hashmap of pattern t to keep track of characters so far
        c = Counter(t)
        
        #Variable minimum start to return an actual answer
        min_start = 0
        
        #Sliding window start
        start = 0
        
        #Smallest possible window
        smallest = float('inf')
        
        #Number of matched letter from pattern
        matched = 0
        n = len(s)
        m = len(t)
        
        for end in range(n):
            #If character appears in our pattern decrease its freq
            #by 1. If its frequency more than or equal to zero (meaning that we are matching just enough letter)
            #we increase number of matched words by 1. 
            #Consider example s = 'aaaa' and t = 'aaa' - when we match 3 a's we do not need to match 4th one
            if s[end] in c:
                c[s[end]] -= 1
                
                if c[s[end]] >= 0:
                    matched += 1
                    
            #Whenever we reach the target first of all compare it with the smallest window we found
            #Save beginning of sliding window as left = s[start] and only then move it forward
            #If left character appears to be in our hashmap we check if its frequency is greater
            #or equal to 0, if it is - decrease number of matched character by one and increase its frequency
            #by one
            while matched == m:
                if end - start + 1 < smallest:
                    smallest = end - start + 1
                    min_start = start
                    
                left = s[start]
                start += 1
                if left in c:
                    if c[left] >= 0:
                        matched -= 1
                    c[left] += 1
        return s[min_start : min_start + smallest] if smallest != float('inf') else ""