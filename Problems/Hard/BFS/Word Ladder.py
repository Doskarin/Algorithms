'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.


'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #Create word set in order to track our progress as we go through BFS
        word_set = set(wordList)
        
        #Flag in order to stop earlier in case we have not found desired endWord in our set
        isPresent = False
        for word in word_set:
            if word == endWord:
                isPresent = True
                break
        if not isPresent:
            return 0
        
        #Initialize queue starting with beginWord
        q = deque([beginWord])
        dist = 1
        
        while q:
            #Iterate over entire frontier of queue
            for _ in range(len(q)):
                cur_word = q.popleft()
                #Pop current word and transform it into the array so that we can change words one by one
                #and check if it is our target word or it is in our set
                temp = [char for char in cur_word]
                for i in range(len(temp)):
                    #Save current letter in order to return it to its place after we are done with iteration
                    letter = temp[i]
                    for char in ascii_lowercase:
                        temp[i] = char
                        changed_word = ''.join(temp)
                        
                        #If transformed word is our current word - we do nothing
                        if changed_word == cur_word:
                            continue
                        #If happens that we found our target word - return distance + 1 
                        if changed_word == endWord:
                            return dist + 1
                        #If it is in our word set it means that we could possibly be one step closer
                        #to finding target word - add word to the queue and remove word from the set
                        if changed_word in word_set:
                            word_set.remove(changed_word)
                            q.append(changed_word)
                    #return letter to its place
                    temp[i] = letter
            #Increase frontier distance
            dist += 1
        return 0