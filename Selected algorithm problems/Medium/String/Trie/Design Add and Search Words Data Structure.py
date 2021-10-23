'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 
Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.

'''
#TrieNode class to create node for separate letters
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    #Initialize root
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        #Start at the root
        current = self.root
        for char in word:
            #If char is not in our current node
            #create new TrieNode
            if char not in current.children:
                current.children[char] = TrieNode()
            #Move current node to the next one
            current = current.children[char]
        #Finally mark isWord flag as True indicating there is a word ending at this letter
        current.isWord = True
                
    def search(self, word: str) -> bool:
        #Dfs method to explore Trie
        def dfs(node, i):
            
            #If index is equal to length of searched word
            #we return isWord flag
            if i == len(word):
                return node.isWord
            
            #If current character is dot we should explore every possibility
            #for current node and if any of them will return True it means we can
            #match the word
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True
                    
            #if character is not word we just continue usual Trie exploration
            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            
            #Otherwise return False indicating we have not found any matched
            return False
        
        #Start dfs at the root and index 0
        return dfs(self.root, 0)