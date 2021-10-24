'''
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

Example 1:

Input: s = "banana"
Output: "ana"
Example 2:

Input: s = "abcd"
Output: ""
 

Constraints:

2 <= s.length <= 3 * 104
s consists of lowercase English letters.

'''
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        n = len(s)
        #Initialize lookup array in order to create rolling hash
        lookup = [ord(s[i]) - ord('a') + 1 for i in range(n)]
        
        #Base as in polynomial coefficients : s[0] + s[1] * a + s[2] * a^2 + ... + s[n - 1] * a^(n - 1)
        a = 26
        
        #In order to avoid collisions and overflow we use modulus
        mod = 2**35 - 1
        
        #Method to find repeating pattern for a given window size
        def find(window):
            
            h = 0
            
            #Instantiate the very first rolling hash base
            for i in range(window):
                h = (h * a + lookup[i])%mod
            seen = {h}
            #Calculate constant to account for biggest power of rolling hash
            c = pow(a, window,mod)
            for i in range(1, n - window + 1):
                #Moving rolling hash along the string
                h = (h * a - c * lookup[i - 1] + lookup[i + window - 1])%mod
                #If hash is in seen set it means we found duplicate and can return index
                if h in seen:
                    return i
                seen.add(h)
            return -1
        
        
        
        
        left, right = 1, n
        
        #Binary search for largest window size possible : 1 - smallest window size, n - 1 - largest possible size
        while left <= right:
            mid = left + (right - left) // 2
            
            #If we returned some index it means we found the window size and can still expand its size
            if find(mid) != -1:  
                left = mid + 1
            else:
                #Shrink otherwise
                right = mid - 1
        #Left - 1 to account for last successful iteration
        window = left - 1
        start = find(window)
        return s[start:start + window] if start != -1 else ""

