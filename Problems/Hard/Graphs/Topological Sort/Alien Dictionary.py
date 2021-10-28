'''
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegree = Counter({c : 0 for word in words for c in word})
        
        graph = defaultdict(set)
        #Build graph
        for first, second in zip(words, words[1:]):
            #Since words are given in sorted order
            #we need to check current and next words
            #the very first time when their
            #characters are not equal
            #it means we found edge in graph
            #We also keep track of indegrees
            for char1, char2 in zip(first, second):
                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                        indegree[char2] += 1
                    break
            else:
                if len(first) > len(second):
                    return ""
        output = []
        #Start with letter whose indegree is 0
        q = deque([c for c in indegree if indegree[c] == 0])
        
        while q:
            letter = q.popleft()
            #Popped letter has indegree of 0
            #and we can append it to the final result
            output.append(letter)
            for child in graph[letter]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        if len(output) != len(indegree):
            return ""
        
        return "".join(output)