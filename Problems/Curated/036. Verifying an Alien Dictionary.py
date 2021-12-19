'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        c = {val : i for i, val in enumerate(order)}
        
        for word1, word2 in zip(words, words[1:]):
            
            for char1, char2 in zip(word1, word2):
                
                if c[char1] < c[char2]:
                    break
                    
                elif c[char1] > c[char2]:
                    return False
            else:
                if len(word1) > len(word2):
                    return False
                
        return True
    
    '''
    Time : O(N + M), where M - total number of characters, N - creating hashmap which is essentially constant time
    Space : O(N) - essentially O(1) because characters are at most of size 26
    
    '''