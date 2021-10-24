'''
BinarySearch problem
You are given a two dimensional array matrix, containing strings "r", "g", and "b". Perform a floodfill operation at row r, column c with the color target.

A floodfill operation replaces elements that are connected to matrix[r][c] (up/right/down/left) and have the same color as matrix[r][c] with the color of target.

Constraints

n, m ≤ 200 where n and m are the number of rows and columns in matrix
Example 1
Input
matrix = [
    ["r", "r", "r"],
    ["r", "g", "b"],
    ["g", "b", "b"]
]
r = 0
c = 0
target = "g"
Output
[
    ["g", "g", "g"],
    ["g", "g", "b"],
    ["g", "b", "b"]
]
Explanation
The red elements connected to matrix[0][0] are replaced with "g".

'''

class Solution:
    def solve(self, matrix, r, c, target):
        rows, cols = len(matrix), len(matrix[0])
        
        #Helper array to traverse the grid in 4 directions and explore neighbourhood
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        
        #Save the value of relevant cells - the ones we need to perform flood fill on
        relevant = matrix[r][c]

        #Initialize queue starting at (r,c)
        q = deque([(r,c)])
        seen = {(r,c)}
        while q:
            x, y = q.popleft()
            #Mark current cell with target color
            matrix[x][y] = target
            
            #Explore 4 directions
            for dx, dy in d:
                xx, yy = x + dx, y + dy
                #Check if cell is inbounds and it's relevant cell we want to fill
                #also keep track of seen coordinates to avoid infinite loops
                if 0 <= xx < rows and 0 <= yy < cols and matrix[xx][yy] == relevant and (xx,yy) not in seen:
                    seen.add((xx, yy))
                    q.append((xx, yy))

        return matrix