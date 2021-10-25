'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:


Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],
                ["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

'''
#For this problem we will use Trie data structure in order to
#efficiently lookup words in the dictionary
#First we build the trie and as we iterate through the board
#everytime we find some word in the trie we change isWord flag to False
#this will make sure we will not waste time next time on this word
#since we already found it
class TrieNode:
    def __init__(self):
        self.children = {}
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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        self.d = [(1,0),(0,1),(-1,0),(0,-1)]
        tree = Trie()
        #Fill in trie with words from dictionary
        for word in words:
            tree.insert(word)
            
        #Define root of the trie
        root = tree.root
        self.ans = set()
        for i in range(rows):
            for j in range(cols):
                #If letter is in our root - enter dfs
                if board[i][j] in root.children:
                    #pass coordinates, board itself,
                    #root at current letter and first part of the searched word
                    self.dfs(i, j, board, root.children[board[i][j]], board[i][j])
        return self.ans
    
    def dfs(self, i, j, board, root, word):
        #Base case - if isWord flag is True
        #it means there is a word in the trie
        #and we can safely add word to the answer
        if root.isWord:
            self.ans.add(word)
            
            #To make algorithm more efficient
            #we change isWord flag to False in order to
            #continue traversing through trie without stopping at this word
            root.isWord = False
            
        #Check if inbounds
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return
        
        #Save the letter
        letter = board[i][j]
        
        #Mark current cell as None to avoid going back to it
        board[i][j] = None
        for dx, dy in self.d:
            x, y = i + dx, j + dy
            #If new coordinate is inbounds and next letter is in current Trie's node - continue dfs
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] in root.children:
                
                #continue dfs passing new coordiates, board, new node and current part of searched word
                self.dfs(x, y, board, root.children[board[x][y]], word + board[x][y])
        
        #assign cell to its initial letter
        board[i][j] = letter