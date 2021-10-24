'''
Given a string s, return the number of distinct substrings of s.

A substring of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string.

 

Example 1:

Input: s = "aabbaba"
Output: 21
Explanation: The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
Example 2:

Input: s = "abcdefg"
Output: 28
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
 

Follow up: Can you solve this problem in O(n) time complexity?

'''

class Solution:
    def countDistinct(self, s: str) -> int:
        seen = set()
        
        #Modulus in order to avoid collisions and overflow
        mod = 2**63 - 1
        n = len(s)
        
        #Base that we will use in our rolling hash function
        a = 26
        #Lookup array to get unique values for letters
        lookup = [ord(s[i]) - ord('a') + 1 for i in range(n)]
        
        def search(window):
            #At the beginning hash is zero and we need to find initial one
            h = 0
            for i in range(window):
                
                #Fill in hash of size 'window'
                h = (h * a + lookup[i]) % mod
            
            #Add hash to the seen set
            seen.add(h)
            
            #Precalculate c constant which will help to account for highest power when moving hash
            c = pow(a, window, mod)
            for i in range(1, n - window + 1):
                #Start iterating over all possible windows
                h = (h * a - c * lookup[i - 1] + lookup[i + window - 1]) % mod
                #If hash is already in seen set - continue
                if h in seen:
                    continue
                #Otherwise add hash to the set
                seen.add(h)
            return
        
        #Check all possible windows starting from size 1 and size n
        for window in range(1, n + 1):
            #Each time we make a call on search method we wfill in seen set
            search(window)
        #Finally return size of seen set which will have all distinct substrings
        return len(seen)