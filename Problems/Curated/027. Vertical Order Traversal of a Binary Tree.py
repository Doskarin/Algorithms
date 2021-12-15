'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

 

Example 1:
            
            3 (0,0)
           / \
          9  20     
        (1,-1) (1,1)
             / \
            15  7
         (2,0) (2,2)      
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
Example 3:


Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000


'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal_dfs(self, root: TreeNode) -> List[List[int]]:
        
        min_col = float('inf')
        max_col = float('-inf')
        
        d = { }
        
        res = [ ]
        
        def dfs(node, row, col):
            nonlocal min_col, max_col
            
            if not node:
                return
            
            if node:
                
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                
                if col not in d:
                    
                    d[col] = [(row, node.val)]
                else:
                    d[col].append((row, node.val))
                    
                if node.left:
                    dfs(node.left, row + 1, col - 1)

                if node.right:
                    dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        
        for col in range(min_col, max_col + 1):
            
            if col not in d:
                continue
                
            d[col].sort()
            res.append([val for _, val in d[col]])
            
        return res
    
    '''
    Time Complexity: W*HlogH where W is the width of the binary tree
    (i.e. the number of columns in the result) and H is the height of the tree.
    In the first part of the algorithm, 
    we traverse the tree in DFS, which results in O(N) time complexity.

    Once we build the columnTable, we then have to sort it column by column.

    Let us assume the time complexity of the sorting algorithm to be KlogK where K
    is the length of the input. The maximal number of nodes in a column would be H/2
    where H is the height of the tree, due to the zigzag nature of the node distribution. 
    As a result, the upper bound of time complexity to sort a column in a binary tree
    would be (H/2)*log(H/2).

    Since we need to sort W columns, the total time complexity of the sorting 
    operation would then be W * (H/2)*log(H/2).
    Note that, the total number of nodes N in a tree is bounded by W*H, i.e. N < W
    As a result, the time complexity of O(W*HlogH) will dominate the O(N) of the
    DFS traversal in the first part.

    At the end of the DFS traversal, we have to iterate through the 
    columnTable in order to retrieve the values, which will take another O(N) time.

    To sum up, the overall time complexity of the algorithm would be O(W⋅HlogH).

    An interesting thing to note is that in the case where the
    binary tree is completely imbalanced (e.g. node has only left child.),
    this DFS approach would have the O(N) time complexity,
    since the sorting takes no time on columns that contains only a single node.
    While the time complexity for our first BFS approach would be O(NlogN),
    since we have to sort the NN keys in the columnTable.
    
    Space: O(N) where NN is the number of nodes in the tree.

    We kept the columnTable which contains all
    the node values in the binary tree.
    Together with the keys, it would consume O(N)
    space as we discussed in previous approaches.

    Since we apply the recursion for our DFS traversal,
    it would incur additional space consumption
    on the function call stack. In the worst case where
    the tree is completely imbalanced,
    we would have the size of call stack up to O(N).

    Finally, we have the output which contains all
    the values in the binary tree, thus O(N) space.

    So in total, the overall space complexity of
    this algorithm remains O(N).
    
    '''

    def verticalTraversal_bfs(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        d = { }
        
        q = deque([(root, 0, 0)])
        
        min_col = max_col = 0
        
        while q:
            node, row, col = q.popleft()
            
            if node:
                if col in d:
                    d[col].append((row,node.val))
                else:
                    d[col] = [(row, node.val)]
                    
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                    
                if node.left:
                    q.append((node.left, row + 1, col - 1))
                    
                if node.right:
                    q.append((node.right, row + 1, col + 1))

                    
        for col in range(min_col, max_col + 1):
            
            if col not in d:
                continue
                
            d[col].sort()
            
            res.append([val for _, val in d[col]])
            
        return res
    
    '''
    Time : O(N*log(N/k)), suppose that we have a list of N
    elements, it would then O(NlogN) time to sort this list
    In total, to sort all the k sublists, it would take
    O(k * N/k *log(N/k)) = O(N*log(N/k)) which is less than the time
    complexity of sorting the original list, i.e. O(NlogN)
    
    Space : O(N)
    
    
    '''