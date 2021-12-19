'''
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],
                 [5,1,2,3],
                 [9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],
                 [2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99
 

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?

'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        from collections import defaultdict
        d = defaultdict(set)
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                d[i - j].add(matrix[i][j])
                if len(d[i - j]) > 1:
                    return False
        return True
        '''
        Time :  O(M*N)
        Space : O(M + N)
        Follow up:

        What if the matrix is stored on disk, 
        and the memory is limited such that you can
        only load at most one row of the matrix into the memory at once?
        What if the matrix is so large that you
        can only load up a partial row into the memory at once?
        
        you can barely get one row into memory,
        the hashmap approach doesn't make sense to me.
        I am thinking of an alternative to approach which is
        rather straight forward, you need to know how interaction 
        with filesystem works. Load row 1 and have pointers to 
        each column and follow along:

        For approach 1: Assuming we are dealing with example 1:

        [[1,2,3,4],
        [5,1,2,3],
        [9,5,1,2]]
        We go top down:
        Step 1: load First row 1, 2, 3, 4
        Step 2: 4 is valid so move col 3 pointer forward since thats valid 1, 2 , 3, 3;
        Step 3: 3 & 3 are valid so move col 2 and col 3 : 1, 2, 2, 2;
        Step 4: 2 & 2 & 2 are valid so move col 1, 2, 3 : 1 , 1, 1, null; (drop col 3);
        Step 5: 1 & 1 & 1 are valid so move col 0, 1, 2: 5, 5, null, null (drop col 2);
        Step 6: 5 & 5 are valid so move col 0, 1: 9, null (drop col 1);
        Step 7: 9 is valid;

        return valid;
        At most we have one "row" in memory;
        If you notice a pattern here that when moving from r->l we incrementally compare values;
        I'll leave it to you to think how you can extend this to fewer columns.
        '''