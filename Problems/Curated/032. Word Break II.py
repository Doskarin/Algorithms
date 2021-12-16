'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.


'''

class TrieNode:
    def __init__(self):
        self.children = { }
        self.isWord = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isWord = True
            


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        current = [ ]
        result = [ ]
        
        
        def dfs(i):
            if i == len(s):
                k = 0
                temp = []
                
                for i in current:
                    temp.append(s[k:i])
                    k = i
                
                result.append(" ".join(temp))
                return True
            
            
            cur = trie.root
            for j in range(i, len(s)):
                if s[j] in cur.children:
                    cur = cur.children[s[j]]
                    if cur.isWord:
                        current.append(j + 1)
                        dfs(j + 1)
                        current.pop()
                else:
                    return False
            return False
        dfs(0)
        
        return result
                        
        
        '''
        Time : O(N*len(string)) + 2^M), M = len(string) - all possible combinations
        Space : O(?)
        
        
        '''