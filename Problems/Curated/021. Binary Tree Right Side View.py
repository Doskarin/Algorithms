'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:
             1
            / \
           2   3
            \   \
             5   4



Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        from collections import deque
        
        res = [ ]
        
        q = deque([root])
        
        while q:
            
            rightMost = q.pop()
            
            if rightMost:
                res.append(rightMost.val)
            
            q.append(rightMost)
            
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)
                    
        return res
    
    '''
    Time : O(N) - we visit each node
    Space : O(D), where D - is a tree diameter, last level could contain up to N/2 tree nodes

    '''