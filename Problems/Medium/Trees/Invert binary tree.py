'''
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:
           4                
          / \
         2   7         
        / \ / \
       1  3 6  9    
           |
           |
           ^
           4                
          / \
         7   2         
        / \ / \
       9  6 3  1  

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''

class Solution:
    #Recursive - todo
    def invertTree_rec(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        right = self.invertTree_rec(root.right)
        left = self.invertTree_rec(root.left)
        
        root.left = right
        root.right = left
        
        return root
    
    #Iterative
    def invertTree_iter(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Method to swap children of nodes
        def swap(node):
            node.left, node.right = node.right, node.left
            
            
        q = deque([root])
        
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                if cur_node:
                    swap(cur_node)
                    
                    if cur_node.left:
                        q.append(cur_node.left)
                        
                    if cur_node.right:
                        q.append(cur_node.right)
        return root