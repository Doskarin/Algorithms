'''
Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

 

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
Example 2:

Input: s = "abbababa", k = 1
Output: true
 

Constraints:

1 <= s.length <= 1000
s consists of only lowercase English letters.
1 <= k <= s.length

'''

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        memo = { }
        
        def dp(l, r):
            if l == r:
                return 0
            
            if r - l == 1:
                return int(s[l] != s[r])
            
            if (l, r) not in memo:
                
                if s[l] == s[r]:
                    memo[(l, r)] = dp(l + 1, r - 1)
                else:
                    memo[(l, r)] = 1 + min(dp(l + 1, r), dp(l, r - 1))
            
            return memo[(l, r)]
        
        return dp(0, len(s) - 1) <= k
    
    '''
    Time : O(N^2)
    
    Space : O(N)
    
    '''