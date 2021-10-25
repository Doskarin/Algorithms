'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1


'''

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        result = 0
        
        for i in range(rows):
            for j in range(cols):
                #The idea is to scan each cell in the matrix to update
                #the placeholder result variable with the number of squares
                #that can be formed from the currently looking cell (when it is the 
                #bottom right corner cell of the any possible square).
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        result += 1
                    else:
                        cur_val = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + matrix[i][j]
                        result += cur_val
                        matrix[i][j] = cur_val
        return result