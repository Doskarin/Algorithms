'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],
              [3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105

'''
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m, n = len(mat), len(mat[0])
        row, col = 0, 0
        
        res = []
        
        while len(res) < m * n:
            
            res.append(mat[row][col])
            diagonal = row + col
            
            if diagonal % 2 == 0:
                if col == n - 1:
                    row += 1
                
                elif row == 0:
                    col += 1
                    
                else:
                    row -= 1
                    col += 1
            
            else:
                if row == m - 1:
                    col += 1
                
                elif col == 0:
                    row += 1
                
                else:
                    row += 1
                    col -= 1
        return res
    
    '''
    Time : O(M*N) - we visit each element once in entire matrix
    Space : O(1) - no extra space is used, apart from result array
    
    '''