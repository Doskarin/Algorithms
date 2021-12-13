'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:
              3
            /   \
           5     1
         /  \   / \
        6    2 0   8
            / \
           7   4      

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.

'''
class TreeNode:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        return self.dfs(root, p, q)
        
        
    def dfs(self, node, p, q):
        
        if not node:
            return None
        
        if node == p or node == q:
            return node
        
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        
        if left and right:
            return node
        
        if not left and right:
            return right
        
        if left and not right:
            return left
        
        
        '''
        Time : O(N) - worst case we might be visiting all nodes in the tree
        Space : O(N) - recursion stack
        
        '''

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        stack = [root]
        
        parent = {root : None}
        
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
                
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parent[p]
            
        while q not in ancestors:
            q = parent[q]
            
        return q
    
    '''
    Time : O(N), N - number of nodes, in the worst case we might be visiting all nodes
    Space : O(N), stack/parent hashmap/ancestor hashset - all can utilize O(N) at worst
    
    
    '''