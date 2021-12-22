'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:

       1                          2
        \                        / \
         2                      1   3
          \         =>               \
           3                          4
            \
             4


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
1 <= Node.val <= 10^5


'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nodes = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
        def build_BST(left, right):
            if left > right:
                return None
            
            mid = left + (right - left) // 2
            
            root = nodes[mid]
            
            root.left = build_BST(left, mid - 1)
            root.right = build_BST(mid + 1, right)
            
            return root
        
        return build_BST(0, len(nodes) - 1)
    
    '''
    Time : O(N)
    
    Space : O(N) - nodes array, call stack logN
    
    '''