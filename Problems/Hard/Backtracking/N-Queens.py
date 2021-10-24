'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:


Input: n = 4
Output: [[".Q..",
          "...Q",
          "Q...",
          "..Q."],
         
         ["..Q.",
          "Q...",
          "...Q",
          ".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9


'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #Check if move is safe, i.e if queen is under attack. Queen is considered to be under attack if they share the same row, col or diagonal
        def isSafe(row, col, visited):
            for i, j in visited:
                if row == i or col == j or abs(row - i) == abs(col - j):
                    return False
            return True
        
        #Method to build the board
        def buildBoard(visited):
            board = [["." for _ in range(n)] for _ in range(n)]
            for i, j in visited:
                board[i][j] = "Q"
            for i in range(n):
                board[i] = "".join(board[i])
            return board
        
        #Backtracking method
        def solve(row, queens):
            #If we reached the bottom of board build the answer and append to the result
            if row == n:
                output.append(buildBoard(queens))
            for j in range(n):
                #Check if move is safe
                if isSafe(row, j, queens):
                    #Add queen to the set
                    queens.add((row, j))
                    #Proceed further
                    solve(row + 1, queens)
                    #Backtrack
                    queens.remove((row, j))
        
        output = []
        solve(0, set())
        return output