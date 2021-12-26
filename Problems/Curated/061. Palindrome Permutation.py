'''
Given a string s, return true if a permutation of the string could form a palindrome.

 

Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
 

Constraints:

1 <= s.length <= 5000
s consists of only lowercase English letters.

'''

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        c = Counter(s)
        if len(s) % 2 == 0:
            for char in c:
                if c[char] % 2 != 0:
                    return False
        else:
            odd = 0
            for char in c:
                if c[char] % 2 == 1:
                    odd += 1
                    if odd > 1:
                        return False
        return True
    
    '''
    Time : O(N) , single pass
    
    Space : O(1), we are using hashmap which can get as big as O(26)
    
    
    '''