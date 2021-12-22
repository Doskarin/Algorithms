'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:
              1
             / \
            3   2
           / \   \
          5   3   9      

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 10^4].
-2^31 <= Node.val <= 2^31 - 1

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        from collections import deque
        res = []
        
        q = deque([root])
        
        while q:
            max_val = float('-inf')
            for _ in range(len(q)):
                cur_node = q.popleft()
                if cur_node:
                    max_val = max(max_val, cur_node.val)
                    if cur_node.left:
                        q.append(cur_node.left)
                    if cur_node.right:
                        q.append(cur_node.right)
            res.append(max_val)
            
        return res if root else []
    
    '''
    Time : O(N) time because we have to process each node in the tree.
	Space : O(N) space because there are N nodes
    in the tree that will be added to the queue in the worst case.
    
    '''