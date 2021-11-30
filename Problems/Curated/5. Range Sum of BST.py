'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:

         10
        /  \
       5    15
      / \     \
     3   7     18


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        
        self.dfs(root, low, high)
        
        return self.total
    
    
    
    def dfs(self, node, low, high):
        if not node:
            return
        
        if low <= node.val <= high:
            self.total += node.val
            
        if node.val > low:
            self.dfs(node.left, low, high)
            
        if node.val < high:
            self.dfs(node.right, low, high)
        
    '''
    Time : O(N), N - number of nodes in the tree
    Space : O(N), space in the function call stack
    
    '''
    
    def rangeSumBST_iter(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        total = 0
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                if low <= node.val <= high:
                    total += node.val
                    
                if node.left and node.val > low:
                    stack.append(node.left)
                    
                if node.right and node.val < high:
                    stack.append(node.right)
                    
        return total
    
    '''
    Time : O(N), N - number of nodes in the tree
    Space : O(N), stack will contain no more than two levels of the nodes. The maximal number of nodes in a binary tree is N/2
    Therefore, the maximal space needed for the stack would be O(N).
    
    '''