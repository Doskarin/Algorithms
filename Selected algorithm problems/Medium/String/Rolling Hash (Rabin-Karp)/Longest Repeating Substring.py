'''
Given a string s, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

Example 1:

Input: s = "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: s = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: s = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: s = "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
 
Constraints:

The string s consists of only lowercase English letters from 'a' - 'z'.
1 <= s.length <= 1500

'''
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        
        n = len(s)
        #Search method in order to explore particular window sizes
        #and find if there are any repeating hashes in the process
        def search(window):
            h = 0
            #Prefill hash for initial window
            for i in range(window):
                h = (h * a + lookup[i]) % mod
                
            #Add hash to the seen set
            seen = {h}
            
            #Precalculate constant in order to account for highest power in a hash
            aL = pow(a, window, mod)
            #Explore all hashes of substrings of size window
            for i in range(1, n - window + 1):
                h = (h * a - lookup[i - 1] * aL + lookup[i + window - 1]) % mod
                #If this hash is in seen it means this substring is repeating and
                #we can return True
                if h in seen:
                    return True
                seen.add(h)
            #We have not seen repeating hash hence return False
            return False
        
        lookup = [ord(s[i]) - ord('a') for i in range(n)]
        a = 26
        mod = 2**31 - 1
        
        #Define search space of windows ranging from smallest one 1 and biggest one (size - 1)
        left, right = 1, len(s) - 1
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            #If search return True it means window size of mid has repeating hashes
            #Therefore we can explore bigger window sizes and proceed with left = mid + 1
            #while keeping in mind that we have to save best result we found so far
            if search(mid):
                ans = mid
                left = mid + 1
            #Otherwise shrink towards the left
            else:
                right = mid - 1
        return ans