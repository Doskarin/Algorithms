'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.

'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                
                first_option = self.isPalindrome(s, left + 1, right)
                second_option = self.isPalindrome(s, left, right - 1)
                
                if first_option or second_option:
                    return True
                else:
                    return False
            left += 1
            right -= 1
            
        return True
         
    def isPalindrome(self, string, left, right):
        
        while left < right:
            
            if string[left] == string[right]:
                
                left += 1
                right -= 1
                
            else:
                return False
            
        return True
    
    '''
    Time : O(n) - Two Pointers in one pass
    Space : O(1) - No extra space is used in the process
    
    '''