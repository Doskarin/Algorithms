'''
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
Example 4:

Input: n = 2, k = 7
Output: ""
Example 5:

Input: n = 10, k = 100
Output: "abacbabacb"
 

Constraints:

1 <= n <= 10
1 <= k <= 100

'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def backtrack(chosen):
            #Base case - when length of chosen array
            #is equal to n - it means we found potential candidate
            if len(chosen) == n:
                
                #increate counter by one in order to keep track
                #if reached kth element
                self.count += 1
                
                #if counter is equal to k
                #it means we found kth lexicographically
                #smallest element
                if self.count == k:
                    #mark found flag and save the answer
                    self.found = True
                    self.ans = ''.join(chosen)
                return
                    
            else:
                #Since we need the answer in lexicographical order
                #we explore from a to b to c
                for char in ['a','b','c']:
                    #if there is something in our array
                    #and the last element is equal to current character
                    #we do not proceed with explroing
                    if chosen and chosen[-1] == char:
                        continue
                    
                    #if it happens that we have already found
                    #our word - just break
                    if self.found:
                        break
                        
                    #append current character to the array
                    chosen += [char]
                    
                    #Proceed with this array
                    backtrack(chosen)
                    
                    #Backtrack by popping lastly added element
                    chosen.pop()
                    
        self.count = 0
        self.found = False
        self.ans = ""
        
        backtrack([])
        return self.ans