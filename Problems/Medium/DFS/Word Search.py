'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        rows, cols, n = len(board), len(board[0]), len(word)
        
        #Dfs method to explore the board
        def dfs(r, c, j):
            #Base case - if we reached end of the word
            #it means we matched every character and can return Tur
            if j == n:
                return True
            #Save the letter in order to return it
            #to its place once we have finished
            #This will prevent algorithm from checking the same
            #letter multiple times
            letter = board[r][c]
            board[r][c] = "#"
            for dr, dc in d:
                rr, cc = r + dr, c + dc
                #If new cells is inbounds and corresponds to
                #the next searched letter of a word - continue dfs
                if 0 <= rr < rows and 0 <= cc < cols and board[rr][cc] == word[j]:
                    if dfs(rr, cc, j + 1):
                        return True
                    
            board[r][c] = letter
            return False
        
        #Main loop where we enter dfs whenever current element
        #matches the first letter of our word
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    #If found - return True
                    if dfs(i, j, 1):
                        return True
        return False