'''
Given the root of a binary tree, return the vertical order
traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
              3
            /   \
           9    20
               /  \
              15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
              
              3
            /  \
           9    8
          / \  /  \
         4  0  1   7

Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''
class Solution:
    def verticalOrder_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        d = { }
        min_col, max_col = 0, 0
        def dfs(node, row, col):
            nonlocal min_col, max_col
            if not node:
                return
            
            if node:
                if col not in d:
                    d[col] = [(row,node.val)]
                else:
                    d[col].append((row,node.val))
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                
                dfs(node.left, row + 1, col - 1)
                
                dfs(node.right, row + 1, col + 1)
  
        
        dfs(root, 0, 0)
        
        for key in range(min_col, max_col + 1):
            d[key].sort(key = lambda x : x[0])
            
            res.append([val for row, val in d[key]])
            
        return res

    def verticalOrder_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        d = { }
        
        q = deque([(root, 0)])
        
        min_col = max_col = 0
        
        while q:
            node, col = q.popleft()
            
            if node:
                if col in d:
                    d[col].append(node.val)
                else:
                    d[col] = [node.val]
                    
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                    
                if node.left:
                    q.append((node.left, col - 1))
                    
                if node.right:
                    q.append((node.right, col + 1))
                    
        for col in range(min_col, max_col + 1):
            
            if col not in d:
                continue
            res.append(d[col])
            
        return res